# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Point_cloud_generation.ui'
#
# Created: Sat Nov 29 13:04:10 2014
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
        Dialog.resize(733, 374)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../bin_31/bin/isro.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.groupBox_4 = QtGui.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 20, 691, 341))
        self.groupBox_4.setStyleSheet(_fromUtf8("border-bottom-color: rgb(255, 138, 99);"))
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.groupBox = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 651, 161))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 70, 191, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(530, 60, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setGeometry(QtCore.QRect(180, 60, 311, 31))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.pushButton_4 = QtGui.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(180, 110, 311, 23))
        self.pushButton_4.setCheckable(False)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 200, 651, 81))
        self.groupBox_3.setStyleSheet(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 30, 311, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.buttonBox = QtGui.QDialogButtonBox(self.groupBox_4)
        self.buttonBox.setGeometry(QtCore.QRect(510, 290, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Point Cloud Generation", None))
        self.groupBox.setTitle(_translate("Dialog", "1. Generate Sparse Point Cloud and Densify", None))
        self.label.setText(_translate("Dialog", "Select Directory of Photos", None))
        self.pushButton.setText(_translate("Dialog", "Browse", None))
        self.pushButton_4.setText(_translate("Dialog", "Generate Point Cloud", None))
        self.groupBox_3.setTitle(_translate("Dialog", "2.Georeference Point Cloud", None))
        self.pushButton_3.setText(_translate("Dialog", "Georeference", None))

import tt_rc
