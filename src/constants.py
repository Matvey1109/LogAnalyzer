from enum import Enum


class Constants(Enum):
    """
    A class to hold the program constants
    """

    STATS_FOLDER = "src/logs_data"
    FILE_NAME = "data"
    LIMIT_OF_FREQUENCY = 3
    LOG_FORMAT = "%d/%b/%Y:%H:%M:%S %z"
