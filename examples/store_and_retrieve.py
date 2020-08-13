from microstate.client import MicroStateWriter
from pprint import pprint

# Step 1: You need a key
try:
    from microstate.redis_config import REDIS_TEST_CONFIG
    write_key = REDIS_TEST_CONFIG['SHOOTABLE_CAT']
except ImportError:
    write_key = 'YOUR WRITE KEY HERE'

# Step 2: Instantiate writer
writer = MicroStateWriter(write_key=write_key)

MODEL_PARAMS = [{'frogs legs': 11},
                11,
                'dog',
                3.14156,
                ['sam', 17],
                ['sam', {'mary': 11, 'bob': 32}]]

if __name__ == '__main__':
    # Step 3: Use it
    pprint(writer.set(value=MODEL_PARAMS))
    params_back = writer.get()
    pprint(params_back)
