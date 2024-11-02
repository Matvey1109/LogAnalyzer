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

    assert parsed_log.remote_addr == expected_log.remote_addr
    assert parsed_log.remote_user == expected_log.remote_user
    assert parsed_log.time_local == expected_log.time_local
    assert parsed_log.request_method == expected_log.request_method
    assert parsed_log.request_source == expected_log.request_source
    assert parsed_log.status == expected_log.status
    assert parsed_log.body_bytes_sent == expected_log.body_bytes_sent
    assert parsed_log.http_referer == expected_log.http_referer
    assert parsed_log.http_user_agent == expected_log.http_user_agent
