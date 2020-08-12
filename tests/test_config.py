
from microstate.redis_config import REDIS_TEST_CONFIG, REDIS_CONFIG
TEST_WRITE_KEY = REDIS_TEST_CONFIG['SHOOTABLE_CAT']

# Also a test of github secrets

def test_state_config():
    assert 'host' in REDIS_CONFIG
    assert 'host' in REDIS_TEST_CONFIG


