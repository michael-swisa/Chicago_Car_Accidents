from flask import jsonify, Blueprint
from services.loat_data import load_data_to_db_service

bp_load_data = Blueprint('load_data', __name__)


@bp_load_data.route('', methods=['POST'])
def load_data():
    load_data_to_db_service()
    return jsonify({'status': 'success'}), 201
