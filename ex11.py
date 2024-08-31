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
        return
    def borrow(self,mem):
        if self.available:
            self.available = False
            print(f"{mem.name} with id of {mem.member_id}, you can borrow the book {self.title}. have a good time!")
        else:
            print(f"{mem.name} with id of {mem.member_id}, the book {self.title} is not available!")
        return
    def return_book(self,mem): 
        if not self.available:
            self.available = True
            print(f"{mem.name} with id of {mem.member_id}, thanks for returning the book {self.title}. have a good time!")
        else:
            print(f"{mem.name} with id of {mem.member_id}, the book {self.title} is in the library!!!!!")
        return
class Member():
    def __init__(self, name, member_id):
        self.borrowed_books = []
        self.name=name
        self.member_id=member_id
    def __str__(self):
        print(f"his/her name is {self.name} and its id is : {self.member_id} he/she borrowed these books : {self.borrowed_books}")
        return
    def borrow_book(self, Book):
        if Book not in self.borrowed_books:
            self.borrowed_books.append(Book)
            Book.borrow(self)
        else:
            print(f"maember {self.name}, you borrowed this book!")
    def return_book(self, Book):
        if Book in self.borrowed_books:
            self.borrowed_books.remove(Book)
            Book.return_book(self)
        else:
            print(f"maember {self.name}, you didn't borrow this book!")
class Library():
    def __init__(self):
        self.books=[]
        self.members=[]
    def add_book(self, book):
        self.books.append(book)
    def register_member(self, member):
        self.members.append(member)
    def issue_book(self, member_id, isbn):
        for i in self.books:
            if i.isbn == isbn:
                aaa=True
                ii=self.books.index(i)
        for j in self.members:
            if j.member_id == member_id:
                bbb=True
                jj=self.members.index(j)
        e1=f"there is no such a book with isbn of {isbn}".title()
        e2=f"there is no such a member with id of {member_id}".title()
        if aaa and bbb:
            self.members[jj].borrow_book(self.books[ii])
            aaa=False
            bbb=False
        elif aaa:
            print(e1)
        elif bbb:
            print(e2)
        else:
            print(e1," and ",e2)
    def return_book(self, member_id, isbn):
        for i in self.books:
            if i.isbn == isbn:
                aaa=True
                ii=self.books.index(i)
        for j in self.members:
            if j.member_id == member_id:
                bbb=True
                jj=self.members.index(j)
        e1=f"there is no such a book with isbn of {isbn}".title()
        e2=f"there is no such a member with id of {member_id}".title()
        if aaa and bbb:
            self.members[jj].return_book(self.books[ii])
            aaa=False
            bbb=False
        elif aaa:
            print(e1)
        elif bbb:
            print(e2)
        else:
            print(e1," and ",e2)
book1 = Book("1984", "جورج اورول", "1234567890")
book2 = Book("کشتن مرغ مقلد", "هارپر لی", "0987654321")
library = Library()
library.add_book(book1)
library.add_book(book2)
member = Member("آلیس", "M001")
library.register_member(member)
library.issue_book("M001", "1234567890")
library.return_book("M001", "1234567890")


# github address :   https://github.com/Barmad6666/Django-classes-1