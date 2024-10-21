from abc import ABC, abstractmethod
from typing import Generator

from log import Log


class Fetcher(ABC):
    """
    Abstract class for fetching logs
    """

    def __init__(self, source: str) -> None:
        """Initialize the fetcher with a source"""
        super().__init__()
        self.source: str = source

    @abstractmethod
    def fetch_logs(self) -> Generator[Log, None, None]:
        """Method to fetch logs from a source"""
        pass
