class book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"'{self.title}' by {self.author}, published in {self.year}"
b1 = book("1984", "George Orwell", 1949)
b2 = book("To Kill a Mockingbird", "Harper Lee", 1960)
print(b1.get_info())
print(b2.get_info())
#class and object 
