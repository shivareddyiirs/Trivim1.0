# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Point_cloud_generation.ui'
#
# Created: Wed Nov 19 14:05:56 2014
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
        Dialog.resize(691, 409)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 651, 371))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.buttonBox = QtGui.QDialogButtonBox(self.groupBox)
        self.buttonBox.setGeometry(QtCore.QRect(280, 310, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(39, 40, 581, 131))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 40, 71, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(50, 40, 131, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(213, 40, 191, 31))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(84, 90, 311, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(40, 190, 581, 91))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.pushButton = QtGui.QPushButton(self.groupBox_3)
        self.pushButton.setGeometry(QtCore.QRect(80, 30, 321, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Trivim", None))
        self.groupBox.setTitle(_translate("Dialog", "Point Cloud Generation", None))
        self.groupBox_2.setTitle(_translate("Dialog", "1. Generate Sparse Point Cloud and Densify", None))
        self.pushButton_2.setText(_translate("Dialog", "Browse", None))
        self.label.setText(_translate("Dialog", "Select Directory of Photos", None))
        self.pushButton_3.setText(_translate("Dialog", "Generate and Densify Point Cloud", None))
        self.groupBox_3.setTitle(_translate("Dialog", "2. Georeference Point Cloud", None))
        self.pushButton.setText(_translate("Dialog", "Georeference", None))

