# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cam_calib.ui'
#
# Created: Sat Nov 29 12:41:42 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(782, 734)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../bin_31/bin/isro.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 30, 351, 311))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(30, 270, 291, 23))
        self.pushButton.setStyleSheet(_fromUtf8("border-color: rgb(0, 85, 0);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_5 = QtGui.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(220, 110, 75, 23))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 50, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 171, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.comboBox = QtGui.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(110, 40, 211, 31))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.plainTextEdit_3 = QtGui.QPlainTextEdit(self.groupBox)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(20, 170, 311, 31))
        self.plainTextEdit_3.setObjectName(_fromUtf8("plainTextEdit_3"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(390, 30, 361, 311))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 270, 291, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 91, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 91, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(120, 50, 181, 31))
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.plainTextEdit_4 = QtGui.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(120, 100, 181, 31))
        self.plainTextEdit_4.setObjectName(_fromUtf8("plainTextEdit_4"))
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 360, 741, 361))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 110, 291, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_4.setGeometry(QtCore.QRect(410, 170, 291, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.groupBox_3)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(40, 30, 321, 251))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.buttonBox = QtGui.QDialogButtonBox(self.groupBox_3)
        self.buttonBox.setEnabled(True)
        self.buttonBox.setGeometry(QtCore.QRect(570, 320, 161, 31))
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setStyleSheet(_fromUtf8(""))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Camera Calibration", None))
        self.groupBox.setTitle(_translate("Dialog", "Select Camera and Directory", None))
        self.pushButton.setText(_translate("Dialog", "Calculate Parameters", None))
        self.pushButton_5.setText(_translate("Dialog", "Browse", None))
        self.label.setText(_translate("Dialog", "Camera Name", None))
        self.label_2.setText(_translate("Dialog", "Directory for Chessboard Images", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Add New Camera", None))
        self.pushButton_2.setText(_translate("Dialog", "Add New Camera", None))
        self.label_3.setText(_translate("Dialog", "Camera Name", None))
        self.label_4.setText(_translate("Dialog", "Sensor Width", None))
        self.groupBox_3.setTitle(_translate("Dialog", "Camera Parameters", None))
        self.pushButton_3.setText(_translate("Dialog", "Load Camera Parameters", None))
        self.pushButton_4.setText(_translate("Dialog", "Save Camera Parameters", None))

import tt_rc
