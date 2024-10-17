from parser import Parser
from typing import Generator

from log import Log
from readers.reader import Reader


class LocalReader(Reader):
    """
    Class for local file reading
    """

    def __init__(self, source: str) -> None:
        """Initialize the LocalReader with a source"""
        super().__init__(source)

    def read_logs(self) -> Generator[Log, None, None]:
        """Method to read logs from a source"""
        with open(self.source, "r") as file:
            for line in file:
                yield Parser.parse_line(line)
