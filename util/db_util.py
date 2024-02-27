"""
数据库连接工具包
"""

from pymysql import Connect


def get_con():
    """
    获取数据库链接
    :return:
    """
    con = Connect(
        host='localhost',  # 主机名
        port=3306,  # 端口
        user="root",  # 账号
        password='123456',  # 密码
        database='db_book',  # 数据库
        autocommit=True  # 自动提交，在插入、修改的时候会自动更改
    )
    return con


def close_con(con: Connect):
    """
    关闭连接
    :param con:
    :return:
    """
    if con:
        con.close()


if __name__ == '__main__':
    con = None
    try:
        con = get_con()
        # 创建游标对象
        cursor = con.cursor()
        cursor.execute('select * from t_user')
        result = cursor.fetchall()
        print(result)
        # sql = """
        # CREATE TABLE `t_book2` (
        # `id` int(11) NOT NULL AUTO_INCREMENT,
        # `bookName` varchar(20) DEFAULT NULL,
        # `author` varchar(20) DEFAULT NULL,
        # `sex` varchar(10) DEFAULT NULL,
        # `price` float DEFAULT NULL,
        # `bookTypeId` int(11) DEFAULT NULL,
        # `bookDesc` varchar(1000) DEFAULT NULL,
        # PRIMARY KEY (`id`),
        # KEY `bookTypeId` (`bookTypeId`),
        # CONSTRAINT `t_book_ibfk_1` FOREIGN KEY (`bookTypeId`) REFERENCES `t_booktype`
        # (`id`)
        # ) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
        # """
        # cursor.execute(sql)
    except Exception as e:
        print(e)
    finally:
        close_con(con)
