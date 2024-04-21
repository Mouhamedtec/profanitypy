import requests
import json

BASE_URL = "https://vector.profanity.dev"

class ProfanityApi(object):
    def __init__(self, extra_headers={}):
        self.headers = {'Content-Type': 'application/json'}
        self.extra_headers = extra_headers
        self.message = None
        self.result = None

        if self.extra_headers:
            self.merge_headers()

    def merge_headers(self):
        if isinstance(self.extra_headers, dict):
            self.headers.update(self.extra_headers)

    def build_request(self):
        response = requests.post(
            url = BASE_URL,
            headers=self.headers,
            json = {'message':self.message}
        )

        if response.status_code == 200:
            self.result = json.loads(response.content.decode(encoding="utf-8"))

        return self.result

    def check_profanity(self, message):
        self.message = message
        self.build_request()
        return self
    
    @property
    def score(self):
        return self.result['score']

    @property
    def profanity(self):
        return self.result['isProfanity']
