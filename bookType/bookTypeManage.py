""""
图书管理模块
"""
import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QModelIndex
from PyQt6.QtWidgets import QWidget, QApplication, QSizePolicy, QHeaderView, QMessageBox

from dao import bookTypeDao, bookDao
from entity.BookTypeModel import BookType


class Ui_Form(QWidget):

    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUi(self)
        self.initTable()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(726, 565)
        self.groupBox = QtWidgets.QGroupBox(parent=Form)
        self.groupBox.setGeometry(QtCore.QRect(40, 20, 631, 111))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 60, 91, 16))
        self.label.setObjectName("label")
        self.s_bookTypeNameinput = QtWidgets.QLineEdit(parent=self.groupBox)
        self.s_bookTypeNameinput.setGeometry(QtCore.QRect(140, 60, 231, 21))
        self.s_bookTypeNameinput.setObjectName("s_bookTypeNameinput")
        self.searchBtn = QtWidgets.QPushButton(parent=self.groupBox)
        self.searchBtn.setGeometry(QtCore.QRect(420, 60, 75, 24))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/search.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.searchBtn.setIcon(icon)
        self.searchBtn.setObjectName("searchBtn")
        # 绑定定搜索按钮点击事件
        self.searchBtn.clicked.connect(self.initTable)
        self.bookTypeTable = QtWidgets.QTableWidget(parent=Form)
        self.bookTypeTable.setGeometry(QtCore.QRect(40, 140, 631, 211))
        self.bookTypeTable.setObjectName("bookTypeTable")
        self.bookTypeTable.setColumnCount(0)
        self.bookTypeTable.setRowCount(0)
        # 点击行，绑定槽函数，显示点击行的信息
        self.bookTypeTable.clicked.connect(self.initForm)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=Form)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 360, 631, 181))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(50, 30, 54, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(50, 80, 54, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(303, 30, 81, 20))
        self.label_4.setObjectName("label_4")
        self.idinput = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.idinput.setGeometry(QtCore.QRect(110, 30, 161, 21))
        self.idinput.setObjectName("idinput")
        # 不可更改self.idinput
        self.idinput.setReadOnly(True)
        # 背景色设置为浅灰色
        self.idinput.setStyleSheet("background-color:lightgray")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(400, 30, 191, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=self.groupBox_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(110, 60, 481, 71))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.booktypemodifybtn = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.booktypemodifybtn.setGeometry(QtCore.QRect(150, 150, 75, 24))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./images/modify.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.booktypemodifybtn.setIcon(icon1)
        self.booktypemodifybtn.setObjectName("booktypemodifybtn")
        # 修改属性
        self.booktypemodifybtn.clicked.connect(self.update_booktype)
        self.booktypedelbtn = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.booktypedelbtn.setGeometry(QtCore.QRect(450, 150, 75, 24))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./images/delete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.booktypedelbtn.setIcon(icon2)
        self.booktypedelbtn.setObjectName("booktypedelbtn")
        # 删除按钮
        self.booktypedelbtn.clicked.connect(self.delete)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "图书类别信息维护"))
        self.groupBox.setTitle(_translate("Form", "查询操作"))
        self.label.setText(_translate("Form", "图书类别名称："))
        self.searchBtn.setText(_translate("Form", "搜索"))
        self.groupBox_2.setTitle(_translate("Form", "表单操作"))
        self.label_2.setText(_translate("Form", "编号："))
        self.label_3.setText(_translate("Form", "描述："))
        self.label_4.setText(_translate("Form", "图书类别名称："))
        self.booktypemodifybtn.setText(_translate("Form", "修改"))
        self.booktypedelbtn.setText(_translate("Form", "删除"))

    def initTable(self):
        """
        初始化表格，添加搜索结果
        :return:
        """
        # 获取搜索结果
        s_bookTypeName = self.s_bookTypeNameinput.text()
        # 获取查询结果，并添加到表格中,返回的是一个列表，列表中的每个元素都是一个元组
        result = bookTypeDao.list(s_bookTypeName)
        row = 0
        if result:
            row = len(result)
        self.bookTypeTable.setColumnCount(3)
        self.bookTypeTable.setRowCount(row)
        self.bookTypeTable.verticalHeader().setVisible(False)
        # 设置表格不可编辑，默认为可编辑，设置为不可编辑，防止修改数据库数据，但是可�
        self.bookTypeTable.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        # 设置表格大小，自适应，填充数据
        self.bookTypeTable.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.bookTypeTable.setHorizontalHeaderLabels(["编号", "图书类别名称", "描述"])
        self.bookTypeTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.bookTypeTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)

        for i in range(row):
            for j in range(3):
                data = QtWidgets.QTableWidgetItem(str(result[i][j]))
                self.bookTypeTable.setItem(i, j, data)

    # def initForm(self, index: QModelIndex):
    #     """
    #     获取选择图书类型信息 初始化表单Form(教程方法，感觉AI的方法更好)
    #     :param index: 行信息
    #     :return:
    #     """
    #     row_index = index.row()
    #     self.idinput.setText(self.bookTypeTable.item(row_index, 0).text())

    # 定义函数，获取已选表格中的信息
    def initForm(self):
        """
        初始化表单，显示选择的行
        :return:
        """
        # 获取当前行的信息，并将信息显示在表单中，并绑定槽函数，修改图书类别信息，删除图书类别信息
        row = self.bookTypeTable.currentRow()
        self.idinput.setText(self.bookTypeTable.item(row, 0).text())
        self.lineEdit_3.setText(self.bookTypeTable.item(row, 1).text())
        self.plainTextEdit.setPlainText(self.bookTypeTable.item(row, 2).text())

    def update_booktype(self):
        """
        更新表单
        :return:
        """
        id = self.idinput.text()
        bookTypeName = self.lineEdit_3.text()
        bookTypeDesc = self.plainTextEdit.toPlainText()
        new_booktype = BookType.my_constructor(id, bookTypeName, bookTypeDesc)
        if bookTypeDao.update(new_booktype) > 0:
            QMessageBox.information(None, '系统提示', '成功')
            self.initTable()
        else:
            QMessageBox.warning(None, '系统提示', '修改失败')

    def delete(self):
        """
        删除数据
        :return:
        """
        id = self.idinput.text()
        commit = QMessageBox.question(self, "系统提示", "确定删除？",
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if commit == QMessageBox.StandardButton.Yes:
            booktypename = self.lineEdit_3.text()
            book_type_desc = self.plainTextEdit.toPlainText()
            de_book_type = BookType.my_constructor(id, booktypename, book_type_desc)

            if bookDao.countByType(id)[0] > 0:
                QMessageBox.warning(self, "系统提示", "该分类下有书！禁止删除")
                self.initTable()
            else:
                if bookTypeDao.delete(de_book_type) > 0:
                    QMessageBox.information(self, '系统提示', "删除成功")
                    self.initTable()
                else:
                    QMessageBox.warning(self, "系统提示", "删除失败")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()

    app.exec()
