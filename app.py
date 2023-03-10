from flask import Flask, send_file, request, abort
from typing import Optional

import sheet

sheet_dict = {}

def get_sheet(name: str) -> dict:
    if name not in sheet_dict:
        s = sheet.load_sheet(name)
        if s is None:
            abort(404)
        sheet_dict[name] = s
    return sheet_dict[name]

app = Flask(__name__)

@app.route('/sheet/<uuid:sheet_id>')
def show_sheet(sheet_id):
    s = get_sheet(sheet_id)
    return send_file('frontend/sheet.html')

@app.route('/sheet/<uuid:sheet_id>/data')
def get_all_cells(sheet_id):
    s = get_sheet(sheet_id)
    return s

@app.route('/sheet/<uuid:sheet_id>/calc', methods=['POST'])
def calc_all(sheet_id):
    s = get_sheet(sheet_id)
    sheet.calculate_all_and_save(sheet_id, s)
    return s

@app.route('/sheet/<uuid:sheet_id>/cell/<cell_id>', methods=['PUT', 'DELETE'])
def cell_op(sheet_id, cell_id):
    if request.method == 'PUT':
        s = get_sheet(sheet_id)
        sheet.update_cell_calc_and_save(sheet_id, s, cell_id, request.json)
        return s
    elif request.method == 'DELETE':
        s = get_sheet(sheet_id)
        sheet.delete_cell_calc_and_save(sheet_id, s, cell_id)
        return s
    else:
        raise Exception('Invalid request method')
