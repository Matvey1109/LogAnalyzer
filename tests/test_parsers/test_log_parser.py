from src.log import Log
from src.parsers.log_parser import LogParser


def test_parse_log_line():
    log_line = '192.168.1.1 - john [10/Oct/2024:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 1234 "http://example.com" "Mozilla/5.0"'
    expected_log = Log(
        remote_addr="192.168.1.1",
        remote_user="john",
        time_local="10/Oct/2024:13:55:36 +0000",
        request_method="GET",
        request_source="/index.html",
        status="200",
        body_bytes_sent="1234",
        http_referer="http://example.com",
        http_user_agent="Mozilla/5.0",
    )

    parsed_log = LogParser.parse_line(log_line)
    assert parsed_log == expected_log
