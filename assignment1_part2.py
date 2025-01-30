# assignment1_part2.py

class Book:
    def __init__(self, author="", title=""):
        """
        Initializes the Book instance with an author and a title.

        :param author: The author of the book.
        :param title: The title of the book.
        """
        self.author = author
        self.title = title

    def display(self):
        """
        Prints a string representation of the book in the format:
        "title, written by author".
        """
        print(f"{self.title}, written by {self.author}")

# Instantiate the books
book1 = Book("J. K. Rowling", "Harry Potter and the Goblet of Fire")
book2 = Book("Walter Scott", "Ivanhoe: A Romance")

# Display the books
book1.display()
book2.display()
