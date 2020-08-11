from microconventions import MicroConventions
from microconventions.value_conventions import ValueConventions
import json
import requests


class MicroStateConventions(MicroConventions):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def jsonify(value):
        """ Convention used by MicroStateWriter """
        # TODO: We can remove this after MicroConventions 0.1.0 is pushed
        if ValueConventions.is_valid_value(value):
            return value
        elif ValueConventions.is_dict_value(value):
            return json.dumps(value)

