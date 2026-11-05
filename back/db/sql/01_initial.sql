CREATE TABLE notes (
    id TEXT PRIMARY KEY NOT NULL,
    content TEXT NOT NULL,
    is_empty INTEGER NOT NULL CHECK (is_empty IN (0, 1)),
    is_untitled INTEGER NOT NULL CHECK (is_untitled IN (0, 1)),
    created_at TEXT NOT NULL,
    created_timezone TEXT,
    updated_at TEXT NOT NULL,
    updated_timezone TEXT
);

CREATE TABLE tags (
    id TEXT PRIMARY KEY NOT NULL,
    name TEXT NOT NULL UNIQUE,
    is_system INTEGER NOT NULL DEFAULT 0 CHECK (is_system IN (0, 1))
);

CREATE TABLE note_tags (
    note_id TEXT NOT NULL REFERENCES notes(id) ON DELETE CASCADE,
    tag_id TEXT NOT NULL REFERENCES tags(id) ON DELETE CASCADE,
    PRIMARY KEY (note_id, tag_id)
);

CREATE TABLE note_tombstones (
    id TEXT PRIMARY KEY NOT NULL
);