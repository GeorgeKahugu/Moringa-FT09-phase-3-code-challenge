
from database.connection import get_db_connection

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

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
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._title = value
        else:
            raise ValueError("Title must be a non-empty string")

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._content = value
        else:
            raise ValueError("Content must be a non-empty string")

    @property
    def author_id(self):
        return self._author_id

    @author_id.setter
    def author_id(self, value):
        if isinstance(value, int):
            self._author_id = value
        else:
            raise ValueError("Author ID must be of type integer")

    @property
    def magazine_id(self):
        return self._magazine_id

    @magazine_id.setter
    def magazine_id(self, value):
        if isinstance(value, int):
            self._magazine_id = value
        else:
            raise ValueError("Magazine ID must be of type integer")

    def __repr__(self):
        return f'<Article {self.title}>'

    @classmethod
    def drop_table(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS articles')
        conn.commit()
        conn.close()

    @classmethod
    def create_table(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS articles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                author_id INTEGER NOT NULL,
                magazine_id INTEGER NOT NULL,
                FOREIGN KEY(author_id) REFERENCES authors(id),
                FOREIGN KEY(magazine_id) REFERENCES magazines(id)
            )
        ''')
        conn.commit()
        conn.close()

    @staticmethod
    def create(title, content, author_id, magazine_id):
        if not title or not content:
            raise ValueError("Title and content are required")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
                       (title, content, author_id, magazine_id))
        conn.commit()
        article_id = cursor.lastrowid
        conn.close()
        return Article(article_id, title, content, author_id, magazine_id)

    @classmethod
    def get_all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM articles')
        rows = cursor.fetchall()
        conn.close()
        return [Article(row[0], row[1], row[2], row[3], row[4]) for row in rows]

    @classmethod
    def get_by_id(cls, article_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM articles WHERE id = ?', (article_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Article(row[0], row[1], row[2], row[3], row[4])
        return None

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE articles SET title = ?, content = ?, author_id = ?, magazine_id = ? WHERE id = ?',
                       (self.title, self.content, self.author_id, self.magazine_id, self.id))
        conn.commit()
        conn.close()

    def delete(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM articles WHERE id = ?', (self.id,))
        conn.commit()
        conn.close()

    def get_summary(self, word_limit):
        words = self.content.split()[:word_limit]
        return ' '.join(words)
    

