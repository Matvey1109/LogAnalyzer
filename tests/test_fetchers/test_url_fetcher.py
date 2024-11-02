from typing import Generator

import pytest

from src.fetchers.url_fetcher import URLFetcher
from src.log import Log
from src.stats.stats_data import StatsData
from src.stats.stats_tracker import StatsTracker


class TestURLFetcher:
    @pytest.fixture
    def url_fetcher(self) -> URLFetcher:
        """Fixture to create a new URLFetcher instance for each test"""
        return URLFetcher(
            "https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs"
        )

    def test_get_correct_data_from_url(self, url_fetcher: URLFetcher):
        generator: Generator[Log, None, None] = url_fetcher.fetch_logs()
        stats = StatsTracker()
        stats.update_stats(generator)
        stats_data: StatsData = stats.get_stats_data()
        print(stats_data)
        assert stats_data.total_requests == 51462
        assert stats_data.most_frequent_requested_sources == [
            ("/downloads/product_1", 30285),
            ("/downloads/product_2", 21104),
            ("/downloads/product_3", 73),
        ]
        assert stats_data.most_frequent_occurring_status_codes == [
            ("404", 33876),
            ("304", 13330),
            ("200", 4028),
        ]
        assert stats_data.most_active_remote_addrs == [
            ("216.46.173.126", 2350),
            ("180.179.174.219", 1720),
            ("204.77.168.241", 1439),
        ]
        assert stats_data.avg_size_of_response == 659509.514398974
        assert stats_data.percentile_95th_of_response_size == 1768.0
