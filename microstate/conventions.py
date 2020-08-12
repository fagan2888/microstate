from microconventions import MicroConventions
from microconventions.value_conventions import ValueConventions
import json
import numpy as np


try:
    from microconventions.redis_conventions import has_nan
except ImportError:
    # TODO: Toss this after microconventions 0.1.0 pushed
    def has_nan(obj):
        if isinstance(obj, list):
            return any(map(has_nan, obj))
        elif isinstance(obj, dict):
            return has_nan(list(obj.values())) or has_nan(list(obj.keys()))
        else:
            try:
                return np.isnan(obj)
            except:
                return False


class MicroStateConventions(MicroConventions):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def to_redis_value(value):
        """ Used by MicroStateWriter prior to storage in redis database """
        # TODO: We can remove this after MicroConventions 0.1.0 is pushed
        if ValueConventions.is_valid_value(value):
            return value
        elif ValueConventions.is_dict_value(value) or ValueConventions.is_vector_value(value):
            if has_nan(value):
                raise Exception('Values with NaN cannot be stored, sorry')
            else:
                try:
                    return json.dumps(value)
                except Exception as e:
                    raise Exception('Value cannot be JSON dumped so cannot be stored '+str(e) )

    @staticmethod
    def from_redis_value(value):
        """ Used by MicroStateWriter to infer a Python type """
        # Note: will not try to convert string back to int or float.
        # If you wish to preserve type then make it dict, tuple or list
        try:
            native = json.loads(value)
            if isinstance(native, (dict,list,tuple)):
                return native
            else:
                return value
        except Exception as e:
            return value