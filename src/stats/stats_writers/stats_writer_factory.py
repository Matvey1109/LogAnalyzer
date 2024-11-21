from enum import StrEnum, auto

from src.constants import FILE_NAME, STATS_FOLDER
from src.stats.stats_data import StatsData
from src.stats.stats_writers.adoc_stats_writer import AdocStatsWriter
from src.stats.stats_writers.markdown_stats_writer import MarkdownStatsWriter
from src.stats.stats_writers.stats_writer import IStatsWriter


class StatsWriterType(StrEnum):
    """
    Enum class for stats writer types
    """

    MarkdownStatsWriter = auto()
    AdocStatsWriter = auto()


class StatsWriterFactory:
    """
    Factory class for creating stats writers based on the user input
    """

    @staticmethod
    def get_stats_writer(
        stats_writer_type: StatsWriterType,
        stats_data: StatsData,
        folder_name: str = STATS_FOLDER,
        file_name: str = FILE_NAME,
    ) -> IStatsWriter:
        file_path: str = f"{folder_name}/{file_name}"

        match stats_writer_type:
            case StatsWriterType.MarkdownStatsWriter:
                stats_writer: IStatsWriter = MarkdownStatsWriter(stats_data, file_path)
            case StatsWriterType.AdocStatsWriter:
                stats_writer: IStatsWriter = AdocStatsWriter(stats_data, file_path)
            case _:
                raise ValueError

        return stats_writer
