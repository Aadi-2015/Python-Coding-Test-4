class Book:
    def __init__(self,author,title):
        self.author = author
        self.title = title
        is_borrowed=False
    def borrow(self): 
        is_borrowed=True
        print('You have purchased it!')
    def return_book(self):
        is_borrowed=False
        print('Thank you for returning it on time.')
d=Book()
d.borrow()
d.return_book()                   