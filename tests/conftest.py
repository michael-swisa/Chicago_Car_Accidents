import pytest
from pymongo import MongoClient
from  pymongo.collation import Collation


@pytest.fixture
def init_db():
    client = MongoClient('mongodb://localhost:27017')
    test_db = client['test_db']
    yield test_db
    client.drop_database('test_db')
    client.close()


@pytest.fixture
def users_db(init_db):
    return init_db['Chicago_Car_Accidents']
