from dataclasses import dataclass


@dataclass
class Log:
    """
    Dataclass representing a single log
    """

    remote_addr: str
    remote_user: str
    time_local: str
    request_method: str
    request_source: str
    status: str
    body_bytes_sent: str
    http_referer: str
    http_user_agent: str
