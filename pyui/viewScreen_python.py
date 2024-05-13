# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/ASUS/Desktop/ann-pyqt5/ui/viewScreen.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ViewScreen(object):
    def setupUi(self, ViewScreen):
        ViewScreen.setObjectName("ViewScreen")
        ViewScreen.resize(1079, 805)
        self.camera_area = QtWidgets.QLabel(ViewScreen)
        self.camera_area.setGeometry(QtCore.QRect(20, 40, 640, 480))
        self.camera_area.setMinimumSize(QtCore.QSize(640, 480))
        self.camera_area.setMaximumSize(QtCore.QSize(640, 480))
        self.camera_area.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.camera_area.setStyleSheet("background-color:black;color:white;font-size:48px;")
        self.camera_area.setAlignment(QtCore.Qt.AlignCenter)
        self.camera_area.setObjectName("camera_area")
        self.start_button = QtWidgets.QPushButton(ViewScreen)
        self.start_button.setGeometry(QtCore.QRect(240, 570, 93, 28))
        self.start_button.setObjectName("start_button")

        self.retranslateUi(ViewScreen)
        QtCore.QMetaObject.connectSlotsByName(ViewScreen)

    def retranslateUi(self, ViewScreen):
        _translate = QtCore.QCoreApplication.translate
        ViewScreen.setWindowTitle(_translate("ViewScreen", "ViewScreen"))
        self.camera_area.setText(_translate("ViewScreen", "Camera"))
        self.start_button.setText(_translate("ViewScreen", "Start"))

