class Book():

    def __init__(self, author, name, pages):
        self.author = author
        self.name = name
        self.pages = pages

    def __str__(self):
       return f'The author of this book is {self.author} and the name is{self.name}'
    def __len__(self):
        return self.pages

myBook = Book('Abhishek','Good to great',350)
print(myBook)
length = len(myBook)
print(length)