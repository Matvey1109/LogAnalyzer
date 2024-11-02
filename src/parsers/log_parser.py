from src.log import Log


class LogParser:
    """
    A class to parse log lines and create Log objects
    """

    @staticmethod
    def parse_line(line: str) -> Log:
        """Parse a log line and return a Log object"""
        parts = line.split()
        return Log(
            remote_addr=parts[0],
            remote_user=parts[2],
            time_local=(parts[3] + " " + parts[4]).strip("[]"),
            request_method=parts[5].strip('"'),
            request_source=parts[6],
            status=parts[8],
            body_bytes_sent=parts[9],
            http_referer=parts[10].strip('"'),
            http_user_agent=" ".join(parts[11:]).strip('"'),
        )
