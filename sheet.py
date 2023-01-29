import json
import jsonschema
import os
import re
from typing import Optional
import uuid

from calculate import calculate, CalculationError
from parse import parse, ParseError

re_cell_id = re.compile(r'^[a-zA-Z0-9-_]+$')

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
    with open(filename, 'w') as f:
        json.dump(sheet, f, indent=2)

def update_cell_and_save(name: uuid.UUID, sheet: dict, cell_id: str, data: dict) -> dict:
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
    _save_sheet(name, sheet, must_exist=True)
    return sheet['cells'][cell_id]

def delete_cell_and_save(name: uuid.UUID, sheet: dict, cell_id: str) -> None:
    filename = _name_to_filename(name, must_exist=True)

    if not re_cell_id.match(cell_id):
        raise ValueError('Invalid cell ID')

    if cell_id not in sheet['cells']:
        raise ValueError('Cell does not exist')

    del sheet['cells'][cell_id]
    _save_sheet(name, sheet, must_exist=True)

def calculate_all_and_save(name: uuid.UUID, sheet: dict) -> None:
    filename = _name_to_filename(name, must_exist=True)

    for cell_id, cell in sheet['cells'].items():
        cell['computed'] = {}

    for cell_id, cell in sheet['cells'].items():
        try:
            formula = parse(cell['formula'])
            cell['computed']['value'] = str(calculate(formula))
        # Catch a ParseError or CalculationError and add it to the cell
        except (ParseError, CalculationError) as e:
            cell['computed']['error'] = str(e)

    _save_sheet(name, sheet, must_exist=True)
