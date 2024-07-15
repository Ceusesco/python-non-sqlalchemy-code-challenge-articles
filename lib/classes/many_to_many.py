# class Article:
# #     def __init__(self, author, magazine, title):
#         self.author = author
#         self.magazine = magazine
#         self.title = title
        
# # class Author:
#     def __init__(self, name):
#         self.name = name

#     def articles(self):
#         pass

#     def magazines(self):
#         pass

#     def add_article(self, magazine, title):
#         pass

#     def topic_areas(self):
#         pass

# class Magazine:
#     def __init__(self, name, category):
#         self.name = name
#         self.category = category

#     def articles(self):
#         pass

#     def contributors(self):
#         pass

#     def article_titles(self):
#         pass

#     def contributing_authors(self):
#         pass
class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if not hasattr(self, '_title'):
            if isinstance(title, str) and 5 <= len(title) <= 50:
                self._title = title
            else:
                raise ValueError("Title must be a string between 5 and 50 characters.")
        else:
            raise AttributeError("Title cannot be changed once set.")

class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not hasattr(self, '_name'):
            if isinstance(name, str) and len(name) > 0:
                self._name = name
            else:
                raise ValueError("Name must be a non-empty string.")
        else:
            raise AttributeError("Name cannot be changed once set.")



    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list({magazine.category for magazine in self.magazines()}) or None
    
class Magazine:
    def __init__(self, name, category):
        self.name = name  # Use the setter to set the name
        self.category = category  # Use the setter to set the category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise ValueError("Name must be a string between 2 and 16 characters.")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError("Category must be a non-empty string.")

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        return [article.title for article in self.articles()] or None

    def contributing_authors(self):
        author_articles_count = {}
        for article in self.articles():
            if article.author in author_articles_count:
                author_articles_count[article.author] += 1
            else:
                author_articles_count[article.author] = 1
        return [author for author, count in author_articles_count.items() if count > 2] or None


