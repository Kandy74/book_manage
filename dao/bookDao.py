"""
根据typeid判断是否在书类别里有书
"""
from util.db_util import get_con, close_con
from entity.BookModel import Book


def countByType(typeId):
    con = None
    try:
        con = get_con()
        cursor = con.cursor()
        cursor.execute(f"select count(*) as total from t_book where bookTypeId='{typeId}'")
        return cursor.fetchone()
    except Exception as e:
        print(e)
        con.rollback()
        return None
    finally:
        close_con(con)


def return_typename(typeId: int):
    con = None
    try:
        con = get_con()
        cursor = con.cursor()
        cursor.execute(f"select bookTypeName from t_booktype where id='{typeId}'")
        return cursor.fetchone()
    except Exception as e:
        print(e)
        con.rollback()
        return None
    finally:
        close_con(con)


def return_typeid(type_name: str):
    con = None
    try:
        con = get_con()
        cursor = con.cursor()
        cursor.execute(f"select id from t_booktype where bookTypeName='{type_name}'")
        return cursor.fetchone()
    except Exception as e:
        print(e)
        con.rollback()
        return None
    finally:
        close_con(con)


def book_add_dao(book: Book):
    con = None
    try:
        con = get_con()
        cursor = con.cursor()
        cursor.execute(
            f"insert into t_book value(null,'{book.bookName}','{book.author}','{book.sex}',{book.price},{book.bookTypeId},'{book.bookDesc}') ")
        return cursor.rowcount
    except Exception as e:
        print(e)
        con.rollback()
        return 0
    finally:
        close_con(con)


def book_list(s_book: Book):
    con = None
    try:
        con = get_con()
        cursor = con.cursor()
        sql = f"select * from t_book,t_booktype where t_book.bookTypeId = t_booktype.id"
        if s_book.bookName != "":
            sql += f" and t_book.bookName like '%{s_book.bookName}%'"
        if s_book.author != "":
            sql += f" and t_book.author like '%{s_book.author}%'"
        if s_book.bookTypeId != -1:
            sql += f" and t_book.bookTypeId = {s_book.bookTypeId}"

        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return None
    finally:
        close_con(con)


def book_delete(id: int):
    con = None
    try:
        con = get_con()
        cursor = con.cursor()
        cursor.execute(f"delete from t_book where id='{id}'")
        return cursor.rowcount
    except Exception as e:
        print(e)
        con.rollback()
        return 0
    finally:
        close_con(con)


def modify_book(book: Book):
    con = None
    try:
        con = get_con()
        cursor = con.cursor()
        cursor.execute(
            f"update t_book set bookName='{book.bookName}',author='{book.author}',sex='{book.sex}',"
            f"price={book.price},bookTypeId={book.bookTypeId},bookDesc='{book.bookDesc}' where id={book.id}")
        return cursor.rowcount
    except Exception as e:
        print(e)
        con.rollback()
        return 0
    finally:
        close_con(con)


if __name__ == '__main__':
    books = book_list(None)
    print(books)
