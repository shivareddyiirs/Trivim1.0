import sqlite3
from PyQt4 import *
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication,QFrame,QMainWindow
from advar import Ui_Dialog
import sys
import database_enter
import os
import wx
from Tkinter import *



app = QApplication(sys.argv)
call=QtGui.QDialog()
window = QFrame()
print "as"




def run(projectDir):
    print projectDir    
    advar_param=Ui_Dialog()
    advar_param.setupUi(call)
    call.exec_()
    return True
    
    call.connect(advar_param.pushButton,QtCore.SIGNAL("clicked()"),add)    
    #call.connect(advar_param.pushButton,QtCore.SIGNAL("clicked()"),remove)
    
    
def add():
    print "a"
    varName=
    call=QtGui.QDialog()
    print "aaa"
    advar_param.plainTextEdit.setPlainText("try")
    f1.write(a)
    print "after f1"

    

#def remove():
    

print "before call"
run("Trivium")
app.exec_()
