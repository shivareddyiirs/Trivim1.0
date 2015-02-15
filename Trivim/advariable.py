import sqlite3
from PyQt4 import *
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication,QFrame,QMainWindow
from advar import Ui_Dialog
import sys
import os

class Advariable :
    count=0
    advar_param=Ui_Dialog()

    def addvariable(self):
        varname=self.advar_param.plainTextEdit.toPlainText()
        self.advar_param.listWidget.addItem(varname)
        if self.advar_param.radioButton.isChecked():
            vartype= self.advar_param.radioButton.text()
            self.advar_param.listWidget_2.addItem(vartype)

        if self.advar_param.radioButton_2.isChecked():
            vartype= self.advar_param.radioButton_2.text()
            self.advar_param.listWidget_2.addItem(vartype)
        return

    def removevariable(self):
        item = self.advar_param.listWidget.takeItem((self.advar_param.listWidget.currentRow()))
        item = None
        self.advar_param.listWidget_2.clear()                                           
                                                      
        return

    def run(self,projectDir,call):
        print projectDir
        self.advar_param.setupUi(call)
        call.connect(self.advar_param.pushButton,QtCore.SIGNAL("clicked()"),self.addvariable)
        call.connect(self.advar_param.pushButton_2,QtCore.SIGNAL("clicked()"),self.removevariable)
        call.exec_()
        print "a"
        projName=os.path.join(projectDir,"column.txt")
        dataFile=os.path.join(projectDir,"dataType.txt")
        pathData = projectDir.split('/')
        paths = projectDir.split('/')
        index=len(paths)-1
        fw=open(projName,'w')
        fd=open(dataFile,'w')
        index=len(pathData)-1
        databaseName = pathData[index] + '.db'
        conn = sqlite3.connect(databaseName, detect_types=sqlite3.PARSE_COLNAMES )
        dbcursor = conn.cursor()    
        print "b"
        count=self.advar_param.listWidget.count()

        for i in range(count):
            try:
                dbcursor.execute('''ALTER TABLE information ADD COLUMN '''+str(self.advar_param.listWidget.item(i).text())+" "+str(self.advar_param.listWidget_2.item(i).text()))

            except :
                print 
            fw.write(str(self.advar_param.listWidget.item(i).text()+"\n"))
            fd.write(str(self.advar_param.listWidget_2.item(i).text()+"\n"))
        fw.close()
        fd.close()
        dbcursor.close()
        conn.close()










