from datetime import datetime


class TimeParser:
    """
    A class to parse time from ISO format to log format
    """

    def __init__(
        self,
        iso_format: str = "%Y-%m-%dT%H:%M:%S%z",
        log_format: str = "%d/%b/%Y:%H:%M:%S %z",
    ):
        self._iso_format: str = iso_format
        self._log_format: str = log_format

    def convert_iso_to_log_format(self, iso_time) -> str:
        """Method to implement convertion"""
        return (
            "["
            + datetime.strptime(iso_time, self._iso_format).strftime(self._log_format)
            + "]"
        )
