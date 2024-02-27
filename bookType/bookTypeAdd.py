import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox

from dao import bookTypeDao
from entity.BookTypeModel import BookType


class Ui_Form(QWidget):

    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(630, 454)
        self.formLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(70, 50, 491, 331))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(15)
        self.formLayout.setVerticalSpacing(25)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.book_type_info_input = QtWidgets.QTextEdit(parent=self.formLayoutWidget)
        self.book_type_info_input.setObjectName("book_type_info_input")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.book_type_info_input)
        self.book_style_input = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.book_style_input.setObjectName("book_style_input")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.book_style_input)
        self.book_style_addbtn = QtWidgets.QPushButton(parent=Form)
        self.book_style_addbtn.setGeometry(QtCore.QRect(140, 400, 75, 24))
        self.book_style_addbtn.setObjectName("book_style_addbtn")
        # 点击添加，绑定添加槽函数add
        self.book_style_addbtn.clicked.connect(self.add)
        self.book_style_resetbtn = QtWidgets.QPushButton(parent=Form)
        self.book_style_resetbtn.setGeometry(QtCore.QRect(360, 400, 75, 24))
        self.book_style_resetbtn.setObjectName("book_style_resetbtn")
        # 点击重置，绑定重置槽函数reset
        self.book_style_resetbtn.clicked.connect(self.reset)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "图书类别名称："))
        self.label_2.setText(_translate("Form", "图书类别描述："))
        self.book_style_addbtn.setText(_translate("Form", "添加"))
        self.book_style_resetbtn.setText(_translate("Form", "重置"))

    def reset(self):
        """
        重置内容
        :return:
        """
        self.book_style_input.setText("")
        self.book_type_info_input.setPlainText("")

    def add(self):
        """
        添加图书类别
        :return:
        """
        bookTypeName = self.book_style_input.text()
        bookTypeDesc = self.book_type_info_input.toPlainText()
        if bookTypeName.strip() == "":
            QMessageBox.warning(None, "系统提示", "书类型为空")
        else:
            bookType: BookType = BookType(bookTypeName, bookTypeDesc)
            if bookTypeDao.add(bookType) > 0:
                QMessageBox.information(None, "系统提示", "添加成功")
                self.reset()
            else:
                QMessageBox.warning(None, "系统提示", "添加失败")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec())
