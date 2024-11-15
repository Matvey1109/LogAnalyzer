from argparse import Namespace

from src.parsers.arg_parser import ArgParser, ProgramVars


def test_arg_parser(monkeypatch):
    test_args = Namespace(
        path="/test/path",
        from_time="2024-01-01T00:00:00",
        to_time="2024-01-02T00:00:00",
        format="markdown",
        filter_field="status",
        filter_value="200",
    )

    monkeypatch.setattr(
        "sys.argv",
        [
            "test_arg_parser.py",
            "--path",
            test_args.path,
            "--from-time",
            test_args.from_time,
            "--to-time",
            test_args.to_time,
            "--format",
            test_args.format,
            "--filter-field",
            test_args.filter_field,
            "--filter-value",
            test_args.filter_value,
        ],
    )

    arg_parser: ArgParser = ArgParser()
    program_vars: ProgramVars = arg_parser.get_program_vars()

    assert program_vars.path == test_args.path
    assert program_vars.from_time == test_args.from_time
    assert program_vars.to_time == test_args.to_time
    assert program_vars.format == test_args.format
    assert program_vars.filter_field == test_args.filter_field
    assert program_vars.filter_value == test_args.filter_value
