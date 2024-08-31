class Book():
    available = True
    def __init__(self ,title, author, isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
    def __str__(self):
        a=""
        if self.available:
            a="available"
        else:
            a="not available"
        print(f"this is a book that is called {self.title}, it author is {self.author} and its isbn is {self.isbn}. this book is {a}")
    def borrow(self):
        if self.available:
            self.available = False
            print(f"you can borrow this book. have a good time!")
        else:
            print(f"the book {self.title} is not available!")
    def return_book(self): 
        if not self.available:
            self.available = True
            print(f"thanks for returning the book. have a good time!")
        else:
            print(f"the book {self.title} is in the library!!!!!")
class Member():
    borrowed_books = []
    def __init__(self, name, member_id):
        self.name=name
        self.member_id=member_id
    def __str__(self):
        print(f"his/her name is {self.name} and its id is : {self.member_id} he/she borrowed these books : {self.borrowed_books}")
class Library():
    pass
book1 = Book("1984", "جورج اورول", "1234567890")
book2 = Book("کشتن مرغ مقلد", "هارپر لی", "0987654321")
library = Library()
library.add_book(book1)
library.add_book(book2)
member = Member("آلیس", "M001")
library.register_member(member)
library.issue_book("M001", "1234567890")
library.return_book("M001", "1234567890")