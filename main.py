import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel

from book import book_info_add, book_info_manage
from bookType import bookTypeAdd, bookTypeManage
from dao import userDao
from entity import user_model


class Ui_mainwindows(QMainWindow):

    def __init__(self):
        super(Ui_mainwindows, self).__init__()
        self.setupUi(self)

    def setupUi(self, mainwindows):
        mainwindows.setObjectName("mainwindows")
        mainwindows.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        mainwindows.resize(1038, 684)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        mainwindows.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=mainwindows)
        self.centralwidget.setObjectName("centralwidget")

        # 设置背景图片
        self.centralwidget.setStyleSheet("border-image:url('images/main.jpeg')")

        mainwindows.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=mainwindows)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1038, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(parent=self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_3.setObjectName("menu_3")
        mainwindows.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=mainwindows)
        self.statusbar.setObjectName("statusbar")

        # 设置状态栏内容
        mylabel = QLabel()
        mylabel.setText('当前登录用户：' + userDao.currentUser.userName + '|作者：Kandy')
        self.statusbar.addWidget(mylabel)
        mainwindows.setStatusBar(self.statusbar)
        self.action = QtGui.QAction(parent=mainwindows)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/add.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action.setIcon(icon1)
        self.action.setObjectName("action")
        self.action_2 = QtGui.QAction(parent=mainwindows)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/modify.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action_2.setIcon(icon2)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtGui.QAction(parent=mainwindows)
        self.action_3.setIcon(icon1)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtGui.QAction(parent=mainwindows)
        self.action_4.setIcon(icon2)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtGui.QAction(parent=mainwindows)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/password.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action_5.setIcon(icon3)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtGui.QAction(parent=mainwindows)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action_6.setIcon(icon4)
        self.action_6.setObjectName("action_6")
        self.actionAbout = QtGui.QAction(parent=mainwindows)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/about.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionAbout.setIcon(icon5)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtGui.QAction(parent=mainwindows)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/bookManager.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionHelp.setIcon(icon6)
        self.actionHelp.setObjectName("actionHelp")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        # 菜单点击，图书类别 不加[QAction]也能操作
        self.menu_2.triggered[QAction].connect(self.openBookType)
        self.menu.triggered.connect(self.open_book_info)

        self.menu_2.addAction(self.action_3)
        self.menu_2.addAction(self.action_4)
        self.menu_3.addAction(self.action_5)
        self.menu_3.addAction(self.action_6)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.actionAbout)
        self.menu_3.addAction(self.actionHelp)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(mainwindows)
        QtCore.QMetaObject.connectSlotsByName(mainwindows)

    def retranslateUi(self, mainwindows):
        _translate = QtCore.QCoreApplication.translate
        mainwindows.setWindowTitle(_translate("mainwindows", "图书管理系统"))
        self.menu.setTitle(_translate("mainwindows", "图书管理"))
        self.menu_2.setTitle(_translate("mainwindows", "图书类别管理"))
        self.menu_3.setTitle(_translate("mainwindows", "系统设置"))
        self.action.setText(_translate("mainwindows", "图书添加"))
        self.action_2.setText(_translate("mainwindows", "图书信息管理"))
        self.action_3.setText(_translate("mainwindows", "图书类别添加"))
        self.action_4.setText(_translate("mainwindows", "图书类别信息管理"))
        self.action_5.setText(_translate("mainwindows", "修改密码"))
        self.action_6.setText(_translate("mainwindows", "安全退出"))
        self.actionAbout.setText(_translate("mainwindows", "About"))
        self.actionHelp.setText(_translate("mainwindows", "Help"))

    def openBookType(self, m):
        if m.text() == "图书类别添加":
            self.bookTypeAdd = bookTypeAdd.Ui_Form()
            self.bookTypeAdd.show()
        elif m.text() == "图书类别信息管理":
            self.bookTypeManage = bookTypeManage.Ui_Form()
            self.bookTypeManage.show()

    def open_book_info(self, m):
        if m.text() == "图书添加":
            self.book_info_add = book_info_add.Ui_Form()
            self.book_info_add.show()
        elif m.text() == "图书信息管理":
            self.book_info_manage = book_info_manage.Ui_Form()
            self.book_info_manage.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_mainwindows()
    ui.show()
    sys.exit(app.exec())
