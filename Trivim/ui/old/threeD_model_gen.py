# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'threeD_model_gen.ui'
#
# Created: Fri Nov 14 11:49:59 2014
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
        Dialog.resize(745, 588)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 701, 541))
        self.groupBox.setStyleSheet(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.buttonBox = QtGui.QDialogButtonBox(self.groupBox)
        self.buttonBox.setGeometry(QtCore.QRect(330, 500, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(300, 20, 121, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 100, 111, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setGeometry(QtCore.QRect(520, 100, 111, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_5 = QtGui.QPushButton(self.groupBox)
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setGeometry(QtCore.QRect(380, 160, 121, 23))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.groupBox)
        self.pushButton_6.setEnabled(False)
        self.pushButton_6.setGeometry(QtCore.QRect(380, 210, 121, 23))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_8 = QtGui.QPushButton(self.groupBox)
        self.pushButton_8.setEnabled(False)
        self.pushButton_8.setGeometry(QtCore.QRect(380, 320, 121, 23))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.progressBar = QtGui.QProgressBar(self.groupBox)
        self.progressBar.setEnabled(False)
        self.progressBar.setGeometry(QtCore.QRect(510, 160, 118, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.progressBar_2 = QtGui.QProgressBar(self.groupBox)
        self.progressBar_2.setEnabled(False)
        self.progressBar_2.setGeometry(QtCore.QRect(530, 320, 118, 23))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName(_fromUtf8("progressBar_2"))
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(self.groupBox)
        self.plainTextEdit_2.setEnabled(False)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(20, 160, 261, 151))
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Trivim", None))
        self.groupBox.setTitle(_translate("Dialog", "3D Model Generation", None))
        self.pushButton.setText(_translate("Dialog", "Add New Building", None))
        self.pushButton_2.setText(_translate("Dialog", "Footprint Extraction", None))
        self.pushButton_3.setText(_translate("Dialog", "Load KML Files", None))
        self.pushButton_5.setText(_translate("Dialog", "Footprint Processing", None))
        self.pushButton_6.setText(_translate("Dialog", "Construct Building(s)", None))
        self.pushButton_8.setText(_translate("Dialog", "Visualise on Geo Portal", None))
        self.plainTextEdit_2.setPlainText(_translate("Dialog", "Progress Updates...", None))

import tt_rc
