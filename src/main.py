import logging
import platform

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)

# from src.time_parser import TimeParser
# from src.fetchers.fetcher_factory import FetcherFactory
# from src.stats import StatsTracker


def main() -> None:

    # source = "https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs"
    # source = "src/test_logs/*.txt"

    # from_time_iso = "2015-05-17T08:05:23+0000"
    # to_time_iso = "2015-05-17T08:05:24+0000"

    # time_parser = TimeParser()
    # from_time_log = time_parser.convert_iso_to_log_format(from_time_iso)
    # to_time_log = time_parser.convert_iso_to_log_format(to_time_iso)

    # fetcher = FetcherFactory.get_fetcher(source)
    # gener = fetcher.fetch_logs()

    # stats = StatsTracker()
    # stats.update_stats(gener, from_time=from_time_log, to_time=to_time_log)
    # print(stats.get_stats_data())
    logger.info(platform.python_version())


if __name__ == "__main__":
    main()
