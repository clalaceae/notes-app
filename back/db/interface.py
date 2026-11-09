from sqlite3 import Connection
from uuid import uuid4, UUID
import datetime as dt

class Interface():
    def __init__(self, conn: Connection):
        self.conn = conn

    @staticmethod
    def new_id() -> UUID:
        return uuid4().hex

    @staticmethod
    def now() -> str:
        ts = dt.datetime.now(dt.timezone.utc)
        ts = ts.replace(tzinfo=None).isoformat(timespec='milliseconds')
        return ts

class Notes(Interface):
    def insert(self, content: str, offset=None, timezone=None):
        """
        Insert a new note into the notes table
        """

        id = self.new_id()
        created_at = self.now()

        if bool(offset) != bool(timezone):
            raise ValueError("Offset and timezone must occur together")
        
        query = f"""
            --sql
            INSERT INTO notes (id, content, created_at, created_offset, created_timezone)
            VALUES (:id, :content, :created_at, :created_offset, :created_timezone)
            ;
        """

        self.conn.execute(query, {
            'id': id,
            'content': content,
            'created_at': created_at,
            'created_offset': offset,       # None becomes
            'created_timezone': timezone,   # SQL NULL
        })

    def get(self):
        """
        Get list of notes in table
        TODO maintain a connection with a single notes list open, call fetchmany on scroll
        """

        query = f"""
            --sql
            SELECT * FROM notes
            ORDER BY updated_at ASC, id ASC
            ;
        """
        rows = self.conn.execute(query).fetchall()

        return [dict(row) for row in rows]
