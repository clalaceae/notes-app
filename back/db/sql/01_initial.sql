-- notes --
-- id:          UUID
-- content:     Plaintext UTF-8
-- created/updated:
--   at:        UTC Time
--   offset:    UTC Offset
--   timezone:  Name
CREATE TABLE notes (
    id                  TEXT    PRIMARY KEY NOT NULL
,   content             TEXT    NOT NULL

,   created_at          TEXT    NOT NULL
,   created_offset      TEXT
,   created_timezone    TEXT

,   updated_at          TEXT
,   updated_offset      TEXT
,   updated_timezone    TEXT
);

-- tags --
-- id:          UUID
-- name:        UTF-8, format: "parent/child"
-- is_system:   1 for untitled/empty, 0 otherwise
CREATE TABLE tags (
    id          TEXT    PRIMARY KEY NOT NULL
,   name        TEXT    NOT NULL UNIQUE
,   is_system   INTEGER NOT NULL DEFAULT 0
        CHECK (is_system IN (0, 1))
);

-- note_tag --
-- note_id: UUID in notes
-- tag_id:  UUID in tags
CREATE TABLE note_tag (
    note_id TEXT    NOT NULL REFERENCES notes(id)   ON DELETE CASCADE
,   tag_id  TEXT    NOT NULL REFERENCES tags(id)    ON DELETE CASCADE
,   PRIMARY KEY (note_id, tag_id)
);

-- deleted_notes --
-- id: UUID previously in notes
CREATE TABLE deleted_notes (
    id TEXT PRIMARY KEY NOT NULL
);
