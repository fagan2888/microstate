from microstate.server import MicroStateServer
from microstate.redis_config import REDIS_TEST_CONFIG
from pprint import pprint
import random
import json

TEST_WRITE_KEY = REDIS_TEST_CONFIG['SHOOTABLE_CAT']

try:
    from microconventions.equality_conventions import deep_equal
except ImportError:
    from deepdiff import DeepDiff
    # TODO: Discard after microconventions 0.1.0 released
    def deep_equal(obj1, obj2):
        return not DeepDiff(obj1, obj2, ignore_order=True)

TEST_VALUES = [{'frogs legs': 11},
                 11,
                 'dog',
                 3.14156,
                 ('sam', 17),
                 ('sam', {'mary': 11, 'bob': 32})]


def dont_test_server():
    """ Test on actual redis instance """
    server = MicroStateServer(**REDIS_TEST_CONFIG)
    k = random.choice(list(range(10)))
    for value in TEST_VALUES:
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
