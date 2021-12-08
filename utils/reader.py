import json
import os

from test_reusables.service.logger_level import LogLevel
from utils.logger import log


class Reader:
    @staticmethod
    def get_service_endpoints(service_name):
        file_path = os.path.join(os.path.abspath(''), "config/base_urls.json")
        with open(file_path, "r") as read_file:
            service_name_json = read_file.read()
        try:
            value = json.loads(service_name_json)[os.environ['env']][service_name]
            log("Service URL captured --> Key: " + service_name + "Value: " + value, LogLevel.INFO)
            return value
        except KeyError as ex:
            log("Please provider valid Service Name: " + str(ex), LogLevel.ERROR)
            log("Given Information, ServiceName: " + service_name, LogLevel.INFO)
            return " "

    @staticmethod
    def get_api_routes(service_name, route_name):
        file_path = os.path.join(os.path.abspath(''), "config/routes.json")
        with open(file_path, "r") as read_file:
            routes_json = read_file.read()
        try:
            value = json.loads(routes_json)[service_name][route_name]
            log("Service URL captured --> Key: " + service_name + "Value: " + value, LogLevel.INFO)
            return value
        except NameError as ex:
            print("Please provider valid Service Name & routes Details: " + str(ex), LogLevel.ERROR)
            print("Given Information, ServiceName: " + service_name + " route: " + route_name, LogLevel.INFO)
            return " "
