from enum import Enum


class LogLevel(Enum):
    """
        Different logger level where you can control what should print
    """
    OFF = 1
    DEBUG = 2
    INFO = 3
    WARNING = 4
    ERROR = 5
