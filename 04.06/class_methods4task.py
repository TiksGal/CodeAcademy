# Create a class to represent a library system. 
# The library system should have a collection of books that can be borrowed by users. 
# Users can register to the library system, borrow books, and return books. 
# The library system should keep track of the books borrowed by users, and the number of available copies of each book.

from typing import List


class Book:
    def __init__(self, title: str, author: str, isbn: str, num_copies: int) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self.num_copies = num_copies


class User:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        self.books_borrowed: List[Book] = []


class LibrarySystem:
    books: List[Book] = []
    users: List[User] = []

    @classmethod
    def add_book(cls, book: Book) -> None:
        cls.books.append(book)

    @classmethod
    def register_user(cls, user: User) -> None:
        cls.users.append(user)

    @classmethod
    def borrow_book(cls, user: User, isbn: str) -> None:
        for book in cls.books:
            if book.isbn == isbn:
                if book.num_copies > 0:
                    book.num_copies -= 1
                    user.books_borrowed.append(book)
                    print(f"{user.name} has borrowed {book.title}.")
                    return
                else:
                    print("Sorry, no copies of this book are available.")
                    return
        print("Sorry, the book with the given ISBN is not available in the library system.")

    @classmethod
    def return_book(cls, user: User, isbn: str) -> None:
        for book in user.books_borrowed:
            if book.isbn == isbn:
                book.num_copies += 1
                user.books_borrowed.remove(book)
                print(f"{user.name} has returned {book.title}.")
                return
        print("Sorry, the user has not borrowed the book with the given ISBN.")

    @classmethod
    def list_books(cls) -> List[Book]:
        return cls.books

    @classmethod
    def list_users(cls) -> List[User]:
        return cls.users


book1 = Book("The Hobbit", "J.R.R. Tolkien", "1234", 5)
book2 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "5678", 3)
LibrarySystem.add_book(book1)
LibrarySystem.add_book(book2)

user1 = User("John Doe", "johndoe@example.com")
user2 = User("Jane Doe", "janedoe@example.com")
LibrarySystem.register_user(user1)
LibrarySystem.register_user(user2)

LibrarySystem.borrow_book(user1, "1234")
LibrarySystem.borrow_book(user2, "5678")
LibrarySystem.borrow_book(user1, "5678")
LibrarySystem.borrow_book(user1, "9012")

LibrarySystem.return_book(user1, "1234")
LibrarySystem.return_book(user1, "5678")
LibrarySystem.return_book(user2, "5678")

books = LibrarySystem.list_books()
for book in books:
    print(f"{book.title} by {book.author}, ISBN: {book.isbn}, Copies available: {book.num_copies}")

users = LibrarySystem.list_users()
for user in users:
    print(f"{user.name} ({user.email}) has borrowed:")
    for book in user.books_borrowed:
        print(f"- {book.title} by {book.author}, ISBN: {book.isbn}")
