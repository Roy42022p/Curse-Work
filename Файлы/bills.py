# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bills.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Bills(object):
    def setupUi(self, Bills):
        Bills.setObjectName("Bills")
        Bills.resize(569, 365)
        Bills.setStyleSheet("background-color:rgb(54, 54, 54);")
        self.back = QtWidgets.QPushButton(Bills)
        self.back.setGeometry(QtCore.QRect(450, 310, 111, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.back.setFont(font)
        self.back.setStyleSheet("color:rgb(0, 0, 0);\n"
"background-color:rgb(171, 171, 171)")
        self.back.setObjectName("back")
        self.infClients = QtWidgets.QLabel(Bills)
        self.infClients.setGeometry(QtCore.QRect(120, 30, 351, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.infClients.setFont(font)
        self.infClients.setStyleSheet("color:rgb(255, 255, 255)")
        self.infClients.setObjectName("infClients")
        self.logs = QtWidgets.QTextEdit(Bills)
        self.logs.setGeometry(QtCore.QRect(30, 90, 511, 201))
        self.logs.setObjectName("logs")

        self.retranslateUi(Bills)
        QtCore.QMetaObject.connectSlotsByName(Bills)

    def retranslateUi(self, Bills):
        _translate = QtCore.QCoreApplication.translate
        Bills.setWindowTitle(_translate("Bills", "Form"))
        self.back.setText(_translate("Bills", "Назад"))
        self.infClients.setText(_translate("Bills", "Информация о  Счетах Клиентов"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Bills = QtWidgets.QWidget()
    ui = Ui_Bills()
    ui.setupUi(Bills)
    Bills.show()
    sys.exit(app.exec_())
