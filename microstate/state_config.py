import os
from sys import platform
from getjson import getjson

# Load a couple of environment variables for local testing.
# These are secrets on github.
try:
    from microstate.state_config_private import NOTHING_MUCH
except:
    pass

state_config_url = os.getenv('STATE_CONFIG_URL')
state_config_failover_url = os.getenv('STATE_CONFIG_FAILOVER_URL')
REDIZ_STATE_CONFIG = getjson(url=state_config_url, failover_url=state_config_failover_url)
if REDIZ_STATE_CONFIG is None:
    raise Exception('Could not get configuration')

if platform == 'darwin':
    REDIZ_STATE_CONFIG['local'] = True
