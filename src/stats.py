from typing import Generator
from collections import Counter


from log import Log


class Stats:
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
        for log in logs_generator:
            self.total_requests += 1
            self.total_response_size += log.body_bytes_sent
            self.response_sizes.append(log.body_bytes_sent)
            self.request_sources[log.http_referer] += 1
            self.status_codes[log.status] += 1

    def get_percentile(self, data: list[int], percentile: float) -> float:
        data.sort()
        index: float = (len(data) - 1) * percentile / 100

        if index.is_integer():
            return data[int(index)]

        lower: int = data[int(index)]
        upper: int = data[int(index) + 1]
        return lower + (upper - lower) * (index % 1)

    def get_stats(self) -> str:
        most_frequent_sources: list[tuple[str, int]] = self.request_sources.most_common(
            3
        )
        most_frequent_status_codes: list[tuple[str, int]] = (
            self.status_codes.most_common(3)
        )

        avg_response_size: float = (
            self.total_response_size / self.total_requests
            if self.total_requests > 0
            else 0
        )
        percentile_95: float = self.get_percentile(self.response_sizes, 95)

        stats_str: str = f"Total requests: {self.total_requests}\n"
        stats_str += "Most frequently requested sources:\n"
        for source, count in most_frequent_sources:
            stats_str += f"{source}: {count} requests\n"

        stats_str += "\nMost frequently occurring status codes:\n"
        for status_code, count in most_frequent_status_codes:
            stats_str += f"Status code {status_code}: {count} occurrences\n"

        stats_str += f"\nAverage size of response: {avg_response_size:.2f} bytes\n"
        stats_str += f"95th percentile of response size: {percentile_95:.2f} bytes\n"

        return stats_str
