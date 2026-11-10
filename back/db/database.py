import os
import sqlite3
from pathlib import Path

"""
Perform actions on database runtime. Migrate when ran as file.
"""

__SQL_DIR = Path(__file__).resolve().parent / "sql"

_MIGRATIONS = [
    __SQL_DIR / "01_initial.sql",
]

def _get_path() -> Path:
    """
    Get database filepath
    """
    override = os.environ.get("NOTES_APP_DB_PATH")

    if override:
        return Path(override).expanduser()

    xdg_data_home = os.environ.get("XDG_DATA_HOME")

    if xdg_data_home and Path(xdg_data_home).is_absolute():
        data_home = Path(xdg_data_home)
    else:
        data_home = Path.home() / ".local" / "share"

    return data_home / "notes-app" / "notes.sqlite3"

def _run_sql_file(conn: sqlite3.Connection, path: Path) -> None:
    """
    Run SQL file by executing statements individually
    """
    sql = path.read_text(encoding="utf-8")
    statement = ""

    for line in sql.splitlines(keepends=True):
        statement += line

        if sqlite3.complete_statement(statement):
            conn.execute(statement)
            statement = ""

    if statement.strip():
        raise ValueError(f"Incomplete SQL statement in {path}")

def connect() -> sqlite3.Connection:
    """
    Create Connection to database
    """
    path = _get_path()

    # create parent dir if nonexistent
    path.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row

    # enable relationship checks on connection
    conn.execute("PRAGMA foreign_keys = ON")

    return conn

def migrate() -> None:
    """
    Migrate database
    """
    conn = connect()

    try:
        # acquire write before ver check
        conn.execute("BEGIN IMMEDIATE")

        ver = conn.execute("PRAGMA user_version").fetchone()[0]

        if ver > len(_MIGRATIONS):
            raise RuntimeError("outdated migrations")

        for index in range(ver, len(_MIGRATIONS)):
            _run_sql_file(conn, _MIGRATIONS[index])

            # The value comes from our migration list, not user input.
            conn.execute(f"PRAGMA user_version = {index + 1}")

        conn.commit()

    except Exception:
        conn.rollback()
        raise

    finally:
        conn.close()

if __name__ == "__main__":
    migrate()
    print("Database migrations complete.")