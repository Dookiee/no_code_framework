import time

from test_reusables.service.logger_level import LogLevel
from utils.logger import log


class GeneralUtilities:
    @staticmethod
    def custom_sleep_time(sleep_time):
        """
        Generic Method to get the sleep time
        """
        log("Waiting for " + str(sleep_time) + " sec", LogLevel.INFO)
        time.sleep(sleep_time)
