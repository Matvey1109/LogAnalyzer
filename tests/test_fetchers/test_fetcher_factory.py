import pytest

from src.fetchers.fetcher import IFetcher
from src.fetchers.fetcher_factory import FetcherFactory
from src.fetchers.local_fetcher import LocalFetcher
from src.fetchers.url_fetcher import URLFetcher


@pytest.mark.parametrize(
    "mock_input, expected_output",
    [
        (
            "https:...",
            URLFetcher,
        ),
        (
            "tests/mock_input/*.txt",
            LocalFetcher,
        ),
    ],
)
def test_fetcher_factory(mock_input: str, expected_output):
    fetcher: IFetcher = FetcherFactory.get_fetcher(mock_input)
    assert isinstance(fetcher, expected_output)
