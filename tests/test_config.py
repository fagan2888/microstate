
from microstate.redis_config import REDIS_TEST_CONFIG, REDIS_CONFIG
TEST_WRITE_KEY = REDIS_TEST_CONFIG['SHOOTABLE_CAT']

def test_state_config():
    assert 'host' in REDIS_CONFIG

