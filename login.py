# Form implementation generated from reading ui file 'login_ui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QApplication, QMessageBox, QLineEdit

import main
from dao import userDao
from entity import user_model
from entity.user_model import User


class Ui_Form(QWidget):

    def __init__(self):
        super(Ui_Form, self).__init__()
        self.m = None
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.formLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(70, 90, 251, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.FieldsStayAtSizeHint)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(31)
        self.formLayout.setObjectName("formLayout")
        self.label_username = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_username.setTabletTracking(False)
        self.label_username.setObjectName("label_username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_username)
        self.lineEdit_username = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.lineEdit_username.setObjectName("lineEdit_username")
        # 默认显示为admin，可以自行修改，但是必须保证数据库中存在该用户名
        self.lineEdit_username.setText("admin")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_username)
        self.lineEdit_password = QtWidgets.QLineEdit(parent=self.formLayoutWidget)

        self.lineEdit_password.setObjectName("lineEdit_password")
        # 设置成密码格式，即不现实数字
        self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.lineEdit_password.setText("admin")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_password)
        self.label_password = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_password.setObjectName("label_password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_password)
        self.pushButton_login = QtWidgets.QPushButton(parent=Form)
        self.pushButton_login.setGeometry(QtCore.QRect(90, 220, 75, 24))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/login.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_login.setIcon(icon)
        self.pushButton_login.setObjectName("pushButton_login")
        self.pushButton_login.setShortcut("")
        # 登录按钮
        self.pushButton_login.clicked.connect(self.login)

        self.pushButton_reset = QtWidgets.QPushButton(parent=Form)
        self.pushButton_reset.setGeometry(QtCore.QRect(220, 220, 75, 24))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/reset.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_reset.setIcon(icon1)
        self.pushButton_reset.setObjectName("pushButton_reset")

        # 设置重置按钮，连接槽函数
        self.pushButton_reset.clicked.connect(self.reset_form)

        self.label_title = QtWidgets.QLabel(parent=Form)
        self.label_title.setGeometry(QtCore.QRect(140, 40, 171, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(70, 30, 71, 61))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/logo.png"))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登录界面"))
        self.label_username.setText(_translate("Form", "用户名："))
        self.label_password.setText(_translate("Form", "密    码："))
        self.pushButton_login.setText(_translate("Form", "登录"))
        self.pushButton_login.setShortcut(_translate("Form", "Return"))
        self.pushButton_reset.setText(_translate("Form", "重置"))
        self.label_title.setText(_translate("Form", "图书管理系统"))

    def reset_form(self):
        """
        重置用户名和密码
        :return:
        """
        self.lineEdit_username.setText("")
        self.lineEdit_password.setText("")

    def login(self):
        """
        用户登录判断，数据库判断成功，则打得开主窗体，否者提示报错信息
        :return:
        """
        userName = self.lineEdit_username.text()
        password = self.lineEdit_password.text()

        if userName.strip() == "" or password == "":
            QMessageBox.warning(None, '系统提示', '用户名或密码不能为空')
        else:
            user = User(userName, password)
            resultUser = userDao.login(user)
            if resultUser:
                QMessageBox.information(None, '系统提示', '用户登录成功')
                userDao.currentUser = user

                self.m = main.Ui_mainwindows()  # 实例化主窗体
                self.m.show()  # 显示主窗体
                self.hide()  # 隐藏当前的登录窗体
            else:
                QMessageBox.warning(None, '系统提示', '用户名或密码错误')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec())
