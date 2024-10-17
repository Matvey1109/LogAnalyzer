from readers.local_reader import LocalReader
from readers.reader import Reader
from readers.url_reader import URLReader


class ReaderFactory:
    """
    Factory class for creating readers based on the source type
    """

    @staticmethod
    def get_reader(source: str) -> Reader:
        if source.startswith("http"):
            return URLReader(source)
        else:
            return LocalReader(source)
