# Form implementation generated from reading ui file '图书类别维护.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
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
        icon.addPixmap(QtGui.QPixmap("../images/search.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.searchBtn.setIcon(icon)
        self.searchBtn.setObjectName("searchBtn")
        self.bookTypeTable = QtWidgets.QTableWidget(parent=Form)
        self.bookTypeTable.setGeometry(QtCore.QRect(40, 140, 631, 211))
        self.bookTypeTable.setObjectName("bookTypeTable")
        self.bookTypeTable.setColumnCount(0)
        self.bookTypeTable.setRowCount(0)
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
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(400, 30, 191, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=self.groupBox_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(110, 60, 481, 71))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.booktypemodifybtn = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.booktypemodifybtn.setGeometry(QtCore.QRect(150, 150, 75, 24))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/modify.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.booktypemodifybtn.setIcon(icon1)
        self.booktypemodifybtn.setObjectName("booktypemodifybtn")
        self.booktypedelbtn = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.booktypedelbtn.setGeometry(QtCore.QRect(450, 150, 75, 24))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../images/delete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.booktypedelbtn.setIcon(icon2)
        self.booktypedelbtn.setObjectName("booktypedelbtn")

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
