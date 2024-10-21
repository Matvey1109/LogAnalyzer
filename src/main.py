import logging
import platform

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    from fetchers.fetcher_factory import FetcherFactory
    from stats import Stats

    source = "https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs"
    # source = "src/test_logs/*.txt"
    fetcher = FetcherFactory.get_fetcher(source)
    gener = fetcher.fetch_logs()

    stats = Stats()
    stats.update_stats(gener)
    print(stats.get_stats())
    # logger.info(platform.python_version())


if __name__ == "__main__":
    main()
