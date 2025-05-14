class Book:
    def __init__(self, title, author, genre, pages):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages
        self.__is_checked_out = False  # Encapsulated attribute

    def read(self):
        return f"You start reading '{self.title}' by {self.author}."

    def check_out(self):
        if not self.__is_checked_out:
            self.__is_checked_out = True
            return f"'{self.title}' has been checked out."
        else:
            return f"'{self.title}' is already checked out."

    def return_book(self):
        if self.__is_checked_out:
            self.__is_checked_out = False
            return f"'{self.title}' has been returned."
        else:
            return f"'{self.title}' was not checked out."

    def is_checked_out(self):
        return self.__is_checked_out
