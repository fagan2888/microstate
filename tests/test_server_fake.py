from microstate.server import MicroStateServer
from microstate.state_test_config import REDIZ_STATE_TEST_CONFIG
from pprint import pprint
import random
import json

TEST_WRITE_KEY = REDIZ_STATE_TEST_CONFIG['SHOOTABLE_CAT']


def test_set_get():
    server = MicroStateServer(decode_responses=True)
    k = random.choice(list(range(10)))
    VALUES = [{'frogs legs': 11}, 11, 'dog', 3.14156]
    for value in VALUES:
        res1 = server.set(write_key=TEST_WRITE_KEY, k=0, value=value)
        value_back = server.get(write_key=TEST_WRITE_KEY, k=0)
        if server.is_dict_value(value):
            jvalue = json.loads(value_back)
            assert jvalue == value
        elif isinstance(value, str):
            assert value == value_back
        elif isinstance(value, int):
            assert int(value_back) == value
        elif isinstance(value, float):
            assert abs(float(value_back) - value) < 1e-6


def test_123():
    print('hello')
