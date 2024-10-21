from parser import Parser
from typing import Generator
from urllib.request import urlopen

from fetchers.fetcher import Fetcher
from log import Log


class URLFetcher(Fetcher):
    """
    Class for file fetching from a URL
    """

    def __init__(self, source: str) -> None:
        """Initialize the URLFetcher with a source"""
        super().__init__(source)

    def fetch_logs(self) -> Generator[Log, None, None]:
        """Method to fetch logs from a source"""
        response = urlopen(self.source)
        for line_bytes in response:
            line: str = line_bytes.decode("utf-8")
            yield Parser.parse_line(line)
