"""
用户模块-数据访问对象
"""
from entity.user_model import User
from util import db_util

currentUser: User = None


def login(user: User):
    """
    用户登录判断
    :param user:用户实体
    :return:登录成功返回用户信息实体，登录失败，返回None
    """
    con = None
    try:
        con = db_util.get_con()
        cursor = con.cursor()
        # 字符串类型的，两个{}外面必须加一个''
        cursor.execute(f"select * from t_user where userName='{user.userName}' and password = '{user.password}'")
        return cursor.fetchone()
    except Exception as e:
        con.rollback()
        print(e)
    finally:
        db_util.close_con(con)
