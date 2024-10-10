from flask import jsonify, Blueprint
from services.accidents_service import sum_accidents_by_beat_service

bp_accident = Blueprint('accident', __name__)

@bp_accident.route('/by_beat/<string:beat>',methods=['GET'])
def accidents_by_beat(beat):
    result = sum_accidents_by_beat_service(beat)
    return jsonify({
        'beat': beat,
        'accidents': result
    })

