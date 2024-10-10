from flask import jsonify, Blueprint, request

from repository.accidents_repo import count_accidents_by_day_and_beat, count_accidents_by_week_and_beat, \
    count_accidents_by_month_from_date
from services.accidents_service import sum_accidents_by_beat_service

bp_accident = Blueprint('accident', __name__)

@bp_accident.route('/by_beat/<string:beat>',methods=['GET'])
def accidents_by_beat(beat):
    result = sum_accidents_by_beat_service(beat)
    return jsonify({
        'beat': beat,
        'accidents': result
    })

@bp_accident.route('/by_date_beat',methods=['GET'])
def accidents_by_date_and_beat():
    data = request.get_json()
    start_date = data['start_date']
    type_date = data['type_date']
    beat = data['beat']
    if type_date == "day":
        result= count_accidents_by_day_and_beat(beat,start_date)
    elif type_date == "week":
        result= count_accidents_by_week_and_beat(beat,start_date)
    else:
        result= count_accidents_by_month_from_date(beat,start_date)
    return jsonify({'result':result}),200