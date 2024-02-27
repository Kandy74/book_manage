from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QModelIndex
from PyQt6.QtWidgets import QWidget, QSizePolicy, QHeaderView, QMessageBox

import sys

from dao import bookDao, bookTypeDao
from dao.bookDao import modify_book, return_typeid
from entity.BookModel import Book


class Ui_Form(QWidget):

    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUi(self)
        self.init_booktype_list()
        self.init_book_Form()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(871, 670)
        self.groupBox = QtWidgets.QGroupBox(parent=Form)
        self.groupBox.setGeometry(QtCore.QRect(50, 40, 751, 101))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 50, 54, 16))
        self.label.setObjectName("label")
        self.book_name_input = QtWidgets.QLineEdit(parent=self.groupBox)
        self.book_name_input.setGeometry(QtCore.QRect(100, 50, 113, 21))
        self.book_name_input.setObjectName("book_name_input")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(240, 50, 54, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(470, 50, 54, 16))
        self.label_3.setObjectName("label_3")
        self.book_author_input = QtWidgets.QLineEdit(parent=self.groupBox)
        self.book_author_input.setGeometry(QtCore.QRect(320, 50, 113, 21))
        self.book_author_input.setObjectName("book_author_input")
        self.comboBox_booktype = QtWidgets.QComboBox(parent=self.groupBox)
        self.comboBox_booktype.setGeometry(QtCore.QRect(540, 50, 91, 22))
        self.comboBox_booktype.setObjectName("comboBox_booktype")
        self.search_btn = QtWidgets.QPushButton(parent=self.groupBox)
        self.search_btn.setGeometry(QtCore.QRect(660, 50, 75, 24))
        self.search_btn.setObjectName("search_btn")
        # 绑定按钮,实现搜索
        self.search_btn.clicked.connect(self.init_book_Form)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=Form)
        self.groupBox_2.setGeometry(QtCore.QRect(50, 370, 751, 261))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(50, 40, 54, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(50, 80, 54, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(50, 130, 54, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(230, 40, 54, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(230, 80, 54, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(480, 40, 54, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(480, 80, 54, 16))
        self.label_10.setObjectName("label_10")
        self.desc = QtWidgets.QPlainTextEdit(parent=self.groupBox_2)
        self.desc.setGeometry(QtCore.QRect(90, 130, 581, 71))
        self.desc.setObjectName("desc")
        self.modify_btn = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.modify_btn.setGeometry(QtCore.QRect(190, 220, 75, 24))
        self.modify_btn.setObjectName("modify_btn")
        # 绑定修改按钮
        self.modify_btn.clicked.connect(self.book_modify)
        self.delete_btn = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.delete_btn.setGeometry(QtCore.QRect(440, 220, 75, 24))
        self.delete_btn.setObjectName("delete_btn")

        self.delete_btn.clicked.connect(self.book_delete)

        self.id_input = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.id_input.setGeometry(QtCore.QRect(90, 40, 113, 21))
        self.id_input.setReadOnly(True)
        self.id_input.setObjectName("id_input")
        self.id_input.setStyleSheet('background-color:lightgray')
        self.modify_book_name = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.modify_book_name.setGeometry(QtCore.QRect(300, 40, 113, 21))
        self.modify_book_name.setObjectName("modify_book_name")
        self.rbtn_man = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.rbtn_man.setGeometry(QtCore.QRect(550, 40, 95, 20))
        self.rbtn_man.setObjectName("rbtn_man")
        self.rbtn_woman = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.rbtn_woman.setGeometry(QtCore.QRect(640, 40, 95, 20))
        self.rbtn_woman.setObjectName("rbtn_woman")
        self.modify_book_price = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.modify_book_price.setGeometry(QtCore.QRect(90, 80, 113, 21))
        self.modify_book_price.setObjectName("modify_book_price")
        self.modify_book_author = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.modify_book_author.setGeometry(QtCore.QRect(300, 80, 113, 21))
        self.modify_book_author.setObjectName("modify_book_author")
        self.cbb_type_modify = QtWidgets.QComboBox(parent=self.groupBox_2)
        self.cbb_type_modify.setGeometry(QtCore.QRect(550, 80, 121, 22))
        self.cbb_type_modify.setObjectName("cbb_type_modify")

        self.tableWidget = QtWidgets.QTableWidget(parent=Form)
        self.tableWidget.setGeometry(QtCore.QRect(50, 150, 751, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        # 绑定点击事件,显示表单
        self.tableWidget.clicked.connect(self.show_form)
        self.tableWidget.clicked.connect(self.select_booktype)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "图书信息管理"))
        self.groupBox.setTitle(_translate("Form", "查询操作"))
        self.label.setText(_translate("Form", "图书名称："))
        self.label_2.setText(_translate("Form", "图书作者："))
        self.label_3.setText(_translate("Form", "图书类别："))
        self.search_btn.setText(_translate("Form", "搜索"))
        self.groupBox_2.setTitle(_translate("Form", "表单操作"))
        self.label_4.setText(_translate("Form", "编号："))
        self.label_5.setText(_translate("Form", "价格："))
        self.label_6.setText(_translate("Form", "描述："))
        self.label_7.setText(_translate("Form", "图书名称："))
        self.label_8.setText(_translate("Form", "图书作者："))
        self.label_9.setText(_translate("Form", "作者性别："))
        self.label_10.setText(_translate("Form", "图书类别："))
        self.modify_btn.setText(_translate("Form", "修改"))
        self.delete_btn.setText(_translate("Form", "删除"))
        self.rbtn_man.setText(_translate("Form", "男"))
        self.rbtn_woman.setText(_translate("Form", "女"))

    def init_book_Form(self):
        """
        初始化书列表,并实现三种搜索功能
        :return:
        """
        s_bookName = self.book_name_input.text()
        s_bookAuthor = self.book_author_input.text()
        s_bookTypeId = self.comboBox_booktype.currentData()
        s_book = Book(s_bookName, s_bookAuthor, s_bookTypeId)
        # 获取查询结果，并添加到表格中,返回的是一个列表，列表中的每个元素都是一个元组
        result = bookDao.book_list(s_book)

        row = 0
        # 计算行数，如果查询结果为空，则行数为0，否则为查询结果的长度，并将其赋值给row
        if result:
            row = len(result)

        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(row)
        self.tableWidget.verticalHeader().setVisible(False)
        # 设置表格不可编辑，默认为可编辑，设置为不可编辑，防止修改数据库数据，但是可�
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        # 设置表格大小，自适应，填充数据
        self.tableWidget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.tableWidget.setHorizontalHeaderLabels(["编号", "图名", "作者", "性别", "价格", "书类编号"])
        # 隐藏最后一列
        self.tableWidget.setColumnHidden(6, True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        if result:
            for i in range(row):
                for j in range(7):
                    data = QtWidgets.QTableWidgetItem(str(result[i][j]))
                    self.tableWidget.setItem(i, j, data)

    def show_form(self):
        """
        实现表单显示已选择的列表
        :return:
        """
        row = self.tableWidget.currentRow()
        self.modify_book_name.setText(self.tableWidget.item(row, 1).text())
        self.modify_book_price.setText(self.tableWidget.item(row, 4).text())
        self.id_input.setText(self.tableWidget.item(row, 0).text())
        self.modify_book_author.setText(self.tableWidget.item(row, 2).text())
        sex = self.tableWidget.item(row, 3).text()
        if sex.strip(" ") == "男":
            self.rbtn_man.setChecked(True)
        else:
            self.rbtn_woman.setChecked(True)
        self.desc.setPlainText(self.tableWidget.item(row, 6).text())

    def init_booktype_list(self):
        """
        初始化图书类别(上下二个)下拉框，添加图书类别
        :return:
        """
        self.cbb_type_modify.addItem("", -1)
        booktype_list = bookTypeDao.list("")  # 获取所有图书类别信息
        for book_type in booktype_list:
            # addItem(显示，返回索引值)
            self.cbb_type_modify.addItem(book_type[1], book_type[0])

        self.comboBox_booktype.addItem("请选择", -1)
        for book_type in booktype_list:
            self.comboBox_booktype.addItem(f"{book_type[0]}-{book_type[1]}", book_type[0])

    def select_booktype(self):
        """
        选择图书类别
        :return:
        """
        row = self.tableWidget.currentRow()
        typename = bookDao.return_typename(int(self.tableWidget.item(row, 5).text()))[0]
        self.cbb_type_modify.setCurrentText(typename)

    def book_delete(self):
        """
        删除图书信息
        :param id:
        :return:
        """""
        aply = QMessageBox.question(self, "系统提示", "确定删除？",
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if aply == QMessageBox.StandardButton.Yes:
            delete_id = self.id_input.text()
            if delete_id:
                delete_id = int(delete_id)
            else:
                delete_id = -1
            # 不用另加 bookDao.book_delete(delete_id)

            if bookDao.book_delete(delete_id) > 0:
                QMessageBox.information(self, "系统提示", "删除成功")
                self.init_book_Form()
            else:
                QMessageBox.warning(self, "系统提示", "删除失败")

    def book_modify(self, book):
        """
        修改图书信息
        :param book:
        :return:
        """
        name = self.modify_book_name.text()
        author = self.modify_book_author.text()
        sex = "男"
        if self.rbtn_man.isChecked():
            sex = "男"
        elif self.rbtn_woman.isChecked():
            sex = "女"
        price = self.modify_book_price.text()
        typename = self.cbb_type_modify.currentText()
        bookTypeid = return_typeid(typename)[0]

        bookDesc = self.desc.toPlainText()

        id = self.id_input.text()

        book = Book.my_constructor2(id, name, author, sex, price, bookTypeid, bookDesc)

        if bookDao.modify_book(book) > 0:
            QMessageBox.information(self, "系统提示", "修改成功")
            self.init_book_Form()
        else:
            QMessageBox.warning(self, "系统提示", "修改失败")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec())
