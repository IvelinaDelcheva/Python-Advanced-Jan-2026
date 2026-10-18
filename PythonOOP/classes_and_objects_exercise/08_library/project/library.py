from project.user import User


class Library:
    def __init__(self):
        self.user_records: list[User] = []
        self.books_available: dict = {} # authors (key: str) and the books available
        self.rented_books: dict = {} # {usernames: {book names: days to return}}).

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str | None:
        available = self.books_available.get(author, None)
        if available:
            for book_av in available:
                if book_av == book_name:
                    user.books.append(book_name)
                    self.rented_books[user.username] = {book_name: days_to_return}
                    self.books_available[author].remove(book_name)
                    return f"{book_name} successfully rented for the next {days_to_return} days!"
        for username, book_day in self.rented_books.items():
            for book, day in book_day.items():
                if book == book_name:
                    return f'The book "{book}" is already rented and will be available in {day} days!'
        return None

    def return_book(self, author:str, book_name:str, user: User):
        if book_name in user.books:
            user.books.remove(book_name)
            self.books_available[author].append(book_name)
            self.rented_books[user.username].pop(book_name)
        return f"{user.username} doesn't have this book in his/her records!"








