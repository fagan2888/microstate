
from microstate.state_test_config import REDIZ_STATE_TEST_CONFIG
TEST_WRITE_KEY = REDIZ_STATE_TEST_CONFIG['SHOOTABLE_CAT']

def test_state_config():
    assert 'host' in REDIZ_STATE_TEST_CONFIG

