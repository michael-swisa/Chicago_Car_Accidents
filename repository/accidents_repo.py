from datetime import datetime, timedelta

from database.connect import Accidents


def get_sum_accidents_by_beat(beat):
    result = Accidents.count_documents({'LOCATION.BEAT_OF_OCCURRENCE': beat})
    return result


def count_accidents_by_day_and_beat(beat, date):
    count = Accidents.count_documents({
        'LOCATION.BEAT_OF_OCCURRENCE': beat,
        'DATES.CRASH_DATE': {'$regex': f'^{date}'}
    })
    return count


def count_accidents_by_week_and_beat(beat, start_date):
    start_date_obj = datetime.strptime(start_date, "%m/%d/%Y")
    end_date_obj = start_date_obj + timedelta(days=7)
    start_date_str = start_date_obj.strftime("%m/%d/%Y")
    end_date_str = end_date_obj.strftime("%m/%d/%Y")
    count = Accidents.count_documents({
        'LOCATION.BEAT_OF_OCCURRENCE': beat,
        'DATES.CRASH_DATE': {
            '$gte': start_date_str,
            '$lt': end_date_str
        }
    })
    return count


def count_accidents_by_month_from_date(beat, start_date):
    start_date_obj = datetime.strptime(start_date, "%m/%d/%Y")
    month_start = start_date_obj.replace(day=1)
    if start_date_obj.month == 12:
        month_end = month_start.replace(year=start_date_obj.year + 1, month=1)
    else:
        month_end = month_start.replace(month=start_date_obj.month + 1)
    count = Accidents.count_documents({
        'LOCATION.BEAT_OF_OCCURRENCE': beat,
        'DATES.CRASH_DATE': {
            '$gte': month_start.strftime("%m/%d/%Y"),
            '$lt': month_end.strftime("%m/%d/%Y")
        }
    })
    return count


def group_accident_by_cause(beat):
    result = Accidents.aggregate([
        {'$match': {
                'LOCATION.BEAT_OF_OCCURRENCE': beat }
        },
        {'$group': {
                '_id': '$PRIM_CONTRIBUTORY_CAUSE',
                'count': {
                    '$sum': 1 }
            }
        }
    ])
    return list(result)

def get_injured_statistics(beat):
    total_injured = Accidents.find({'LOCATION_ID.BEAT_OF_OCCURRENCE': beat})
    count = 0
    count2 = 0
    for i in list(total_injured):
        injuries_total = i['INJURIES']['INJURIES_TOTAL']
        if injuries_total and injuries_total.isdigit():
            count += int(injuries_total)

        injuries_fatal = i['INJURIES']['INJURIES_FATAL']
        if injuries_fatal and injuries_fatal.isdigit():
            count2 += int(injuries_fatal)

    no_ded = count - count2

    return {'count': count, 'count2': count2, 'no_ded': no_ded}