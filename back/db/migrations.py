import sqlite3
from pathlib import Path

from db.init import connect_db


SQL_DIR = Path(__file__).resolve().parent / "sql"

MIGRATIONS = [
    SQL_DIR / "01_initial.sql",
]


def run_sql_file(connection: sqlite3.Connection, path: Path) -> None:
    sql = path.read_text(encoding="utf-8")
    statement = ""

    for line in sql.splitlines(keepends=True):
        statement += line

        if sqlite3.complete_statement(statement):
            connection.execute(statement)
            statement = ""

    if statement.strip():
        raise ValueError(f"Incomplete SQL statement in {path}")

def migrate_db() -> None:
    conn = connect_db()

    try:
        # acquire write before ver check
        conn.execute("BEGIN IMMEDIATE")

        ver = conn.execute(
            "PRAGMA user_version"
        ).fetchone()[0]

        if ver > len(MIGRATIONS):
            raise RuntimeError(
                "outdated migrations"
            )

        for index in range(ver, len(MIGRATIONS)):
            for statement in MIGRATIONS[index]:
                conn.execute(statement)

            # The value comes from our migration list, not user input.
            conn.execute(f"PRAGMA user_version = {index + 1}")

        conn.commit()

    except Exception:
        conn.rollback()
        raise

    finally:
        conn.close()


if __name__ == "__main__":
    migrate_db()
    print("Database migrations complete.")