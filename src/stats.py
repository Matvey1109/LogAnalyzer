from collections import Counter
from typing import Generator

from log import Log
from dataclasses import dataclass


@dataclass
class StatsData:
    total_requests: int
    most_frequent_requested_sources: list[tuple[str, int]]
    most_frequent_occurring_status_codes: list[tuple[str, int]]
    avg_size_of_response: float
    percentile_95th_of_response_size: float


class StatsTracker:
    """
    A class to keep track of the stats of logs
    """

    def __init__(self):
        self.total_requests: int = 0
        self.total_response_size: int = 0
        self.response_sizes: list[int] = []
        self.request_sources: Counter = Counter()
        self.status_codes: Counter = Counter()

    def update_stats(self, logs_generator: Generator[Log, None, None]):
        """Update the statistics based on logs provided by the logs_generator"""
        for log in logs_generator:
            self.total_requests += 1
            self.total_response_size += log.body_bytes_sent
            self.response_sizes.append(log.body_bytes_sent)
            self.request_sources[log.request_source] += 1
            self.status_codes[log.status] += 1

    def calculate_percentile(self, data: list[int], percentile: float) -> float:
        """Calculate the percentile value from the given data"""
        data.sort()
        index: float = (len(data) - 1) * percentile / 100

        if index.is_integer():
            return data[int(index)]

        lower: int = data[int(index)]
        upper: int = data[int(index) + 1]
        return lower + (upper - lower) * (index % 1)

    def get_most_frequent_sources(self, limit: int = 3) -> list[tuple[str, int]]:
        """Get the most frequent request sources"""
        return self.request_sources.most_common(limit)

    def get_most_frequent_status_codes(self, limit: int = 3) -> list[tuple[str, int]]:
        """Get the most frequent status codes"""
        return self.status_codes.most_common(limit)

    def get_avg_response_size(self) -> float:
        """Get the average response size"""
        return (
            self.total_response_size / self.total_requests
            if self.total_requests > 0
            else 0.0
        )

    def get_percentile_95th_response_size(self) -> float:
        """Get the 95th percentile of the response size"""
        return self.calculate_percentile(self.response_sizes, 95)

    def get_stats_data(self) -> StatsData:
        """Get the statistics data as a StatsData object"""
        most_frequent_sources = self.get_most_frequent_sources()
        most_frequent_status_codes = self.get_most_frequent_status_codes()
        avg_response_size = self.get_avg_response_size()
        percentile_95 = self.get_percentile_95th_response_size()

        return StatsData(
            total_requests=self.total_requests,
            most_frequent_requested_sources=most_frequent_sources,
            most_frequent_occurring_status_codes=most_frequent_status_codes,
            avg_size_of_response=avg_response_size,
            percentile_95th_of_response_size=percentile_95,
        )
