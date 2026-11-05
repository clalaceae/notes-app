import os
import sqlite3
from pathlib import Path


def get_db_path() -> Path:
    override = os.environ.get("NOTES_APP_DB_PATH")

    if override:
        return Path(override).expanduser()

    xdg_data_home = os.environ.get("XDG_DATA_HOME")

    if xdg_data_home and Path(xdg_data_home).is_absolute():
        data_home = Path(xdg_data_home)
    else:
        data_home = Path.home() / ".local" / "share"

    return data_home / "notes-app" / "notes.sqlite3"


def connect_db() -> sqlite3.Connection:
    path = get_db_path()

    # create parent dir if nonexistent
    path.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row

    # enable relationship checks on connection
    connection.execute("PRAGMA foreign_keys = ON")

    return connection