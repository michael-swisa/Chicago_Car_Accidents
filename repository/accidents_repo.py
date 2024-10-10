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


