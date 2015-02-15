# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Field_Planning.ui'
#
# Created: Thu Nov 27 22:27:05 2014
#      by: PyQt4 UI code generator 4.11.3
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
        Dialog.resize(963, 630)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../bin_31/bin/isro.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 941, 611))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.pushButton = QtGui.QPushButton(self.groupBox_3)
        self.pushButton.setGeometry(QtCore.QRect(10, 300, 111, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox_3)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 350, 921, 191))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(40, 60, 161, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(40, 110, 131, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.plainTextEdit_5 = QtGui.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_5.setGeometry(QtCore.QRect(320, 50, 261, 31))
        self.plainTextEdit_5.setObjectName(_fromUtf8("plainTextEdit_5"))
        self.plainTextEdit_6 = QtGui.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_6.setGeometry(QtCore.QRect(320, 100, 261, 31))
        self.plainTextEdit_6.setObjectName(_fromUtf8("plainTextEdit_6"))
        self.buttonBox = QtGui.QDialogButtonBox(self.groupBox_3)
        self.buttonBox.setGeometry(QtCore.QRect(590, 570, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.groupBox = QtGui.QGroupBox(self.groupBox_3)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 921, 251))
        self.groupBox.setMinimumSize(QtCore.QSize(921, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(1677, 16777215))
        self.groupBox.setStyleSheet(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 50, 131, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 171, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(40, 150, 181, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(40, 200, 211, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setGeometry(QtCore.QRect(320, 40, 261, 31))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(self.groupBox)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(320, 90, 261, 31))
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.plainTextEdit_4 = QtGui.QPlainTextEdit(self.groupBox)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(320, 190, 261, 31))
        self.plainTextEdit_4.setObjectName(_fromUtf8("plainTextEdit_4"))
        self.comboBox = QtGui.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(320, 140, 261, 31))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Trivim", None))
        self.groupBox_3.setTitle(_translate("Dialog", "Field Planning", None))
        self.pushButton.setText(_translate("Dialog", "Calculate", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Output", None))
        self.label_5.setText(_translate("Dialog", "Number of Photos Required", None))
        self.label_6.setText(_translate("Dialog", "Approximate time required", None))
        self.groupBox.setTitle(_translate("Dialog", "Input", None))
        self.label.setText(_translate("Dialog", "Length of Path(metres)", None))
        self.label_2.setText(_translate("Dialog", "Distance from building(metres)", None))
        self.label_3.setText(_translate("Dialog", "Percentage overlap of photos", None))
        self.label_4.setText(_translate("Dialog", "Approximate time for one photo(seconds)", None))

