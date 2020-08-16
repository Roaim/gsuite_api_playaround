from flask import Blueprint, request, jsonify

from ..services.sheet_service import read_sheet, write_sheet

bp = Blueprint('sheet', __name__, url_prefix='/sheets')


@bp.route('/', defaults={'sheet_id': None})
@bp.route('/<sheet_id>')
def get_sheet(sheet_id):
    range_name = request.args.get('range')
    return jsonify(read_sheet(sheet_id, range_name))


@bp.route('/<sheet_id>', methods=('POST',))
def update_sheet(sheet_id):
    range_name = request.args.get('range')
    body = request.get_json()
    return jsonify(write_sheet(body, sheet_id, range_name))
