from base import I, _ostr


class Notes(I):
    """
    Interface for performing SQL related to notes
    """
    def insert(self, content: str, offset: _ostr = None, timezone: str = None):
        """
        Insert a new note
        """
        id = self._new_id()
        c_at = self._now()

        if bool(offset) != bool(timezone):
            raise ValueError("Offset and timezone must occur together")
        
        self.conn.execute("""
        --sql
            INSERT INTO notes (id, content, c_at, c_offset, c_timezone)
            VALUES (:id, :cn, :ca, :co, :ct)
        ;
        """, {
            'id': id,
            'cn': content,
            'ca': c_at,
            'co': offset,   # None becomes
            'ct': timezone, # SQL NULL
        })

        return

    def get(self, id: str):
        """
        Get a note
        """
        row = self.conn.execute("""
        --sql
            SELECT * from notes
            WHERE id = :id
        ;
        """, {
            'id': id,
        })

        return row

    def update(self, id: str, content: str, offset: _ostr = None, timezone: _ostr = None):
        """
        Update a note
        """
        u_at = self._now()

        if bool(offset) != bool(timezone):
            raise ValueError("Offset and timezone must occur together")
        
        self.conn.execute("""
        --sql
            UPDATE notes
            SET content = :cn
            ,   u_at = :ua
            ,   u_offset = :uo
            ,   u_timezone = :ut
            WHERE id = :id
        ;
        """, {
            'cn': content,
            'ua': u_at,
            'uo': offset,       # None becomes
            'ut': timezone,   # SQL NULL
            'id': id,
        })

        return

    def delete(self, id: str):
        """
        Delete a note
        """
        self.conn.execute("""
        --sql
            DELETE FROM notes
            WHERE id = :id
        ;
        """, {
            'id': id,
        })

        return

    def list(self):
        """
        Get list of notes
        TODO maintain a connection with a single notes list open, call fetchmany on scroll
        """
        rows = self.conn.execute("""
        --sql
            SELECT * FROM notes
            ORDER BY c_at ASC, id ASC
        ;
        """).fetchall()

        return [dict(row) for row in rows]
