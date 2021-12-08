import dpath.util
import ipdb

from test_reusables.service.logger_level import LogLevel
from utils.logger import log


class JsonManipulator:
    def __init__(self):
        pass

    @staticmethod
    def custom_payload_updater(_payload, _input_param):
        """
            Alters the default payload based on the given input
        """
        for input_key in _input_param:
            if len(dpath.util.search(_payload, input_key)) != 0:
                dpath.util.set(_payload, input_key, _input_param[input_key])
            else:
                log('Could not update input key ===> ' + input_key, LogLevel.ERROR)
                return {}
        log("Generated Payload is: " + str(_payload), LogLevel.INFO)
        return _payload

    @staticmethod
    def add_new_key_to_payload(_payload, _input_param):
        """
            Adds new key value pair to the default payload based on the given input
        """

        for input_key in _input_param:
            if len(dpath.util.search(_payload, input_key)) == 0:
                dpath.util.new(_payload, input_key, _input_param[input_key])
            else:
                log('Input Key is already present ===> ' + input_key, LogLevel.ERROR)
                return {}
        log("Keys added in payload. Updated payload: " + str(_payload), LogLevel.INFO)
        return _payload

    @staticmethod
    def validate_value_present(_payload, _input_param):
        """
            Validate and return Difference in JSON data
        """
        _result_json = []
        for input_key, input_value in _input_param.items():
            if len(dpath.util.search(_payload, input_key)) == 0:
                _result_json.append({
                    "wrong_input_path": input_key
                })
            else:
                if not dpath.util.get(_payload, input_key) == input_value:
                    _result_json.append({
                        "json_path": input_key,
                        "expected": input_value,
                        "actual": dpath.util.get(_payload, input_key)
                    })
        log("Result JSON -> " + str(_result_json), LogLevel.INFO)
        return _result_json
