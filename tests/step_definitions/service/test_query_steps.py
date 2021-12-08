import json

import ipdb
from pytest_bdd import scenarios, when, parsers, then

from test_reusables.service.logger_level import LogLevel
from utils.json_manipulator import JsonManipulator

from utils.logger import log
from utils.reader import Reader
from utils.request_wrapper import Requests

scenarios('../../features/service')

requests = Requests()


@then(parsers.parse('the response contains results for {code:Number}', extra_types=dict(Number=int)))
def response_validation(_response, code):
    assert _response.status_code == code, "Expecting Status code: " + \
                                          str(code) + " Actual Status Code is: " + str(_response.status_code)


@when(parsers.parse("Create {operation:String} Request in {service_name:String} {route:String} API: "
                    "{query_param:String} as query param: {query_string:String} as query string",
                    extra_types=dict(String=str)), target_fixture='_response')
def get_with_query_param(operation, service_name, route, query_param, query_string):
    _end_point = Reader.get_service_endpoints(service_name)
    _route = Reader.get_api_routes(service_name, route)
    _url = _end_point + _route + query_param.format(query_string)
    if operation.upper() == 'GET':
        return requests.get(_url)


@then(parsers.parse("I validate the response against {validation_json:String}", extra_types=dict(String=str)))
def validate_response(_response, validation_json):
    _result = JsonManipulator().validate_value_present(_response.json(), json.loads(validation_json))
    assert _result == [], json.dumps(_result, indent = 4)

