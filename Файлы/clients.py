# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Info_Clients.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Clients(object):
    def setupUi(self, Clients):
        Clients.setObjectName("Clients")
        Clients.resize(762, 416)
        Clients.setStyleSheet("background-color:rgb(54, 54, 54);")
        self.logs = QtWidgets.QTextEdit(Clients)
        self.logs.setGeometry(QtCore.QRect(20, 90, 721, 251))
        self.logs.setObjectName("logs")
        self.infClients = QtWidgets.QLabel(Clients)
        self.infClients.setGeometry(QtCore.QRect(220, 30, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.infClients.setFont(font)
        self.infClients.setStyleSheet("color:rgb(255, 255, 255)")
        self.infClients.setObjectName("infClients")
        self.back = QtWidgets.QPushButton(Clients)
        self.back.setGeometry(QtCore.QRect(630, 360, 111, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.back.setFont(font)
        self.back.setStyleSheet("color:rgb(0, 0, 0);\n"
"background-color:rgb(171, 171, 171)")
        self.back.setObjectName("back")

        self.retranslateUi(Clients)
        QtCore.QMetaObject.connectSlotsByName(Clients)

    def retranslateUi(self, Clients):
        _translate = QtCore.QCoreApplication.translate
        Clients.setWindowTitle(_translate("Clients", "Form"))
        self.infClients.setText(_translate("Clients", "Информация о Клиентах"))
        self.back.setText(_translate("Clients", "Назад"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Clients = QtWidgets.QWidget()
    ui = Ui_Clients()
    ui.setupUi(Clients)
    Clients.show()
    sys.exit(app.exec_())
