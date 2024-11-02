from abc import ABC, abstractmethod

from src.stats.stats_data import StatsData


class IStatsWriter(ABC):
    """
    Abstract class for writing statistics data
    """

    def __init__(self, stats_data: StatsData, file_path: str) -> None:
        """Initialize the writer with a stats_data and file_path"""
        super().__init__()
        self._stats_data: StatsData = stats_data
        self._file_path: str = file_path + self.get_file_extension()

    @abstractmethod
    def write_stats_to_file(self) -> None:
        """Method to write stats_data in a file"""
        pass

    @abstractmethod
    def get_file_extension(self) -> str:
        """Method to get file extension"""
        pass
