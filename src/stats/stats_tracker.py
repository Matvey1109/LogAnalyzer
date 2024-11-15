from collections import Counter
from typing import Generator

from src.constants import Constants
from src.log import Log
from src.stats.stats_data import StatsData


class StatsTracker:
    """
    A class to keep track of the stats of logs
    """

    def __init__(self):
        self._total_requests: int = 0
        self._total_response_size: int = 0
        self._response_sizes: list[int] = []
        self._request_sources: Counter = Counter()
        self._status_codes: Counter = Counter()
        self._remote_addrs: Counter = Counter()
        self._from_time: str | None = None
        self._to_time: str | None = None
        self._filter_field: str | None = None
        self._filter_value: str | None = None

    def update_stats(
        self,
        logs_generator: Generator[Log, None, None],
        from_time: str | None = None,
        to_time: str | None = None,
        filter_field: str | None = None,
        filter_value: str | None = None,
    ) -> None:
        """Update the statistics based on logs provided by the logs_generator within the specified time range"""
        for log in logs_generator:
            if self._does_log_fit_filter_criteria(
                log, from_time, to_time, filter_field, filter_value
            ):
                continue

            current_body_bytes_sent: int = int(log.body_bytes_sent)

            self._total_requests += 1
            self._total_response_size += int(current_body_bytes_sent)
            self._response_sizes.append(current_body_bytes_sent)
            self._request_sources[log.request_source] += 1
            self._status_codes[log.status] += 1
            self._remote_addrs[log.remote_addr] += 1
            self._from_time = from_time
            self._to_time = to_time
            self._filter_field = filter_field
            self._filter_value = filter_value

    def get_stats_data(self) -> StatsData:
        """Get the statistics data as a StatsData object"""
        most_frequent_sources: list[tuple[str, int]] = self._get_most_frequent_sources()
        most_frequent_status_codes: list[tuple[str, int]] = (
            self._get_most_frequent_status_codes()
        )
        avg_response_size: float = self._get_avg_response_size()
        percentile_95: float = self._get_percentile_95th_response_size()
        most_active_remote_addrs: list[tuple[str, int]] = (
            self._get_most_active_remote_addrs()
        )

        return StatsData(
            total_requests=self._total_requests,
            most_frequent_requested_sources=most_frequent_sources,
            most_frequent_occurring_status_codes=most_frequent_status_codes,
            avg_size_of_response=avg_response_size,
            percentile_95th_of_response_size=percentile_95,
            from_time=self._from_time,
            to_time=self._to_time,
            filter_field=self._filter_field,
            filter_value=self._filter_value,
            most_active_remote_addrs=most_active_remote_addrs,
        )

    def _calculate_percentile(self, data: list[int], percentile: float) -> float:
        """Calculate the percentile value from the given data"""
        if not data:
            return 0.0

        data.sort()
        index: float = (len(data) - 1) * percentile / 100

        if index.is_integer():
            return data[int(index)]

        lower: int = data[int(index)]
        upper: int = data[int(index) + 1]
        return lower + (upper - lower) * (index % 1)

    def _get_most_frequent_sources(
        self, limit: int = Constants.LIMIT_OF_FREQUENCY.value
    ) -> list[tuple[str, int]]:
        """Get the most frequent request sources"""
        return self._request_sources.most_common(limit)

    def _get_most_frequent_status_codes(
        self, limit: int = Constants.LIMIT_OF_FREQUENCY.value
    ) -> list[tuple[str, int]]:
        """Get the most frequent status codes"""
        return self._status_codes.most_common(limit)

    def _get_most_active_remote_addrs(
        self, limit: int = Constants.LIMIT_OF_FREQUENCY.value
    ) -> list[tuple[str, int]]:
        """Get the most active remote addresses"""
        return self._remote_addrs.most_common(limit)

    def _get_avg_response_size(self) -> float:
        """Get the average response size"""
        return (
            self._total_response_size / self._total_requests
            if self._total_requests > 0
            else 0.0
        )

    def _get_percentile_95th_response_size(self) -> float:
        """Get the 95th percentile of the response size"""
        return self._calculate_percentile(self._response_sizes, 95)

    def _does_log_fit_filter_criteria(
        self,
        log: Log,
        from_time: str | None = None,
        to_time: str | None = None,
        filter_field: str | None = None,
        filter_value: str | None = None,
    ) -> bool:
        """Filter logs by time range and by value"""
        if from_time and log.time_local < from_time:
            return True
        if to_time and log.time_local > to_time:
            return True

        if filter_field and filter_value:
            try:
                available_filter_fields = Log.__annotations__.keys()
                if filter_field not in available_filter_fields:
                    raise ValueError(
                        f"Filter field '{filter_field}' is not available in the log."
                    )

                log_value: str = getattr(log, filter_field)
            except AttributeError:
                return False

            if filter_value not in log_value:
                return True
        return False
