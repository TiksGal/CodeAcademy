from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Book:
    title: str
    author: str
    publication_year: int
    isbn: str

@dataclass
class Library:
    books: List[Optional[Book]]
    

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, book: Book) -> None:
        self.books.remove(book)

    def search_by_title(self, title: str) -> List[Book]:
        return [book for book in self.books if book.title == title]

    def search_by_author(self, author: str) -> List[Book]:
        return [book for book in self.books if book.author == author]

    def display_books(self) -> None:
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(f"{book.title} by {book.author}, {book.publication_year}, ISBN: {book.isbn}")


library = Library([])
book1 = Book("Good book", "No name", 2020, "123456")
book2 = Book("very good", "Cool", 2021, "012345")
book3 = Book("1984", "George Orwell", 1949, "012346")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.display_books()
matching_books = library.search_by_author("Cool")
for book in matching_books:
    print(f"Book found: {book.title} by {book.author}")
    
library.remove_book(book3)
library.display_books()

# output: Good book by No name, 2020, ISBN: 123456
# very good by Cool, 2021, ISBN: 012345
# 1984 by George Orwell, 1949, ISBN: 012346
# Book found: very good by Cool
# Good book by No name, 2020, ISBN: 123456
# very good by Cool, 2021, ISBN: 012345