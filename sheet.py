from collections import defaultdict
import json
import jsonschema
import os
import re
from typing import Optional
import uuid

from calculate import calculate, CalculationError
from parse import parse, ParseError
from value import Value, UnknownValue, TypedValue

re_cell_id = re.compile(r'^[a-zA-Z0-9-_]+$')
re_cell_name = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')

with open('cell_schema.json', 'r') as f:
    cell_schema = json.load(f)

sheet_schema = {
    'type': 'object',
    'properties': {
        'cells': {
            'type': 'object',
            'patternProperties': {
                r'^[a-zA-Z0-9-_]+$': cell_schema
            }
        }
    },
    'required': ['cells']
}

def _name_to_filename(name: uuid.UUID, must_exist:bool=False) -> str:
    if not isinstance(name, uuid.UUID):
        raise ValueError('Invalid sheet name')

    filename = f'data/sheet/{str(name)}.json'
    if must_exist and not os.path.exists(filename):
        raise ValueError('Sheet does not exist')

    return filename

def load_sheet(name: uuid.UUID) -> Optional[dict]:
    filename = _name_to_filename(name, must_exist=False)
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            result = json.load(f)
            jsonschema.validate(result, sheet_schema)
            return result
    else:
        return None

def _save_sheet(name: uuid.UUID, sheet: dict, must_exist:bool=False) -> None:
    filename = _name_to_filename(name, must_exist)
    jsonschema.validate(sheet, sheet_schema)
    with open(filename, 'w') as f:
        json.dump(sheet, f, indent=2)

def update_cell_calc_and_save(name: uuid.UUID, sheet: dict, cell_id: str, data: dict) -> None:
    filename = _name_to_filename(name, must_exist=True)

    if not re_cell_id.match(cell_id):
        raise ValueError('Invalid cell ID')

    op = data.get('metadata',{}).get('op')
    if op == 'create':
        if cell_id in sheet['cells']:
            raise ValueError('Cell already exists')
    elif op == 'update':
        if cell_id not in sheet['cells']:
            raise ValueError('Cell does not exist')

    jsonschema.validate(data, cell_schema)
    sheet['cells'][cell_id] = dict(data)
    del sheet['cells'][cell_id]['metadata']
    _calculate_all(sheet)
    _save_sheet(name, sheet, must_exist=True)

def delete_cell_calc_and_save(name: uuid.UUID, sheet: dict, cell_id: str) -> None:
    filename = _name_to_filename(name, must_exist=True)

    if not re_cell_id.match(cell_id):
        raise ValueError('Invalid cell ID')

    if cell_id not in sheet['cells']:
        raise ValueError('Cell does not exist')

    del sheet['cells'][cell_id]
    _calculate_all(sheet)
    _save_sheet(name, sheet, must_exist=True)

def _calculate_all(sheet: dict) -> None:
    for cell_id, cell in sheet['cells'].items():
        cell['computed'] = {'value':'', 'type':'', 'error':None}

    formulas = {}  # indexed by cell id
    values = {}    # indexed by cell name

    for cell_id, cell in sheet['cells'].items():
        if not re_cell_name.match(cell['name']):
            cell['computed']['error'] = 'Invalid cell name'
        elif any(c['name'] == cell['name'] for i,c in sheet['cells'].items() if cell_id != i):
            cell['computed']['error'] = 'Duplicate cell name'
        else:
            try:
                formulas[cell_id] = parse(cell['formula'])
                values[cell['name']] = UnknownValue()
            # Catch a ParseError or CalculationError and add it to the cell
            except (ParseError, CalculationError) as e:
                cell['computed']['error'] = str(e)

    # Repeatedly calculate cells until no more cells can be calculated
    while True:
        changed = False
        for cell_id in formulas:
            cell = sheet['cells'][cell_id]
            cell_name = cell['name']

            if values[cell_name].complete:
                continue

            try:
                new_value = calculate(formulas[cell_id], values)
                if new_value != values[cell_name]:
                    cell['computed']['value'] = str(new_value)
                    cell['computed']['type'] = new_value.type_string
                    values[cell_name] = new_value
                    changed = True
            except CalculationError as e:
                cell['computed']['error'] = str(e)

        if not changed:
            break

    # Go over any incomplete ones that don't already have an error string
    # and mark them as cyclic dependencies
    for cell_id in formulas:
        cell = sheet['cells'][cell_id]
        cell_name = cell['name']
        if not values[cell_name].complete and cell['computed']['error'] is None:
            cell['computed']['error'] = 'Cyclic dependency'

def calculate_all_and_save(name: uuid.UUID, sheet: dict) -> None:
    filename = _name_to_filename(name, must_exist=True)
    _calculate_all(sheet)
    _save_sheet(name, sheet, must_exist=True)
