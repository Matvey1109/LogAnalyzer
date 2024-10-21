from fetchers.local_fetcher import LocalFetcher
from fetchers.url_fetcher import URLFetcher
from fetchers.fetcher import Fetcher


class FetcherFactory:
    """
    Factory class for creating fetchers based on the source type
    """

    @staticmethod
    def get_fetcher(source: str) -> Fetcher:
        if source.startswith("http"):
            return URLFetcher(source)
        else:
            return LocalFetcher(source)
