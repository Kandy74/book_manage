"""
用户实体类
"""


# 用户实体类
class User:
    # 编号 主建ID
    id = None
    # 用户名
    userName = None
    # 密码
    password = None

    def __init__(self, userName, password):
        self.userName = userName
        self.password = password
