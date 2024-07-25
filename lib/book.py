class Book:
    def __init__(self, title, author, pages, year_published):
        self.title = title
        self.author = author
        self.pages = pages
        self.year_published = year_published

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int) or value < 1:
            raise ValueError("Pages must be a positive integer")
        self._pages = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")