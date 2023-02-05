from collections import defaultdict
import json
import jsonschema
import os
import re
from typing import Optional
import uuid

from calculate import calculate, CalculationError, get_dependencies, CellInfo, get_subcell_dims, get_subcell_dim_names
from parse import parse, ParseError, Import
from display import tensorlike_to_str, type_to_str
from external_resources import get_external_resource, ImportError

max_sheet_size = 10_000_000

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
    string = json.dumps(sheet, indent=2)
    if len(string) > max_sheet_size:
        raise Exception("Sheet exceeds maximum size")
    with open(filename, 'w') as f:
        f.write(string)

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
    values = {}    # indexed by (cell id, subcell)
    dependencies = {} # indexed by (cell id, subcell)
    cell_info = {} # indexed by cell name
    error_cells = set()

    for cell_id, cell in sheet['cells'].items():
        if not re_cell_name.match(cell['name']):
            cell['computed']['error'] = 'Invalid cell name'
        elif any(c['name'] == cell['name'] for i,c in sheet['cells'].items() if cell_id != i):
            cell['computed']['error'] = 'Duplicate cell name'
        else:
            formula = parse(cell['formula'])
            formulas[cell_id] = formula
            cell_info[cell['name']] = CellInfo(cell_id, get_subcell_dims(formula))

    for cell_name, cellinfo in cell_info.items():
        cell_id = cellinfo.cell_id
        cell = sheet['cells'][cell_id]
        try:
            formula = formulas[cell_id]
            if isinstance(formula, Import):
                resource = get_external_resource(formula.name)
                values[(cell_id, ())] = resource
            else:
                for subcells in cellinfo.list_subcells():
                    subcell_args = dict(zip(get_subcell_dim_names(formula), subcells))
                    deps = get_dependencies(formula, (), subcell_args, cell_info)
                    dependencies[(cell_id, subcells)] = deps
                    if cell['computed']['error'] is None:
                        formulas[cell_id] = parse(cell['formula'])
        # Catch a ParseError or CalculationError and add it to the cell
        except (ParseError, CalculationError, ImportError) as e:
            cell['computed']['error'] = str(e)

    # Repeatedly calculate cells until no more cells can be calculated
    while True:
        # Find a formula where all of its dependencies have been calculated
        chosen_cell_id = None
        chosen_subcell = None
        for cell_id, subcell in dependencies.keys() - values.keys() - error_cells:
            if all(d in values for d in dependencies[(cell_id, subcell)]):
                chosen_cell_id = cell_id
                chosen_subcell = subcell
                break

        # If no formula was found, then we're done
        if chosen_cell_id is None:
            break

        chosen_cell = sheet['cells'][chosen_cell_id]

        # Calculate the chosen formula
        try:
            val = calculate(formulas[chosen_cell_id], dict(values), cell_info, subcell).value
            values[(chosen_cell_id, chosen_subcell)] = val
            chosen_cell['computed']['value'] = tensorlike_to_str(val)
            chosen_cell['computed']['type'] = type_to_str(val)
        except CalculationError as e:
            sheet['cells'][chosen_cell_id]['computed']['error'] = str(e)
            error_cells.add((chosen_cell_id, chosen_subcell))

        #del formulas[chosen_cell_id]

    # Go over any unvisited ones and mark them as cyclic dependencies
    for cell_id, _ in dependencies.keys() - values.keys() - error_cells:
        cell = sheet['cells'][cell_id]
        cell['computed']['error'] = 'Cyclic dependency'

def calculate_all_and_save(name: uuid.UUID, sheet: dict) -> None:
    filename = _name_to_filename(name, must_exist=True)
    _calculate_all(sheet)
    _save_sheet(name, sheet, must_exist=True)
