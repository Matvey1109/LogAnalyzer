import logging
import platform

from src.workflow import workflow

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    logger.info(platform.python_version())
    workflow()


if __name__ == "__main__":
    main()
