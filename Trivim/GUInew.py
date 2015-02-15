
##from Tkinter import *
##import tkMessageBox
##import tkFont
import guidatabase
import sqlite3
import os
from os.path import expanduser
import Segmentation as seg
import numpy as np



Database_gui=guidatabase.Ui_Dialog()
##line=""
class Application(Frame):


    def __init__(self,master):
        
##        Frame.__init__(self,master)
        self.home = expanduser("~")
        self.trivim_home= open(os.path.join(self.home,"Trivim.txt"),'r').readline()
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):

        #label1(Main Heading)
##        self.customFont = tkFont.Font(size=16)
##        self.label1 = Label(self,text = "ENTER DETAILS", font=self.customFont, height=4)
##        self.label1.grid(row = 0, column = 6, columnspan =3, sticky = N)

##        #label2(Name)
##        self.customFont = tkFont.Font(size=12)
##        self.label2 = Label(self,text = "NAME", font=self.customFont, height=1)
##        self.label2.grid(row=4, column = 0, columnspan =2, sticky = W)

        #TextField1(Name)
##        self.Entry1 = Entry(self)
##        self.Entry1.grid(row= 4,column=6, columnspan =2, sticky = E)
        fw = open(os.path.join(self.trivim_home,'curr_proj.txt'),'r')
        pathDir = fw.readline()
        fw.close()
        os.chdir(pathDir)
        pathDir=os.getcwd()
        paths = pathDir.split('\\')
        index=len(paths)-1
        projName ='column'+'.txt'
                        
        fw=open(projName,'r')
        global line
        line = fw.readlines()
        

        
        i=0
        

        
        self.a=line
        while(i<len(line)):
            value=int(guidatabase.plainTextEdit.toPlainText())
            
##            self.a[i]= Label(self, text=line[i].upper(), font=self.customFont, height=2)
##            self.a[i].grid(row=(26+4*i), column=0, columnspan=2, sticky=W)
##            
##            self.a[i] = Entry(self)
##            self.a[i].grid(row= (26+4*i),column=6, columnspan =2, sticky = W)
##            i+=1
            
        print self.a  
        
        

        #create button
        
##        self.button1= Button(self, font=self.customFont, height=2)
##        self.button1.grid(row = 100, column=2, columnspan= 3, sticky = W)
##        self.button1["text"] = "SUBMIT"
##        self.button1["command"] = self.DatabaseValue

    def DatabaseValue(self):

            database = [self.Entry1.get()+"\n"]
            for i in range(0,len(line)):
                print self.a[i].get()
                database.append(self.a[i].get()+"\n")
            with open("tempGUI.txt",'w') as data:
                    data.writelines(database)
            tkMessageBox.showinfo("Message", "Value saved successfully")
            self.master.destroy()
    

        
        

    def placemark(self,values,lat,longi,altitude): #values is a list of values to be filled in the placemark file
        
        f = open('First.txt','rb')
        linesCol = f.readlines()
        totalLength = len(linesCol)
        f.close()

        f = open('Placemark.kml','r') #reading from the previously created Placemark file
        lines = f.readlines()
        temp = len(lines)
        f.close()
        fw = open('temp.kml','w')
    
        '''Based on the assumption that user-defined attributes does not contain
        Name and values[0] is always the name of the building
        and after that are the other attributes'''
    
        for i in range(temp-2):
            fw.writelines(lines[i])
        
        fw.writelines('<Placemark>\n\
            <name>'+values[0]+'</name>\n\
            <ExtendedData>')
        for i in range(totalLength):
            fw.writelines('<Data name="'+(linesCol[i])[:-2]+'">\n\
                <value>'+values[i+1]+'</value>\n\
              </Data>')
        fw.writelines('</ExtendedData>\n\
            <Point>\n\
              <coordinates>'+lat+','+longi+','+altitude+'</coordinates>\n\
                  <altitudeMode>relativeToGround</altitudeMode>\n\
                  <extrude>1</extrude>\n\
            </Point>\n\
        </Placemark>\n')

        fw.writelines((lines[temp-2]))
        fw.writelines((lines[temp-1]))
        fw.close()
        os.remove('Placemark.kml')
        os.rename('temp.kml','Placemark.kml')
def main():
    root=
    app = Application(root)
    root.mainloop()
         
