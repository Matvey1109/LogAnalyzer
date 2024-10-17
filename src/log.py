from dataclasses import dataclass


@dataclass
class Log:
    """
    Dataclass representing a single log
    """

    remote_addr: str
    remote_user: str
    time_local: str
    request: str
    status: int
    body_bytes_sent: int
    http_referer: str
    http_user_agent: str
