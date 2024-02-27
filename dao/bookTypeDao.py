"""
图书类别数据访问对象
所有的Dao里 都是对数据库操作
"""
from entity.BookTypeModel import BookType
from util.db_util import get_con, close_con


def add(bookType: BookType):
    """
    向数据库中添加图书类
    :param bookType:图书类别实体
    :return: 返回执行的记录条数
    """
    con = None
    try:
        con = get_con()
        # 创建游标对象
        cursor = con.cursor()
        cursor.execute(f"insert into t_booktype value(null,'{bookType.bookTypeName}','{bookType.bookTypeDesc}')")
        return cursor.rowcount
    except Exception as e:
        print(e)
        con.rollback()
        return 0
    finally:
        close_con(con)


def list(s_bookTypeName: str):
    """
    查询图书类别
    :param s_bookTypeName: 图书类别名称
    :return: 返回图书类别列表
    """
    con = None
    try:
        con = get_con()
        # 创建游标对象
        cursor = con.cursor()
        cursor.execute(f"select * from t_booktype where bookTypeName like '%{s_bookTypeName}%'")
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return []
    finally:
        close_con(con)


def searchBookType(bookType: BookType):
    """
    查询图书类别
    :param bookType: 图书类别实体
    :return: 返回图书类别列表
    """
    con = None
    try:
        con = get_con()
        # 创建游标对象
        cursor = con.cursor()
        cursor.execute(f"select * from t_booktype where bookTypeName like '%{bookType.bookTypeName}%'")
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return []
    finally:
        close_con(con)


def update(bookType: BookType):
    """
    修改属性
    :param bookType:
    :return:
    """
    con = None
    try:
        con = get_con()
        cursor = con.cursor()
        cursor.execute(
            f"update t_booktype set bookTypeName='{bookType.bookTypeName}',bookTypeDesc='{bookType.bookTypeDesc}' where id={bookType.id}")
        return cursor.rowcount
    except Exception as e:
        print(e)
        print('没修改成功')
        con.rollback()
        return 0
    finally:
        close_con(con)


def delete(bookType: BookType):
    """
    删除属性
    :param bookType:
    :return:
    """
    con = None
    try:
        con = get_con()
        cursor = con.cursor()
        cursor.execute(f"delete from t_booktype where id ={bookType.id}")
        return cursor.rowcount
    except Exception as e:
        print(e)
        con.rollback()
        return 0
    finally:
        close_con(con)


if __name__ == '__main__':
    ls = list("")
    for l in ls:
        print(l[1])
