# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoadKMLui.ui'
#
# Created: Sat Nov 29 13:04:29 2014
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
        
    def setupUi(self, Dialog,buildings):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        font = QtGui.QFont()
        font.setPointSize(14)
        Dialog.setFont(font)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setStyleSheet(_fromUtf8("font: 75 14pt \"Times New Roman\";\n""color: rgb(0, 0, 0);"))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.layout= QtGui.QVBoxLayout(Dialog)
        self.buttons = []
        for building in buildings:
            print "creating one new button"
            buttonObj=QtGui.QPushButton(_fromUtf8("Click to Load Footprint of "+ building), Dialog)
            buttonObj.setStyleSheet(_fromUtf8("font: 75 14pt \"Times New Roman\";\n""color: rgb(0, 0, 0);"))
            buttonObj.setGeometry(QtCore.QRect(20, 210, 341, 31))
            #self.buttons.append(QtGui.QPushButton(_fromUtf8("Click to Load footprint of "+ building), Dialog))
            self.buttons.append(buttonObj)
            self.layout.addWidget(self.buttons[-1])
        self.layout.addWidget(self.buttonBox)
        Dialog.setLayout(self.layout)        
        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Import Footprints", None))
        

