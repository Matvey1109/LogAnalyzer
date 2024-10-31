from datetime import datetime


class TimeParser:
    """
    A class to parse time from ISO format to log format
    """

    def __init__(
        self, iso_format="%Y-%m-%dT%H:%M:%S%z", log_format="%d/%b/%Y:%H:%M:%S %z"
    ):
        self.iso_format = iso_format
        self.log_format = log_format

    def convert_iso_to_log_format(self, iso_time):
        """Method to implement convertion"""
        return (
            "["
            + datetime.strptime(iso_time, self.iso_format).strftime(self.log_format)
            + "]"
        )
