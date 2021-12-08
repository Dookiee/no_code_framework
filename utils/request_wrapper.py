import os

import ipdb
import requests

from test_reusables.service.logger_level import LogLevel
from utils.general_utilies import GeneralUtilities
from utils.logger import log


class Requests:

    def __init__(self):
        pass

    def get(self, _url, _auth="", _body="", _retries=os.environ["api_retry_limit"]):
        if not _auth and not _body:
            response = requests.get(url=_url)
        elif not _body:
            response = requests.get(url=_url, auth=_auth)
        else:
            response = requests.get(url=_url, auth=_auth, body=_body)
        log(f'API Method: GET | URL:- {_url}', LogLevel.INFO)
        log(f"Status Code:- {response.status_code}", LogLevel.INFO)
        log("API Response:- ", LogLevel.INFO)
        log(response.text, LogLevel.INFO)
        log(f"Time taken:- {response.elapsed}", LogLevel.INFO)
        log("*******", LogLevel.INFO)
        if response.status_code >= 500 and _retries <= _retries:
            log(f'Retry count for PUT API - {_retries}', LogLevel.INFO)
            GeneralUtilities().custom_sleep_time(os.environ["api_wait_time"])
            response = self.get(_url, _auth=_auth, _params=_body, _retries=_retries+1)
        return Requests.parse_response(response)

    @staticmethod
    def parse_response(response):
        try:
            response.json()
            return response
        except Exception as e:
            log(f"Response not json! - {e}", LogLevel.ERROR)
            log(f"Raw response is - {response}", LogLevel.ERROR)
            return response



