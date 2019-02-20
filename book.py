from datetime import datetime
import random

# Create a class called Book.
class Book:

# Your class should have two class variables: on_shelf and on_loan.
# Both should start as empty lists. on_shelf will contain the collection of book objects that are
# available to be lent out and on_loan will contain the collection of books that are currently being borrowed.

    on_shelf = []
    on_loan = []

# __init__
# This instance method makes a new book object. It should initialize a book's title, author, and isbn.
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

# create
# This class method is how new books are added to the library.
# This method should make a new book object with Book(...),add the new book object to on_shelf,
# and then return the new book.

    @classmethod
    def create(cls, title, author, isbn):
        new_book = Book(title, author, isbn)
        cls.on_shelf.append(new_book)
        return new_book

# browse
# This class method should return a random book from on_shelf (remember random.choice()?).

    @classmethod
    def browse(cls):
        book = random.choice(cls.on_shelf)
        return book

# lent_out
# This instance method should return true if a book has already been borrowed and false otherwise.

    def lent_out(self):
        return self in Book.on_loan

# current_due_date
# This class method returns the due date for books taken out today. We've written the body of this one for you:

    @classmethod
    def current_due_date(cls):
        now = datetime.now()
        two_weeks = 60 * 60 * 24 * 14 # two weeks expressed in seconds
        future_timestamp = now.timestamp() + two_weeks
        return datetime.fromtimestamp(future_timestamp)

# borrow
# This instance method is how a book is taken out of the library.
# This method should use lent_out to check if the book is already on loan,
# and if it is this method should return False to indicate that the attempt to borrow the book failed.
# Otherwise, use current_due_date to set the due_date of the book and move it from the collection of
# available books to the collection of books on loan, then return True.

    def borrow(self):
        if self.lent_out():
            return False
        else:
            self.due_date = Book.current_due_date()
            Book.on_shelf.remove(self)
            Book.on_loan.append(self)
            return True


# return_to_library
# This instance method is how a book gets returned to the library.
# It should call lent_out to verify that the book was actually on loan.
# If it wasn't on loan in the first place, return False.
# Otherwise, move the book from the collection of books on loan to the collection of books on the
# library shelves, and set the book's due date to None before returning True.

    def return_to_library(self):
        if not self.lent_out():
            return False
        else:
            Book.on_loan.remove(self)
            Book.on_shelf.append(self)
            self.due_date = None
            return True

# overdue
# This class method should return a list of books whose due dates are in the past (ie. less than Time.now).

    @classmethod
    def overdue(cls):
        in_the_past = []
        for num in range(0, len(Book.on_loan)):
            current_book = Book.on_loan[num]
            if current_book.due_date < datetime.now():
                in_the_past.append(current_book)
        return in_the_past


sister_outsider = Book.create("Sister Outsider", "Audre Lorde", "9781515905431")
aint_i = Book.create("Ain't I a Woman?", "Bell Hooks", "9780896081307")
if_they_come = Book.create("If They Come in the Morning", "Angela Y. Davis", "0893880221")
print(Book.browse().title) # "Sister Outsider" (this value may be different for you)
print(Book.browse().title)
print(len(Book.on_shelf)) # 3
print(len(Book.on_loan)) # 0
print(sister_outsider.lent_out()) # False
print(sister_outsider.borrow()) # True
print(sister_outsider.due_date) # 2017-02-25 20:52:20 -0500 (this value will be different for you)
print(len(Book.overdue())) # 0
print(len(Book.on_loan)) # 1
print(sister_outsider.return_to_library()) # True
print(sister_outsider.lent_out()) # False
print(len(Book.on_shelf)) # 3
print(len(Book.on_loan)) # 0
