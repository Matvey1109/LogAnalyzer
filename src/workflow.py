from typing import Generator

from src.fetchers.fetcher import IFetcher
from src.fetchers.fetcher_factory import FetcherFactory
from src.log import Log
from src.parsers.arg_parser import ArgParser, ProgramVars
from src.parsers.time_parser import TimeParser
from src.stats.stats_data import StatsData
from src.stats.stats_tracker import StatsTracker
from src.stats.stats_writers.stats_writer import IStatsWriter
from src.stats.stats_writers.stats_writer_factory import (StatsWriterFactory,
                                                          StatsWriterType)


def workflow():
    print("ANALYZER STARTED!")

    arg_parser: ArgParser = ArgParser()
    program_vars: ProgramVars = arg_parser.get_program_vars()

    time_parser: TimeParser = TimeParser()
    from_time_log: str | None = None
    to_time_log: str | None = None

    if program_vars.from_time:
        from_time_log: str = time_parser.convert_iso_to_log_format(
            program_vars.from_time
        )

    if program_vars.to_time:
        to_time_log: str = time_parser.convert_iso_to_log_format(program_vars.to_time)

    fetcher: IFetcher = FetcherFactory.get_fetcher(program_vars.path)
    logs_generator: Generator[Log, None, None] = fetcher.fetch_logs()

    stats_tracker: StatsTracker = StatsTracker()
    stats_tracker.update_stats(
        logs_generator,
        from_time=from_time_log,
        to_time=to_time_log,
        filter_field=program_vars.filter_field,
        filter_value=program_vars.filter_value,
    )

    stats_data: StatsData = stats_tracker.get_stats_data()

    writer_type: StatsWriterType = StatsWriterType(f"{program_vars.format}statswriter")
    stats_writer: IStatsWriter = StatsWriterFactory.get_stats_writer(
        writer_type, stats_data
    )
    stats_writer.write_stats_to_file()

    print("ANALYZER FINISHED!")
