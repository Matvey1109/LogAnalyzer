from src.fetchers.fetcher import IFetcher
from src.fetchers.local_fetcher import LocalFetcher
from src.fetchers.url_fetcher import URLFetcher


class FetcherFactory:
    """
    Factory class for creating fetchers based on the source type
    """

    @staticmethod
    def get_fetcher(source: str) -> IFetcher:
        if source.startswith("http"):
            return URLFetcher(source)
        else:
            return LocalFetcher(source)
