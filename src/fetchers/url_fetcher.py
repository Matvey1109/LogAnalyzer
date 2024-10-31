from typing import Generator
from urllib.request import urlopen

from src.fetchers.fetcher import IFetcher
from src.log import Log
from src.log_parser import LogParser


class URLFetcher(IFetcher):
    """
    Class for file fetching from a URL
    """

    def __init__(self, source: str) -> None:
        """Initialize the URLFetcher with a source"""
        super().__init__(source)

    def fetch_logs(self) -> Generator[Log, None, None]:
        """Method to fetch logs from a source"""
        response = urlopen(self._source)
        for line_bytes in response:
            line: str = line_bytes.decode("utf-8")
            yield LogParser.parse_line(line)
