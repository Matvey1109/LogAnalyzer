from typing import Generator

import pytest

from src.fetchers.local_fetcher import LocalFetcher
from src.log import Log
from src.stats.stats_data import StatsData
from src.stats.stats_tracker import StatsTracker


class TestLocalFetcher:
    @pytest.fixture
    def local_fetcher(self) -> LocalFetcher:
        """Fixture to create a new LocalFetcher instance for each test"""
        return LocalFetcher("tests/mock/*.txt")

    def test_get_correct_data_from_local(self, local_fetcher: LocalFetcher):
        generator: Generator[Log, None, None] = local_fetcher.fetch_logs()
        stats = StatsTracker()
        stats.update_stats(generator)
        stats_data: StatsData = stats.get_stats_data()
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
