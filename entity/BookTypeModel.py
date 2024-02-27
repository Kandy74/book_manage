"""
图书类别实体类
"""


class BookType:
    id = None
    bookTypeName = None
    bookTypeDesc = None

    def __init__(self, bookTypeName, bookTypeDesc):
        self.bookTypeDesc = bookTypeDesc
        self.bookTypeName = bookTypeName

    @staticmethod
    def my_constructor(id, bookTypeName, bookTypeDesc):
        obj = BookType(bookTypeName, bookTypeDesc)
        obj.id = id
        return obj
