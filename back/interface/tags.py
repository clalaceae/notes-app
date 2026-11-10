from base import I

class Tags(I):
    """
    Interface for performing SQL related to tags
    """
    def insert(self, name: str, pid: str = None):
        """
        Insert a new tag into table
        """
        id = self._new_id()

        self.conn.execute(f"""
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
        idk why i would need this actually, same for notes.get
        """

    def update(self, id: str, name:str, pid: str):
        """
        Update a tag
        """
        self.conn.execute(f"""
        --sql
            UPDATE tags
            SET name = COALESCE(:na, name)
            ,   pid = COALESCE(:pd, pid)
        ;
        """, {
            'na': name,
            'pd': pid,
        })


    def delete(self, id: str):
        """
        Delete a tag from table
        """
        self.conn.execute(f"""
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
        Get list of tags in table
        TODO fetch amount or select depending on implementation (TBD)
        """
        rows = self.conn.execute(f"""
        --sql
            SELECT * FROM tags
            ORDER BY name ASC, id ASC
        ;
        """).fetchall()

        return [dict(row) for row in rows]
