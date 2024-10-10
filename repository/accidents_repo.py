from datetime import datetime, timedelta

from database.connect import Accidents


def get_sum_accidents_by_beat(beat):
    result = Accidents.count_documents({'LOCATION.BEAT_OF_OCCURRENCE': beat})
    return result



