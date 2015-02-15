# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'advar.ui'
#
# Created: Mon Nov 17 17:22:48 2014
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
        Dialog.resize(633, 396)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 601, 371))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.buttonBox = QtGui.QDialogButtonBox(self.groupBox)
        self.buttonBox.setGeometry(QtCore.QRect(250, 330, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(45, 40, 101, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setGeometry(QtCore.QRect(160, 40, 201, 31))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(30, 190, 101, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        
        self.listWidget = QtGui.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(160, 150, 91, 151))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        
        self.pushButton_2.setGeometry(QtCore.QRect(30, 220, 101, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.listWidget_2 = QtGui.QListWidget(self.groupBox)
        self.listWidget_2.setGeometry(QtCore.QRect(290, 150, 91, 151))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(160, 90, 82, 17))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(210, 90, 82, 17))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(170, 130, 71, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(320, 130, 51, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Database Attributes", None))
        self.groupBox.setTitle(_translate("Dialog", "Add Variable", None))
        self.label.setText(_translate("Dialog", "Enter Variable Name", None))
        self.label_2.setText(_translate("Dialog", "Type", None))
        self.pushButton.setText(_translate("Dialog", "Add  Variable", None))
        self.pushButton_2.setText(_translate("Dialog", "Remove Variable", None))
        self.radioButton.setText(_translate("Dialog", "real", None))
        self.radioButton_2.setText(_translate("Dialog", "Varchar", None))
        self.label_3.setText(_translate("Dialog", "Variable_name", None))
        self.label_4.setText(_translate("Dialog", "Type", None))

import tt1_rc
