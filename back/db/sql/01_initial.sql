-- notes --
-- id:          UUID
-- content:     Plaintext UTF-8
-- created/updated:
--   at:        UTC Time
--   offset:    UTC Offset
--   timezone:  Name
CREATE TABLE notes (
    id            TEXT    PRIMARY KEY NOT NULL
,   content       TEXT    NOT NULL

,   c_at          TEXT    NOT NULL
,   c_offset      TEXT
,   c_timezone    TEXT

,   u_at          TEXT
,   u_offset      TEXT
,   u_timezone    TEXT
);

-- tags --
-- id:          UUID
-- name:        UTF-8, format: "parent/child"
-- pid:         UUID of parent tag | NULL
-- is_system:   1 for untitled/empty, 0 otherwise
-- deleting parent tag deletes child tag.
CREATE TABLE tags (
    id          TEXT    PRIMARY KEY NOT NULL
,   name        TEXT    NOT NULL
,   pid         TEXT    REFERENCES tags(id) ON DELETE CASCADE
,   is_system   INTEGER NOT NULL DEFAULT 0
        CHECK (is_system IN (0, 1))
,   UNIQUE (name, parent_id)
);

-- note_tag --
-- note_id: UUID in notes
-- tag_id:  UUID in tags
-- combined primary key
CREATE TABLE note_tags (
    note_id TEXT    NOT NULL    REFERENCES notes(id) ON DELETE CASCADE
,   tag_id  TEXT    NOT NULL    REFERENCES tags(id) ON DELETE CASCADE
,   PRIMARY KEY (note_id, tag_id)
);

-- deleted_notes --
-- id: UUID previously in notes
CREATE TABLE deleted_notes (
    id TEXT PRIMARY KEY NOT NULL
);

-- System Tags
INSERT INTO tags VALUES
    ('untitled', 'untitled', 1)
,   ('empty', 'empty', 1)
;
