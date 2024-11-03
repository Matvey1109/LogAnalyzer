import os

import pytest

from src.stats.stats_data import StatsData
from src.stats.stats_writers.adoc_stats_writer import AdocStatsWriter


class TestAdocStatsWriter:
    @pytest.fixture
    def adoc_stats_writer(self) -> AdocStatsWriter:
        """Fixture to create a new AdocStatsWriter instance for each test"""
        mock_stats_data: StatsData = StatsData(
            total_requests=22914,
            most_frequent_requested_sources=[
                ("/downloads/product_1", 13555),
                ("/downloads/product_2", 9324),
                ("/downloads/product_3", 35),
            ],
            most_frequent_occurring_status_codes=[
                ("404", 14994),
                ("304", 6011),
                ("200", 1816),
            ],
            avg_size_of_response=701027.0883739198,
            percentile_95th_of_response_size=1768.0,
            from_time="23/May/2015:00:00:00 ",
            to_time="31/May/2015:00:00:00 ",
            filter_field=None,
            filter_value=None,
            most_active_remote_addrs=[
                ("216.46.173.126", 1130),
                ("180.179.174.219", 736),
                ("65.39.197.164", 635),
            ],
        )

        return AdocStatsWriter(mock_stats_data, "tests/mock_output/data")

    def test_correct_output_in_file(self, adoc_stats_writer: AdocStatsWriter):
        adoc_stats_writer.write_stats_to_file()

        modified_file_path: str = adoc_stats_writer._file_path
        assert os.path.exists(modified_file_path)

        with open(modified_file_path, "r") as file:
            content = file.read()
            print(content)
            assert "22914" in content
            assert "Most Frequent Requested Sources" in content
            assert "Most Frequent Occurring Status Codes" in content
            assert "701027.0883739198" in content
            assert "Filtering" in content
            assert "23/May/2015:00:00:00" in content
