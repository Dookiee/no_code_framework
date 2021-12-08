import multiprocessing
import os
import warnings

import allure
import ipdb
import pytest
import six

from test_reusables.service.logger_level import LogLevel
from utils.logger import log, get_log_file_name, get_log_file_directory, get_log_file_path

warnings.filterwarnings("ignore")


def pytest_addoption(parser):
    """
        Fetches addoption from CLI
    """
    parser.addoption("--env", action="store", required=False, default="test",
                     help="Environment arguments. Eg: --env test")
    parser.addoption("--api_retry_limit", action="store", required=False, default="1",
                     help="API retry limit - if we get 500 in any API it will retry Eg: --api_retry_limit 1")
    parser.addoption("--log_level", action="store", required=False, default="DEBUG",
                     help="Logging level Eg: --log_level DEBUG/INFO/WARN/ERROR")
    parser.addoption("--api_wait_time", action="store", required=False, default="30",
                     help="Wait Time in seconds for API Eg: --api_wait_time DEBUG/INFO/WARN/ERROR")


def pytest_configure(config):
    """
        Prerequisites which needs to done in Before Suite
    """
    os.environ["env"] = config.getoption("--env")
    os.environ["api_retry_limit"] = config.getoption("--api_retry_limit")
    os.environ["log_level"] = config.getoption("--log_level")
    os.environ["api_wait_time"] = config.getoption("--api_wait_time")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
        To store add test result in the log
    """
    outcome = yield
    rep = outcome.get_result()
    # if rep.when == 'call':
    #     if '_response' in getattr(item, 'fixturenames', ()):
    #         ipdb.set_trace()
    if rep.when == 'call' and rep.outcome == 'passed':
        log("=============== TEST RESULT ====> " + rep.outcome + " ===============", LogLevel.INFO)
        allure.attach.file(get_log_file_path(), get_log_file_name(), allure.attachment_type.TEXT)
    if rep.outcome == 'failed':
        log(f"=============== Setup Result ====> {rep.outcome} >>> ===============", LogLevel.ERROR)
        log(f"=============== Failure Reason ==> {str(call.excinfo)} ===============", LogLevel.ERROR)
        allure.attach.file(get_log_file_path(), get_log_file_name(), allure.attachment_type.TEXT)
    elif rep.outcome == "skipped":
        log("=============== Skipping Reason ==> " + str(call.excinfo) + " ===============", LogLevel.WARNING)
        allure.attach.file(get_log_file_path(), get_log_file_name(), allure.attachment_type.TEXT)


