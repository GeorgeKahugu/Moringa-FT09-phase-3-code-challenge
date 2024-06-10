
from database.connection import get_db_connection


class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id
        self.get_db_connection = get_db_connection 

    def __repr__(self):
        return f'<Article {self.title}>'
    
   
    def update_content(self, new_content):
        """Update the content of the article."""
        self.content = new_content
    
    def get_summary(self, num_words=50):
        """Return a summary of the article."""
        words = self.content.split()
        summary = ' '.join(words[:num_words])
        if len(words) > num_words:
            summary += '...'
        return summary

    def get_author_id(self):
        """Return the author ID of the article."""
        return self.author_id
    
    def get_magazine_id(self):
        """Return the magazine ID of the article."""
        return self.magazine_id
    