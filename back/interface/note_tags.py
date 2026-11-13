from base import I

class NoteTags(I):
    """
    Interface for performing SQL related to note-tag relationships
    """
    def insert(self, nid: str, tid: str):
        """
        Insert a new n-t relo
        """
        self.conn.execute("""
        --sql
            INSERT INTO note_tags (note_id, tag_id)
            VALUES (:ni, :ti)
        ;
        """, {
            'ni': nid,
            'ti': tid,
        })

        return

    def delete(self, nid: str, tid: str):
        """
        Delete an n-t relo
        """
        self.conn.execute("""
        --sql
            DELETE FROM note_tags
            WHERE note_id = :ni
            AND tag_id = :ti
        ;
        """, {
            'ni': nid,
            'ti': tid,
        })

    def list_tags_by_note(self, nid: str):
        """
        Get a list of tags connected to note
        TODO fetchmany()
        """
        rows = self.conn.execute("""
        --sql
            SELECT * FROM note_tags
            WHERE note_id = :ni
            ORDER BY tag_id ASC
        ;
        """, {
            'ni': nid,
        }).fetchall()

        return [dict(row) for row in rows]

    def list_notes_by_tag(self, tid: str):
        """
        Get a list of notes connected to tag
        TODO fetchmany()
        """

        rows = self.conn.execute("""
        --sql
            SELECT * FROM note_tags
            WHERE tag_id = :ti
            ORDER BY tag_id ASC
        ;
        """, {
            'ti': tid,
        }).fetchall()

        return [dict(row) for row in rows]
