import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QApplication, QMessageBox

from dao import bookTypeDao
from dao.bookDao import book_add_dao
from entity.BookModel import Book


class Ui_Form(QWidget):

    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUi(self)
        self.init_booktype_list()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(799, 590)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(80, 60, 54, 16))
        self.label.setObjectName("label")
        self.book_name_input = QtWidgets.QLineEdit(parent=Form)
        self.book_name_input.setGeometry(QtCore.QRect(170, 60, 231, 21))
        self.book_name_input.setObjectName("book_name_input")
        self.book_author_iinput = QtWidgets.QLineEdit(parent=Form)
        self.book_author_iinput.setGeometry(QtCore.QRect(530, 60, 113, 21))
        self.book_author_iinput.setObjectName("book_author_iinput")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(440, 60, 54, 16))
        self.label_2.setObjectName("label_2")
        self.book_prince_input = QtWidgets.QLineEdit(parent=Form)
        self.book_prince_input.setGeometry(QtCore.QRect(530, 130, 113, 21))
        self.book_prince_input.setObjectName("book_prince_input")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(80, 130, 54, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(450, 130, 54, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(80, 190, 54, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setGeometry(QtCore.QRect(80, 250, 54, 16))
        self.label_6.setObjectName("label_6")
        self.rbnt_man = QtWidgets.QRadioButton(parent=Form)
        self.rbnt_man.setGeometry(QtCore.QRect(170, 130, 95, 20))
        self.rbnt_man.setObjectName("rbnt_man")
        self.rbtn_women = QtWidgets.QRadioButton(parent=Form)
        self.rbtn_women.setGeometry(QtCore.QRect(280, 130, 95, 20))
        self.rbtn_women.setObjectName("rbtn_women")
        self.comboBox_booktype = QtWidgets.QComboBox(parent=Form)
        self.comboBox_booktype.setGeometry(QtCore.QRect(170, 190, 231, 22))
        self.comboBox_booktype.setObjectName("comboBox_booktype")

        self.bookdesc_input = QtWidgets.QPlainTextEdit(parent=Form)
        self.bookdesc_input.setGeometry(QtCore.QRect(170, 250, 471, 221))
        self.bookdesc_input.setObjectName("bookdesc_input")
        self.add_btn = QtWidgets.QPushButton(parent=Form)
        self.add_btn.setGeometry(QtCore.QRect(230, 510, 75, 24))
        self.add_btn.setObjectName("add_btn")
        # 绑定按钮
        self.add_btn.clicked.connect(self.book_add)
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 510, 75, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.reset)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "图书信息添加"))
        self.label.setText(_translate("Form", "图书名称："))
        self.label_2.setText(_translate("Form", "图书作者："))
        self.label_3.setText(_translate("Form", "作者性别"))
        self.label_4.setText(_translate("Form", "图书价格："))
        self.label_5.setText(_translate("Form", "图书类别："))
        self.label_6.setText(_translate("Form", "图书描述："))
        self.rbnt_man.setText(_translate("Form", "男"))
        self.rbtn_women.setText(_translate("Form", "女"))
        self.add_btn.setText(_translate("Form", "添加"))
        self.pushButton_2.setText(_translate("Form", "重置"))

    def init_booktype_list(self):
        """
        初始化图书类别下拉框，添加图书类别
        :return:
        """
        booktype_list = bookTypeDao.list("")  # 获取所有图书类别信息
        self.comboBox_booktype.addItem("请选择图书类别", -1)
        for book_type in booktype_list:
            self.comboBox_booktype.addItem(f"{str(book_type[0])}-{book_type[1]}", book_type[0])

    def book_add(self):
        """
        添加图书信息
        :return:
        """
        book_name = self.book_name_input.text()
        book_author = self.book_author_iinput.text()
        author_sex = ""
        if self.rbnt_man.isChecked():
            author_sex = "男"
        if self.rbtn_women.isChecked():
            author_sex = "女"
        book_price = self.book_prince_input.text()
        book_type = self.comboBox_booktype.currentData()
        book_desc = self.bookdesc_input.toPlainText()
        new_book = Book.my_constructor(book_name, book_author, author_sex, book_price, book_type, book_desc)
        if book_add_dao(new_book) > 0:
            QMessageBox.information(self, "系统提示", "添加成功")
        else:
            QMessageBox.warning(self, "系统提示", "添加失败")

    def reset(self):
        """
        重置界面
        :return:
        """
        self.bookdesc_input.setPlainText("")
        self.book_name_input.setText("")
        self.book_author_iinput.setText("")
        self.book_prince_input.setText("")
        self.rbnt_man.setChecked(True)
        self.comboBox_booktype.setCurrentIndex(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec())
