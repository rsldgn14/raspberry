# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/user/PycharmProjects/ann-pyqt5/ui/connect.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 300)
        Dialog.setMinimumSize(QtCore.QSize(300, 300))
        Dialog.setMaximumSize(QtCore.QSize(300, 300))
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 190, 301, 111))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.connect_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.connect_button.setMaximumSize(QtCore.QSize(100, 30))
        self.connect_button.setObjectName("connect_button")
        self.horizontalLayout.addWidget(self.connect_button)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 281, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ip_input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.ip_input.setText("")
        self.ip_input.setObjectName("ip_input")
        self.gridLayout_2.addWidget(self.ip_input, 0, 1, 1, 1)
        self.ip_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.ip_label.setObjectName("ip_label")
        self.gridLayout_2.addWidget(self.ip_label, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.port_input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.port_input.setText("")
        self.port_input.setObjectName("port_input")
        self.gridLayout.addWidget(self.port_input, 0, 1, 1, 1)
        self.port_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.port_label.setObjectName("port_label")
        self.gridLayout.addWidget(self.port_label, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Connect"))
        self.connect_button.setText(_translate("Dialog", "Connect"))
        self.ip_label.setText(_translate("Dialog", "Raspberry IP Adress"))
        self.port_label.setText(_translate("Dialog", "Port                          "))

