from parser import Parser
from typing import Generator
from glob import glob

from log import Log
from fetchers.fetcher import Fetcher


class LocalFetcher(Fetcher):
    """
    Class for local file fetcher
    """

    def __init__(self, source: str) -> None:
        """Initialize the LocalFetcher with a source"""
        super().__init__(source)

    def fetch_logs(self) -> Generator[Log, None, None]:
        """Method to fetch logs from a source"""
        for file_path in glob(self.source, recursive=True):
            with open(file_path, "r") as file:
                for line in file:
                    yield Parser.parse_line(line)
