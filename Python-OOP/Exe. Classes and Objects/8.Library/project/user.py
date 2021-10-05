from library import Library


class User:

    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = []

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"

    def get_book(self, authot: str, book_name: str, days_to_return: int, library: Library):
        for author, books in library.books_available.items():
            if book_name in books and author == authot:
                self.books.append(book_name)
                library.rented_books[self.username][author] = days_to_return
                library.books_available[author].pop(book_name)
                return f"{book_name} successfully rented for the next {days_to_return} days!"
        for username, info in library.rented_books.items():
            if book_name in info:
                return f"The book '{book_name}' is already rented and will be available in {info.value()} days!"

    def return_book(self, author: str, book_name: str, library: Library):
        if book_name in self.books:
            library.rented_books[self.username].pop(book_name)
            library.books_available[author].append(book_name)
            self.books.remove(book_name)
        else:
            return f"{self.username} doesn't have this book in his/her records!"

