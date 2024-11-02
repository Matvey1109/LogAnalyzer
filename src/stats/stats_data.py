from dataclasses import dataclass


@dataclass
class StatsData:
    """
    Dataclass representing a data fo stats
    """

    total_requests: int
    most_frequent_requested_sources: list[tuple[str, int]]
    most_frequent_occurring_status_codes: list[tuple[str, int]]
    avg_size_of_response: float
    percentile_95th_of_response_size: float
    from_time: str | None
    to_time: str | None
    filter_value: str | None
    most_active_remote_addrs: list[tuple[str, int]]  # Additional stats
