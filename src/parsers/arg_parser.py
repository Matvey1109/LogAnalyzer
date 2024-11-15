import argparse
from dataclasses import dataclass
from enum import Enum


class CLIArgs(Enum):
    """
    A class to hold the command line arguments
    """

    PATH = "--path"
    FROM_TIME = "--from-time"
    TO_TIME = "--to-time"
    FORMAT = "--format"
    FILTER_FIELD = "--filter-field"
    FILTER_VALUE = "--filter-value"


@dataclass
class ProgramVars:
    """
    A class to hold the program variables
    """

    path: str
    from_time: str | None = None
    to_time: str | None = None
    format: str | None = None
    filter_field: str | None = None
    filter_value: str | None = None


class ArgParser:
    """
    A class to parse arguments from the command line
    """

    def __init__(self) -> None:
        parser: argparse.ArgumentParser = argparse.ArgumentParser()

        parser.add_argument(
            CLIArgs.PATH.value,
            type=str,
            help="Path to logs (url or local)",
            required=True,
        )

        parser.add_argument(
            CLIArgs.FROM_TIME.value,
            type=str,
            help="Start time (iso)",
            required=False,
            default=None,
        )

        parser.add_argument(
            CLIArgs.TO_TIME.value,
            type=str,
            help="End time (iso)",
            required=False,
            default=None,
        )

        parser.add_argument(
            CLIArgs.FORMAT.value,
            type=str,
            help="Output format",
            required=False,
            default=None,
        )

        parser.add_argument(
            CLIArgs.FILTER_FIELD.value,
            type=str,
            help="Filter logs by value in field",
            required=False,
            default=None,
        )

        parser.add_argument(
            CLIArgs.FILTER_VALUE.value,
            type=str,
            help="Filter logs by value in field",
            required=False,
            default=None,
        )

        self._args: argparse.Namespace = parser.parse_args()

    def get_program_vars(self) -> ProgramVars:
        """
        Returns the program variables
        """

        if self._args.format is None:
            self._args.format = "markdown"

        return ProgramVars(
            path=self._args.path,
            from_time=self._args.from_time,
            to_time=self._args.to_time,
            format=self._args.format,
            filter_field=self._args.filter_field,
            filter_value=self._args.filter_value,
        )
