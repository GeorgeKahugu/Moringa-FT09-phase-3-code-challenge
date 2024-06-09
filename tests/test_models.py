import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_article_creation(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        self.assertEqual(article.title, "Test Title")

    def test_magazine_creation(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")

#More tests added
    def test_article_update_content(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        article.update_content = "Update content in the article"
        self.assertEqual(article.content, "Update content in the article")

    
    
if __name__ == "__main__":
    unittest.main()
