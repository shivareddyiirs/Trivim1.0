# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Database_query.ui'
#
# Created: Thu Nov 20 13:55:37 2014
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
        Dialog.resize(744, 623)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../bin_31/bin/isro.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(40, 20, 671, 581))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.buttonBox = QtGui.QDialogButtonBox(self.groupBox)
        self.buttonBox.setGeometry(QtCore.QRect(320, 540, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.listWidget = QtGui.QListWidget(self.groupBox)
        self.listWidget.setEnabled(False)
        self.listWidget.setGeometry(QtCore.QRect(20, 100, 251, 411))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 40, 251, 61))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(350, 100, 251, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setGeometry(QtCore.QRect(350, 120, 241, 31))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(424, 160, 81, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(350, 190, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 460, 111, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 530, 251, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.listWidget_2 = QtGui.QListWidget(self.groupBox)
        self.listWidget_2.setGeometry(QtCore.QRect(350, 220, 256, 192))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Trivim", None))
        self.groupBox.setTitle(_translate("Dialog", "Database Query", None))
        self.label.setText(_translate("Dialog", " Names of columns/attributes in Database for Query", None))
        self.label_2.setText(_translate("Dialog", "Enter Query(e.g. name = \'build1_1\' and area >50)", None))
        self.pushButton.setText(_translate("Dialog", "Submit Query", None))
        self.label_3.setText(_translate("Dialog", "Result", None))
        self.pushButton_2.setText(_translate("Dialog", "Save Query Results", None))
        self.pushButton_3.setText(_translate("Dialog", "Load attributes", None))

