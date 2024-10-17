from parser import Parser
from typing import Generator
from urllib.request import urlopen

from log import Log
from readers.reader import Reader


class URLReader(Reader):
    """
    Class for file reading from a URL
    """

    def __init__(self, source: str) -> None:
        """Initialize the URLReader with a source"""
        super().__init__(source)

    def read_logs(self) -> Generator[Log, None, None]:
        """Method to read logs from a source"""
        response = urlopen(self.source)
        for line_bytes in response:
            line: str = line_bytes.decode("utf-8")
            yield Parser.parse_line(line)
