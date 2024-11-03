import pytest

from src.stats.stats_data import StatsData
from src.stats.stats_writers.adoc_stats_writer import AdocStatsWriter
from src.stats.stats_writers.markdown_stats_writer import MarkdownStatsWriter
from src.stats.stats_writers.stats_writer import IStatsWriter
from src.stats.stats_writers.stats_writer_factory import (StatsWriterFactory,
                                                          StatsWriterType)


@pytest.mark.parametrize(
    "mock_input, expected_output",
    [
        (
            "markdownstatswriter",
            MarkdownStatsWriter,
        ),
        (
            "adocstatswriter",
            AdocStatsWriter,
        ),
    ],
)
def test_stats_writer_factory(mock_input: str, expected_output):
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

    stats_writer: IStatsWriter = StatsWriterFactory.get_stats_writer(
        StatsWriterType(mock_input), mock_stats_data
    )
    assert isinstance(stats_writer, expected_output)
