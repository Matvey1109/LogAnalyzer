from glob import glob
from typing import Generator

from src.fetchers.fetcher import IFetcher
from src.log import Log
from src.parsers.log_parser import LogParser


class LocalFetcher(IFetcher):
    """
    Class for local file fetcher
    """

    def fetch_logs(self) -> Generator[Log, None, None]:
        """Method to fetch logs from a source"""
        for file_path in glob(self._source, recursive=True):
            with open(file_path, "r") as file:
                for line in file:
                    yield LogParser.parse_line(line)
