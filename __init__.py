
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


new_magazine = Magazine.create ('Fastcars','MotorSports')
new_magazine2 = Magazine.create ('iWorld','Tech')
new_magazine3 = Magazine.create('Sports Review','Sport')

new_article = Article.create ('SportsCars', 'MotorSports',new_author,new_magazine )
new_article2 = Article.create('Gadgets', 'Tech', new_author3, new_magazine2)
new_article3 = Article.create ('Sports Review', 'Sport', new_author2, new_magazine3)

print('New Article Id:', new_article.id)
print('New Article Id:', new_article2.id)
print('New Article Title:', new_article2.title)

print('Article Author', new_article3.author().name)
print('Article Author', new_article.magazine().name)

