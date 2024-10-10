from repository.accidents_repo import get_sum_accidents_by_beat


def sum_accidents_by_beat_service(bate):
    result = get_sum_accidents_by_beat(bate)
    return result