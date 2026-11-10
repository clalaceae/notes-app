from sqlite3 import Connection
from uuid import uuid4, UUID
import datetime as dt

class I():
    """
    Base class for Notes, Tags
    """
    def __init__(self, conn: Connection):
        self.conn = conn

    @staticmethod
    def _new_id() -> UUID:
        return uuid4().hex

    @staticmethod
    def _now() -> str:
        ts = dt.datetime.now(dt.timezone.utc)
        ts = ts.replace(tzinfo=None).isoformat(timespec='milliseconds')
        return ts
