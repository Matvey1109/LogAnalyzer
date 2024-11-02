from typing import Generator

import pytest

from src.fetchers.local_fetcher import LocalFetcher
from src.log import Log
from src.parsers.time_parser import TimeParser
from src.stats.stats_data import StatsData
from src.stats.stats_tracker import StatsTracker


class TestStatsTracker:
    @pytest.fixture
    def stats_tracker(self) -> StatsTracker:
        """Fixture to create a new StatsTracker instance for each test"""
        return StatsTracker()

    def test_get_correct_stats_data(self, stats_tracker: StatsTracker):
        fetcher: LocalFetcher = LocalFetcher("tests/mock/*.txt")
        logs_generator: Generator[Log, None, None] = fetcher.fetch_logs()
        stats_tracker.update_stats(logs_generator)
        stats_data: StatsData = stats_tracker.get_stats_data()
        print(stats_data)
        assert stats_data.total_requests == 51466
        assert stats_data.most_frequent_requested_sources == [
            ("/downloads/product_1", 30285),
            ("/downloads/product_2", 21104),
            ("/downloads/product_3", 73),
        ]
        assert stats_data.most_frequent_occurring_status_codes == [
            (404, 33877),
            (304, 13330),
            (200, 4030),
        ]
        assert stats_data.avg_size_of_response == 659458.3908211247
        assert stats_data.percentile_95th_of_response_size == 1768.0

    @pytest.mark.parametrize(
        "mock_input_from_time, mock_input_to_time, expected_output",
        [
            (
                "2015-05-17T00:00:00+0000",
                "2015-05-31T00:00:00+0000",
                39177,
            ),
            (
                "2015-05-20",
                "2015-05-31",
                31525,
            ),
            (
                "20150523",
                "20150531",
                22914,
            ),
        ],
    )
    def test_filtering_by_time(
        self,
        mock_input_from_time: str,
        mock_input_to_time: str,
        expected_output: int,
        stats_tracker: StatsTracker,
    ):
        fetcher: LocalFetcher = LocalFetcher("tests/mock/*.txt")
        logs_generator: Generator[Log, None, None] = fetcher.fetch_logs()

        time_parser: TimeParser = TimeParser()
        from_time_log: str = time_parser.convert_iso_to_log_format(mock_input_from_time)
        to_time_log: str = time_parser.convert_iso_to_log_format(mock_input_to_time)

        stats_tracker.update_stats(
            logs_generator, from_time=from_time_log, to_time=to_time_log
        )
        stats_data: StatsData = stats_tracker.get_stats_data()
        assert stats_data.total_requests == expected_output
