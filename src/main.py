import logging
import platform

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    # from readers.reader_factory import ReaderFactory
    # from stats import Stats

    # source = "https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs"
    # reader = ReaderFactory.get_reader(source)
    # gener = reader.read_logs()

    # stats = Stats()
    # stats.update_stats(gener)
    # print(stats.get_stats())
    logger.info(platform.python_version())


if __name__ == "__main__":
    main()
