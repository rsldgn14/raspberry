# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/user/PycharmProjects/ann-pyqt5/ui/viewScreen.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ViewScreen(object):
    def setupUi(self, ViewScreen):
        ViewScreen.setObjectName("ViewScreen")
        ViewScreen.resize(985, 732)
        self.ip_address_label = QtWidgets.QLabel(ViewScreen)
        self.ip_address_label.setGeometry(QtCore.QRect(100, 70, 351, 21))
        self.ip_address_label.setObjectName("ip_address_label")

        self.retranslateUi(ViewScreen)
        QtCore.QMetaObject.connectSlotsByName(ViewScreen)

    def retranslateUi(self, ViewScreen):
        _translate = QtCore.QCoreApplication.translate
        ViewScreen.setWindowTitle(_translate("ViewScreen", "ViewScreen"))
        self.ip_address_label.setText(_translate("ViewScreen", "IP BURDA GÖZÜKCEKTI GELDI MI"))

