from typing import Generator

from log import Log


class Stats:
    """
    A class to keep track of the stats of logs
    """

    def __init__(self):
        self.total_requests: int = 0

    def update_stats(self, logs_generator: Generator[Log, None, None]):
        for log in logs_generator:
            self.total_requests += 1

    def get_stats(self) -> str:
        return f"Total requests: {self.total_requests}"
