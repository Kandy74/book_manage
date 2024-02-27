"""
图书类
"""


class Book:
    id = None
    bookName = None
    author = None
    sex = '男'
    price = None
    bookTypeId = -1
    bookDesc = None

    def __init__(self, bookName, author, bookTypeId):
        self.bookName = bookName
        self.author = author
        self.bookTypeId = bookTypeId

    # 上面的是常用的 下面的是重写 在用的时候调用 Book.my_constructor()
    @staticmethod
    def my_constructor(bookName, author, sex, price, bookTypeId, bookDesc):
        obj = Book(bookName, author, bookTypeId)
        obj.sex = sex
        obj.price = price
        obj.bookDesc = bookDesc
        return obj

    @staticmethod
    def my_constructor2(id, bookName, author, sex, price, bookTypeId, bookDesc):
        obj2 = Book(bookName, author, bookTypeId)
        obj2.id = id
        obj2.sex = sex
        obj2.price = price
        obj2.bookDesc = bookDesc
        return obj2
