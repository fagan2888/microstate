from microstate.redis_config import REDIS_TEST_CONFIG
import random
from microstate.client import MicroStateWriter

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


def dont_test_client():
    """ Test on actual redis instance """
    client = MicroStateWriter(write_key=TEST_WRITE_KEY)
    k = random.choice(list(range(10)))
    for value in TEST_VALUES:
        res1 = client.set(k=k, value=value)
        value_back = client.get(k=k)
        if isinstance(value,(list,dict,tuple,str)):
            assert deep_equal(value, value_back)
        elif isinstance(value, int):
            assert int(value_back) == value
        elif isinstance(value, float):
            assert abs(float(value_back) - value) < 1e-6
