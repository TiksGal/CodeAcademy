import logging

logging.basicConfig(filename="book.log", level=logging.ERROR)

class Book:
    def __init__(self, title = None, author = None):
        if title is None:
            logging.error("Title attribute is missing.")
            raise ValueError("Title attribute is missing.")
        if author is None:
            logging.error("Author attribute is missing.")
            raise ValueError("Author attribute is missing.")
        self.title = title
        self.author = author
    
    def get_title(self):
        return f"Title: {self.title}"
    
    def get_author(self):
        return f"Author: {self.author}"

# Instantiate the Book class with 3 new books
try:
    PP = Book("Pride and Prejudice", "Jane Austen")
    H = Book("Hamlet", "William Shakespeare")
    WP = Book("War and Peace", "Leo Tolstoy")
    # This will raise a ValueError and log an error message
    # x = Book(author="J.K. Rowling")
except ValueError as e:
    logging.error(str(e))

print(PP.title)
print(PP.author)
print(PP.get_title())
print(PP.get_author())