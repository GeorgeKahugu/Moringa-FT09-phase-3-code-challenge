from models import magazine
from models.article import Article
from models.author import Author
from models.magazine import Magazine

Author.drop_table()
Author.create_table()

Magazine.drop_table()
Magazine.create_table()

Article.drop_table()
Article.create_table()

new_author = Author.create("John Doe")
print("Author ID:", new_author.id)
print("Author Name:", new_author.name)

new_author2 = Author.create("Jane Smith")
print("Author ID:", new_author2.id)
print("Author Name:", new_author2.name)

new_author3 = Author.create('George Kahugu')
print("Author ID:", new_author3.id )
print("Author Name:", new_author3.name)

# new_article = Article.create('Speed', 'Cars')
# print("Article Title:", new_article.title)
# print("Article Category:", new_article.category)

# new_article2 = Article.create('Gadgets', 'Technology')
# print("Article Title:", new_article2.title)
# print("Article Category:", new_article2.category)

# new_article3 = Article.create('Football', 'Sports')
# print("Article Title:", new_article3.title)
# print("Article Category:", new_article3.category)


magazine = Magazine. create('Fastcars', 'Motorsport')
magazine2 = Magazine.create('iWorld', 'Tech')
magazine3 = Magazine.create('Sports Review', 'Sports')

