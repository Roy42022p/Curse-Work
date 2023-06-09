# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Operations.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main_Oper(object):
    def setupUi(self, Main_Oper):
        Main_Oper.setObjectName("Main_Oper")
        Main_Oper.resize(1102, 824)
        Main_Oper.setStyleSheet("background-color:rgb(54, 54, 54);")
        self.label = QtWidgets.QLabel(Main_Oper)
        self.label.setGeometry(QtCore.QRect(210, 20, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255, 0, 0)")
        self.label.setObjectName("label")
        self.IDclient = QtWidgets.QLabel(Main_Oper)
        self.IDclient.setGeometry(QtCore.QRect(40, 90, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.IDclient.setFont(font)
        self.IDclient.setStyleSheet("color:\n"
"rgb(255, 255, 255)")
        self.IDclient.setObjectName("IDclient")
        self.tipOperations = QtWidgets.QLabel(Main_Oper)
        self.tipOperations.setGeometry(QtCore.QRect(40, 250, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tipOperations.setFont(font)
        self.tipOperations.setStyleSheet("color:\n"
"rgb(255, 255, 255)")
        self.tipOperations.setObjectName("tipOperations")
        self.accept = QtWidgets.QPushButton(Main_Oper)
        self.accept.setGeometry(QtCore.QRect(370, 390, 111, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.accept.setFont(font)
        self.accept.setStyleSheet("color:rgb(0, 0, 0);\n"
"background-color:rgb(0, 255, 0)")
        self.accept.setObjectName("accept")
        self.back = QtWidgets.QPushButton(Main_Oper)
        self.back.setGeometry(QtCore.QRect(20, 470, 111, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.back.setFont(font)
        self.back.setStyleSheet("color:rgb(0, 0, 0);\n"
"background-color:rgb(171, 171, 171)")
        self.back.setObjectName("back")
        self.numberScheta = QtWidgets.QLabel(Main_Oper)
        self.numberScheta.setGeometry(QtCore.QRect(40, 170, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.numberScheta.setFont(font)
        self.numberScheta.setStyleSheet("color:\n"
"rgb(255, 255, 255)")
        self.numberScheta.setObjectName("numberScheta")
        self.summ = QtWidgets.QLabel(Main_Oper)
        self.summ.setGeometry(QtCore.QRect(50, 320, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.summ.setFont(font)
        self.summ.setStyleSheet("color:\n"
"rgb(255, 255, 255)")
        self.summ.setObjectName("summ")
        self.id_client = QtWidgets.QLineEdit(Main_Oper)
        self.id_client.setGeometry(QtCore.QRect(290, 90, 191, 41))
        self.id_client.setObjectName("id_client")
        self.num_bill = QtWidgets.QLineEdit(Main_Oper)
        self.num_bill.setGeometry(QtCore.QRect(290, 160, 191, 41))
        self.num_bill.setObjectName("num_bill")
        self.type_oper = QtWidgets.QLineEdit(Main_Oper)
        self.type_oper.setGeometry(QtCore.QRect(290, 240, 191, 41))
        self.type_oper.setObjectName("type_oper")
        self.summa = QtWidgets.QLineEdit(Main_Oper)
        self.summa.setGeometry(QtCore.QRect(290, 320, 191, 41))
        self.summa.setObjectName("summa")
        self.tab_bill = QtWidgets.QTextEdit(Main_Oper)
        self.tab_bill.setGeometry(QtCore.QRect(510, 40, 541, 461))
        self.tab_bill.setObjectName("tab_bill")
        self.tab_oper = QtWidgets.QTextEdit(Main_Oper)
        self.tab_oper.setGeometry(QtCore.QRect(120, 540, 861, 261))
        self.tab_oper.setObjectName("tab_oper")

        self.retranslateUi(Main_Oper)
        QtCore.QMetaObject.connectSlotsByName(Main_Oper)

    def retranslateUi(self, Main_Oper):
        _translate = QtCore.QCoreApplication.translate
        Main_Oper.setWindowTitle(_translate("Main_Oper", "Form"))
        self.label.setText(_translate("Main_Oper", "Операции"))
        self.IDclient.setText(_translate("Main_Oper", "Введите ID Клиента"))
        self.tipOperations.setText(_translate("Main_Oper", "Введите Тип Операции"))
        self.accept.setText(_translate("Main_Oper", "Подтвердить"))
        self.back.setText(_translate("Main_Oper", "Назад"))
        self.numberScheta.setText(_translate("Main_Oper", "Введите Номер Счета"))
        self.summ.setText(_translate("Main_Oper", "Сумма"))
        self.tab_oper.setHtml(_translate("Main_Oper", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main_Oper = QtWidgets.QWidget()
    ui = Ui_Main_Oper()
    ui.setupUi(Main_Oper)
    Main_Oper.show()
    sys.exit(app.exec_())
