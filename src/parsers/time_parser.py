from datetime import datetime

from src.constants import LOG_FORMAT


class TimeParser:
    """
    A class to parse time from ISO format to log format
    """

    def __init__(
        self,
        log_format: str = LOG_FORMAT,
    ) -> None:
        self._log_format: str = log_format

    def convert_iso_to_log_format(self, iso_time: str) -> str:
        """Method to implement conversion"""
        return datetime.fromisoformat(iso_time).strftime(self._log_format)
