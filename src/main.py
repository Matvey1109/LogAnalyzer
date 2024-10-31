import logging
import platform

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)

# from src.stats.stats_tracker import StatsTracker
# from src.time_parser import TimeParser
# from src.fetchers.fetcher_factory import FetcherFactory
# from src.stats.stats_writers.markdown_writer import MarkdownWriter


def main() -> None:

    # # source = "https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs"
    # source = "src/mock/*.txt"

    # from_time_iso = "2024-10-31T12:00:00+0000"
    # to_time_iso = "2024-10-31T12:02:00+0000"

    # time_parser = TimeParser()
    # from_time_log = time_parser.convert_iso_to_log_format(from_time_iso)
    # to_time_log = time_parser.convert_iso_to_log_format(to_time_iso)

    # fetcher = FetcherFactory.get_fetcher(source)
    # gener = fetcher.fetch_logs()

    # stats = StatsTracker()
    # stats.update_stats(gener, from_time=from_time_log, to_time=to_time_log)
    # stats_data = stats.get_stats_data()
    # md_wr = MarkdownWriter(stats_data, "src/stats.md")
    # md_wr.write_stats_to_file()
    # print(stats.get_stats_data())
    logger.info(platform.python_version())


if __name__ == "__main__":
    main()
