from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(): pass


class MyBook(Book):
    def __init__(self):
        Book.__init__()

    def display(self):
        print("Title:", title)
        print("Author:", author)
        print("Price:", price)


title = input()
author = input()
price = int(input())
new_novel = MyBook(title, author, price)
new_novel.display()