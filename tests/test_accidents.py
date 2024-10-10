import pytest
from pymongo import MongoClient
from pymongo.synchronous.collection import Collection
from repository.accidents_repo import get_sum_accidents_by_beat, count_accidents_by_day_and_beat, \
    count_accidents_by_week_and_beat


@pytest.fixture
def init_db():
    client = MongoClient

def test_get_sum_accidents_by_beat():
    result = get_sum_accidents_by_beat('225')
    assert result == 268

def test_count_accidents_by_day_and_beat():
    result = count_accidents_by_day_and_beat('424', '10/18/2020')
    assert result == 1

def test_count_accidents_by_week_and_beat():
    result = count_accidents_by_week_and_beat('424', '10/18/2020')
    assert result == 1


def count_accidents_by_day_and_week_and_beat():
    pass


def test_count_accidents_by_day_and_week_and_beat():
    result = count_accidents_by_week_and_beat('424', '10/18/2020')
    assert result == 1

