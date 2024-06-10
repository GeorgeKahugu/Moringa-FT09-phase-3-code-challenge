   
from database.connection import get_db_connection

class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        if isinstance(value, int):
            self._id = value
        else:
            raise ValueError("ID must be of type integer")
        
    @property
    def name(self):
        return self._name 

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")

    def __repr__(self):
        return f'<Author {self.name}>'

    @classmethod
    def drop_table(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS authors')
        conn.commit()
        conn.close()

    @classmethod
    def create_table(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS authors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    @staticmethod
    def create(name):
        if not name:
            raise ValueError("Name is required")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (name,))
        conn.commit()
        author_id = cursor.lastrowid
        conn.close()
        return Author(author_id, name)
    
    @classmethod
    def get_all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM authors')
        rows = cursor.fetchall()
        conn.close()
        return [Author(row[0], row[1]) for row in rows]
    
    @classmethod
    def get_by_id(cls, author_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM authors WHERE id = ?', (author_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Author(row[0], row[1])
        return None
    
    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE authors SET name = ? WHERE id = ?', (self.name, self.id))
        conn.commit()
        conn.close()
    
    def delete(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM authors WHERE id = ?', (self.id,))
        conn.commit()
        conn.close()
