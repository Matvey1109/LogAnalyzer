from abc import ABC, abstractmethod
from typing import Generator

from log import Log


class Reader(ABC):
    """
    Abstract class for reading logs
    """

    def __init__(self, source: str) -> None:
        """Initialize the reader with a source"""
        super().__init__()
        self.source: str = source

    @abstractmethod
    def read_logs(self) -> Generator[Log, None, None]:
        """Method to read logs from a source"""
        pass
