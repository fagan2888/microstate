from microstate.conventions import MicroStateConventions
import requests


class MicroStateWriter(MicroStateConventions):

    def __init__(self, write_key, **kwargs):
        super().__init__(**kwargs)
        self.write_key = write_key
        self.state_base_url = self.base_url.replace('devapi', 'state').replace('api','state')
          # For now, unit this is brought into the main API

    def delete_state(self, k:int):
        method = 'delete_state'
        res = requests.get(self.state_base_url + '/' + method + '/' + self.write_key, params={'k': k})
        if res.status_code == 200:
            return res.json()

    def get_state(self, k: int):
        method = 'get_state'
        res = requests.get(self.state_base_url + '/' + method + '/' + self.write_key, data={'k': k})
        if res.status_code == 200:
            return res.json()

    def set_state(self, k: int, value):
        method = 'set_state'
        params = {'k': k, 'value': value}
        res = requests.put(self.state_base_url + '/' + method + '/' + self.write_key, params=params)
        if res.status_code == 200:
            return res.json()
