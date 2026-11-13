from base import I, _ostr

class Tags(I):
    """
    Interface for performing SQL related to tags
    """
    def insert(self, name: str, pid: _ostr = None):
        """
        Insert a new tag
        """
        id = self._new_id()

        self.conn.execute("""
        --sql
            INSERT INTO tags (id, name, pid)
            VALUES (:id, :na, :pi)
        ;
        """, {
            'id': id,
            'na': name,
            'pi': pid,
        })

        return;

    def get(self, id: str):
        """
        Get a tag
        """
        row = self.conn.execute("""
        --sql
            SELECT * from tags
            WHERE id = :id
        ;
        """, {
            'id': id,
        })

        return row


    def update(self, id: str, name: _ostr = None, pid: _ostr = None):
        """
        Update a tag
        """
        self.conn.execute("""
        --sql
            UPDATE tags
            SET name = COALESCE(:na, name)
            ,   pid = COALESCE(:pd, pid)
            WHERE id = :id
        ;
        """, {
            'na': name,
            'pd': pid,
            'id': id
        })


    def delete(self, id: str):
        """
        Delete a tag
        """
        self.conn.execute("""
        --sql
            DELETE FROM tags
            WHERE id = :id
        ;
        """, {
            'id': id,
        })

        return

    def list(self):
        """
        Get list of tags
        TODO fetch amount or select depending on implementation (TBD)
        """
        rows = self.conn.execute("""
        --sql
            SELECT * FROM tags
            ORDER BY name ASC, id ASC
        ;
        """).fetchall()

        return [dict(row) for row in rows]
