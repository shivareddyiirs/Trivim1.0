# -*- coding: cp1252 -*-
#from Trivim import Ui_MainWindow
from Flowchart import Ui_ProcessFlow
import os
import urlparse
import numpy as np
from os.path import expanduser
home = expanduser("~")
wrk_drr=os.path.dirname(os.path.realpath(__file__))
os.chdir(wrk_drr)
try:
    with open(os.path.join(home,"Trivim.txt"),'w')as f:
        f.write(wrk_drr)
except:
    print "error"
import georef
import GeoImageCoor
import transimage
import transformations
import foot_auto
from PyQt4 import *
from PyQt4.QtGui import QApplication,QFrame,QMainWindow,QGraphicsScene,QPixmap, QMessageBox
import sys
#from Flowchart import Ui_ProcessFlow
from PyQt4 import QtCore
import cam_calib
import Field_Planning
import Height_Extraction
import Point_cloud_generation
import Database_query
import seg_n_mask1
import threeD_model_gen
from Tkinter import *
import tkFileDialog
from advariable import Advariable
import getopt
import run_calib
from glob import glob
#import win32api
import subprocess
import gps
import name
import RunBundler
import RunCMVS
import sqlite3
import shutil
#import RunPMVS
import thread
import threading
import addPlacemark_new
import database_enter
import DemoDatabase
import sqlite3
import Utm_height
import Segmentation as seg
from PIL import Image
##import canny_main
import zipfile
import GUI
import LoadKML
import mask
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QApplication
import sys
import testpycollada

print "application starting"
image_file=""
seg_image=""

#make objects of ui classes
ui = Ui_ProcessFlow()
cameraCalib=cam_calib.Ui_Dialog()
threeD=threeD_model_gen.Ui_Dialog()
Point_param=Point_cloud_generation.Ui_Dialog()
field_param=Field_Planning.Ui_Dialog()
Height_param=Height_Extraction.Ui_Dialog()
Database_param=Database_query.Ui_Dialog()
seg_param=seg_n_mask1.Ui_Dialog()
loadKML= LoadKML.Ui_Dialog()
segtest= mask.Ui_Dialog()
currentBuilding=""


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
app = QApplication(sys.argv)
projPath=""
#myapp = QFrame()
trivim = Ui_ProcessFlow()
window = QFrame()
path_calib= ""
buildings=[]
current_project = ""
current="NIL"
a=""
coordPath=""
testpath=""
status= int(1)
calib_flag= 0
def enableButtonsLoad():
    global status
    print "status is", status
    if status == 0 :
        return
    elif status >= 1:
        print "enabling caliberation"
        ui.pushButton_8.setEnabled(True)
        ui.pushButton_9.setEnabled(True)
        #ui.pushButton_8.setStyleSheet(_fromUtf8("color: rgb(0, 170,255);\n""font: 14pt \"Times New Roman\";"))
        if  status >= 2:
            ui.pushButton_8.setStyleSheet(_fromUtf8("color: rgb(0, 170,255);\n""font: 14pt \"Times New Roman\";"))
            ui.pushButton_9.setEnabled(True)
            ui.pushButton_9.setStyleSheet(_fromUtf8("color: rgb(0, 170,255);\n""font: 14pt \"Times New Roman\";"))
            ui.pushButton_10.setEnabled (True)
            ui.pushButton_10.setStyleSheet(_fromUtf8("color: rgb(0, 170,255);\n""font: 14pt \"Times New Roman\";"))
            if status >=3:
                ui.pushButton_11.setEnabled(True)
                ui.pushButton_11.setStyleSheet(_fromUtf8("color: rgb(0, 170,255);\n""font: 14pt \"Times New Roman\";"))
                if status >= 4 :
##                    ui.pushButton_12.setEnabled(False)
##                    ui.pushButton_12.setStyleSheet(_fromUtf8("color: rgb(0, 170,255);\n""font: 14pt \"Times New Roman\";"))
                    if status >=5:
                        ui.pushButton_13.setEnabled(True)
                        ui.pushButton_13.setStyleSheet(_fromUtf8("color: rgb(0, 170,255);\n""font: 14pt \"Times New Roman\";"))
                        if status >= 6:
                            ui.pushButton.setEnabled(True)
                            ui.pushButton.setStyleSheet(_fromUtf8("color: rgb(0, 170,255);\n""font: 14pt \"Times New Roman\";"))
def enableButtons():
    global status
    print "status is", status
    if status == 0 :
        return
    elif status >= 1:
        print "enabling caliberation"
        ui.pushButton_8.setEnabled(True)
        ui.pushButton_9.setEnabled(True)
        if  status >= 2:
            ui.pushButton_9.setEnabled(True)
            ui.pushButton_10.setEnabled (True)
            if status >=3:
                ui.pushButton_11.setEnabled(True)
                if status >= 4 :
                    #ui.pushButton_12.setEnabled(True)
                    if status >=5:
                        ui.pushButton_13.setEnabled(True)
                        if status >= 6:
                            ui.pushButton.setEnabled(True)
            
def newProjClicked():
        cProjFile=open(os.path.join(wrk_drr,'curr_proj.txt'),'w')
        cProjFile.write("")
        cProjFile.close()
        ui.pushButton_3.setEnabled(False)
        dialog = QtGui.QFileDialog(None,"Create Project Folder")
        dialog.setFileMode(QtGui.QFileDialog.Directory)
        dialog.setDirectory(wrk_drr)
        dialog.setOption(QtGui.QFileDialog.ShowDirsOnly)
        teste=dialog.exec_()
        print "test", teste
        try:
            directoryPath=str(dialog.selectedFiles()[0])
            
        except:
            print"no file choosen"
            return False
        call=QtGui.QDialog()
        global projPath
        projPath=str(directoryPath)
        cProjFile=open(os.path.join(wrk_drr,'curr_proj.txt'),'w')
        cProjFile.write(projPath)
        cProjFile.close()
        if teste!=0:           
            DemoDatabase.run(projPath)
            ad= Advariable()
            ad.run(projPath,call)
            status=1
            with open(os.path.join(projPath,'status.txt'),'w')as f :
                f.write('%d' % status)
            try:
                os.mkdir(projPath+"\\"+"input")
                os.mkdir(projPath+"\\"+"output")
                os.mkdir(projPath+"\\"+"Height")
                
            except :
                print("already exist")
            enableButtons()
##            ui.pushButton_8.setEnabled(True)
            ui.pushButton_2.setStyleSheet(_fromUtf8("color: rgb(0, 85,0);\n""font: 14pt \"Times New Roman\";"))
        else:
            print "Project Not Created"
        return True
def loadProjClicked():
        ui.pushButton_2.setEnabled(False)
        dialog = QtGui.QFileDialog(None,"Select Project Folder")
        dialog.setFileMode(QtGui.QFileDialog.Directory)
        dialog.setDirectory(wrk_drr)
        dialog.setOption(QtGui.QFileDialog.ShowDirsOnly)
        teste=dialog.exec_()
        if teste!=0:
            try:
                global current_project
                current_project = str(dialog.selectedFiles()[0])
            except:
                print("no project choosen")
                return False
            cProjFile=open(os.path.join(wrk_drr,'curr_proj.txt'),'w')
            cProjFile.write(current_project)
            cProjFile.close()
            global projPath
            projPath=current_project
            ui.pushButton_3.setStyleSheet(_fromUtf8("color: rgb(0, 85,0);\n""font: 14pt \"Times New Roman\";"))
            try:
                fread= open(os.path.join(projPath,"status.txt"),'r')
                global status
                status= int(fread.read())
                fread.close()
            except:
                with open(os.path.join(projPath,'status.txt'),'w')as f :
                    f.write('%d' % status)
                print "status file not found"
            enableButtonsLoad()# check previous status of the project and enable buttons accordingly
        else:
            print "Project Not Chosen"
        return True
    
def browseClicked(): # browseClicked in chessboard
    cameraCalib.plainTextEdit.setPlainText("")
    dialog = QtGui.QFileDialog(None,"Select Image Directory")
    dialog.setFileMode(QtGui.QFileDialog.Directory)
    dialog.setDirectory(wrk_drr)
    dialog.setOption(QtGui.QFileDialog.ShowDirsOnly)
    dialog.exec_()
    global path_calib
    try:
        path_calib= str(dialog.selectedFiles()[0])
        cameraCalib.plainTextEdit_3.setPlainText(path_calib)
    except:
        print "no image directory choosen"
        return False
    os.chdir(path_calib)
    fi_name= glob("*.JPG")
    try:
        graypath= os.path.join(projPath,"gry")
        os.makedirs(graypath)
        print "directory created"
        for fi in fi_name:
            print fi
            img = Image.open(fi).convert("L")
            print "image converted"
            img.save(os.path.join(graypath,fi))
            print "file saved"
        path_calib = graypath
    except:
        print("Can not convert to gray")
    
def checkGeotag():
        os.chdir(projPath)
        print coordPath
        fo=open(coordPath,'r')
        flag=0
        for lines in fo:
            if(flag>0):
                coordline=len(lines)
                coords=lines.split()
                xc=coords[0]
                yc=coords[1]
                zc=coords[2]
                if(xc!='none' and yc!='none' and zc!='none'):
                    print "Images are geotagged"
                    break;
                else:
                    print "Images are not geotagged"
                    os.chdir(wrk_drr)
                    subprocess.call(['python','GeotagFrame.py'])
                    break;
            flag=flag+1
        return False

def browseClickHeight():
    dialog = QtGui.QFileDialog(None,"Select PointCloud File")
    dialog.setDirectory(wrk_drr)
    dialog.exec_()
    path_point=""
    try:
        path_point=dialog.selectedFiles()[0]
    except:
        print "point cloud folder not choosen"
        return False
    Height_param.plainTextEdit.setPlainText(path_point)
    Height_param.pushButton_2.setEnabled(True)
    return True
def guiCall():
    print "gui"
    GUI.main()
    
    mask= np.genfromtxt(os.path.join(projPath,'mask.txt'),'float')
    print mask
   
    main_directory= os.path.join(projPath,"input")
##        with open(os.path.join(projPath,'tempGUI.txt'))as datafile:
##            database= datafile.readlines()
    datafile= os.path.join(projPath,'tempGUI.txt')
    with open(datafile,'r') as data :
        filename= data.readline()[:-1]
    print filename
    seg.crop_image(seg_image,mask,datafile,filename,main_directory)
    global image_file
    print "image_file",image_file
    x=os.path.splitext(os.path.basename(urlparse.urlsplit(image_file).path))
    picname=x[0]
    transimage.run(mask,filename,projPath,picname)
    
    heightDir=os.path.join(projPath,"Height")
 

    Utm_height.run(heightDir,main_directory)

    
                                            
def ShowImageSegNMask():

        global image_file
        print "image_file",image_file
        image_file = str(seg_param.comboBox.currentText())
        print "image_file",image_file
        label2 = seg_param.label_2
        pixmap = QPixmap(image_file);
        pixmap1 = pixmap.scaled(label2.size(),QtCore.Qt.KeepAspectRatio);
        label2.setPixmap(pixmap1)
        seg_param.pushButton_4.setEnabled(True)
        return True
            
def browseClickedPointCloud(): # browseClicked in pointcloud
    dialog = QtGui.QFileDialog(None,"Select Image Directory")
    dialog.setFileMode(QtGui.QFileDialog.Directory)
    dialog.setDirectory(wrk_drr)
    dialog.setOption(QtGui.QFileDialog.ShowDirsOnly)
    dialog.exec_()
    global path_image
    path_image=dialog.selectedFiles()[0]
    Point_param.plainTextEdit.setPlainText(path_image)
    Point_param.pushButton_3.setEnabled(True)
    return True
   
def generatePointCloudClicked():
    Point_param.pushButton.setEnabled(True)
    os.chdir(wrk_drr)

    print "current working directory is", wrk_drr
    bundlerPath=""
    path_image= str(Point_param.plainTextEdit.toPlainText())
    print "image path is",path_image
    newPhotoPath=r"point_cloud/temp/"
    
    if not(os.path.isdir(path_image)):
        print("choose correct directory")
       # win32api.MessageBox(0,"Invalid Path, Please choose Correct Directory","Warning")
    else:
        p=os.listdir(newPhotoPath)
        for i in p:
            os.remove(newPhotoPath+i)
        f=os.listdir(path_image)
        for i in f:
            a=i.split('.')
            flag=0
##            try:
##                Image.open(os.path.join(path_image,i))
##            except:
##                flag=1
##                print "can not open image"
            if (a[len(a)-1]=="jpg" or a[len(a)-1]=="JPG")and flag==0:
                shutil.copy(os.path.join(path_image,i),newPhotoPath)
                print "copying photo"
        gps.run(projPath,[newPhotoPath ,os.path.join(projPath,"coordinates.txt")])# photo directory along with coordinates is passed to it
        #checkGeotag()
        a=[os.path.join(wrk_drr,newPhotoPath)]
        name.run(a)
        os.chdir(wrk_drr)
        a=[bundlerPath , "--photos=" + os.path.join(wrk_drr,newPhotoPath)]
##        thread.start_new_thread(RunBundler.run,(a,))
        with open(r"osmbundler/curr_proj.txt",'w') as proj :
            proj.write(projPath)
        RunBundler.run(a)
        print "in point cloud before georeference"
##to run PMVS
        
##        bundlerOutputPath=os.path.join(projPath,"PointCloud")
##        print "bundlerOutputPath"
##        print bundlerOutputPath
##        
##        if not (os.path.isdir(bundlerOutputPath)):
##            print("enter correct path")
##           # win32api.MessageBox(0,'Invalid path. Enter the correct path','Warning')
##        else:
##            a=['--bundlerOutputPath='+bundlerOutputPath]
##            RunPMVS.run(a)
####            thread.start_new_thread( RunPMVS.run,(a,) )
##        print "step 1 ends"
        Point_param.pushButton_3.setStyleSheet(_fromUtf8("color: rgb(0, 85,0);\n""font: 10pt \"Times New Roman\";"))
        Point_param.pushButton.setEnabled(True)
        return True
      
def georeference():
        pointcloudpath=os.path.join(projPath,"PointCloud")
        cooradd= os.path.join(projPath,"coordinates.txt")
        with open(cooradd) as codad:
            if codad.readlines()[1].split(" ")[0] != "none" :
                georef.run(pointcloudpath,cooradd,os.path.join(pointcloudpath,"georeffile.txt"))
                GeoImageCoor.run(pointcloudpath,os.path.join(pointcloudpath,"georeffile.txt"))
            else :
                cooradd=browseCoordinates()
                georef.run(pointcloudpath,cooradd,os.path.join(pointcloudpath,"georeffile.txt"))
                GeoImageCoor.run(pointcloudpath,os.path.join(pointcloudpath,"georeffile.txt"))
        Point_param.pushButton.setStyleSheet(_fromUtf8("color: rgb(0, 85,0);\n""font: 10pt \"Times New Roman\";"))
        return True
    
    
def calculateParameterClicked():
    
    cameraCalib.pushButton.setEnabled(False)
    sensor_name= cameraCalib.comboBox.currentText()
    #cameraCalib.plainTextEdit.setPlainText("Camera Parameters....")
    cameraCalib.pushButton.setText("Calculating")
    print "Changing name"
    with open(os.path.join(wrk_drr,r'camera_calibration\sensor_value.txt'), 'w') as myFile:
            myFile.write(sensor_name)
    global calib_flag
    if calib_flag==0:
        global path_calib
        with open(os.path.join(wrk_drr,'camera_calibration\\path.txt'), 'w') as myFile:
            myFile.write(path_calib)

        f = open(os.path.join(wrk_drr,r"camera_calibration\\path.txt"),"r")
        path=f.read()+ "\\*.jpg"
        args, img_mask = getopt.getopt(sys.argv[1:], '', ['save=', 'debug=', 'square_size='])
        args = dict(args)
        try: img_mask = img_mask[0]
        except: img_mask = path
        img_names = glob(img_mask)
        #calib_flag=1
        value_calib=len(img_names)
        print value_calib
##        a1=threading.Thread(None,run_calib.run(''))
##        a1.start()
##        a1.join()
        run_calib.run("")
        cameraCalibRes=open(os.path.join(wrk_drr,r'camera_calibration\calib_temp.txt'),'r')
        cameraCalib.plainTextEdit.setPlainText("Camera Parameters....")
        for lines in cameraCalibRes:
            lineRes=lines.replace("\n","")
            cameraCalib.plainTextEdit.appendPlainText(lineRes)
        cameraCalibRes.close()
        cameraCalib.pushButton.setEnabled(True)
        cameraCalib.pushButton.setText("Recalculate Parameters")
        return True



def OnCalcNumPhotos():
        f=open(os.path.join(wrk_drr,r'camera_calibration\calib_temp.txt'),'r')
##        numerator=int(field_param.plainTextEdit.toPlainText())
##        denominator=int(field_param.plainTextEdit_2.toPlainText())
        
        for i in range(2):
            a=f.readline()
        try:
            b=a.split(' ')
            ccd=float(b[3])
        except:
            print("provide senser width")
           # win32api.MessageBox("Sensor width could not be obtained. Make sure to calculate or load camera parameters before proceeding further.")

        for i in range(7):
            a=f.readline()

        try:
            b=a.split(' ')
            focalLength=float(b[3])
        except:
            print("provide focal length")
            #win32api.MessageBox("Focal length could not be obtained. Make sure to calculate or load camera parameters before proceeding further.")
        numerator=  (float(field_param.plainTextEdit.toPlainText())*focalLength)/( ccd*float(field_param.plainTextEdit_2.toPlainText()) )
        denominator=(1-float(field_param.comboBox.currentText())/100)
##        if int(field_param.plainTextEdit.toPlainText())==0 or int(field_param.plainTextEdit_2.toPlainText())==0:
##            #win32api.MessageBox('Path Length and Distance from building should be positive','Error')
##            numerator=  (float(field_param.plainTextEdit.toPlainText())*focalLength)/( ccd*float(field_param.plainTextEdit_2.toPlainText()) )
##            denominator=(1-float(field_param.comboBox.currentText())/100)
        if (numerator-1)/denominator >= 0:
            number=float( (numerator-1)/denominator+1 )
            field_param.plainTextEdit_5.setPlainText( str(int(number)) )
            time=int(float(field_param.plainTextEdit_4.toPlainText())*float(number))
            hours=int(time/3600)
            minutes=int( (time-hours*3600)/60 )
            seconds=int( time-minutes*60-hours*3600 )
            field_param.plainTextEdit_6.setPlainText( str(hours)+"h:"+str(minutes)+"m:"+str(seconds)+"s" )
        else:
            field_param.plainTextEdit_5.setPlainText(str(1))
        
def RepresentsInt(s):
        try: 
            float(s)
        except ValueError:
            return False
        return True

def addNewCameraClicked():
    camName=cameraCalib.plainTextEdit_2.toPlainText()
    #sensorWidth=cameraCalib.plainTextEdit_4.toPlainText()
    if str(camName).strip(' ')!='':
            with open(os.path.join(wrk_drr,r'camera_calibration\camera_database.txt'),'a') as f:
                a=str(camName).strip(' ') 
                f.write('\n'+a)
                print a + " added to database"
                cameraCalib.comboBox.addItem(a)
                cameraCalib.comboBox.setItemText(0,a)
    else:
        #win32api.MessageBox(0,"Enter Valid Camera and Sensor width","Error")
        print("provide valid camera and senser width")

def loadCameraParameterClicked():
    cameraCalib.plainTextEdit.setPlainText("")
    dialog = QtGui.QFileDialog(None,"Choose Camera Parameters File")
    dialog.setFileMode(QtGui.QFileDialog.AnyFile)
    dialog.setDirectory(wrk_drr)
    dialog.exec_()
    camFile= dialog.selectedFiles()[0]
    try:
        with open(camFile,'r') as f:
            cameraCalib.plainTextEdit.setPlainText("Camera Parameters....")
            for lines in f:
                lineRes=lines.replace("\n","")
                cameraCalib.plainTextEdit.appendPlainText(lineRes)
            with open(r'camera_calibration\calib_temp.txt','a') as f2:
                for lines in f:
                    f2.write(lines)
    except:
        #win32api.MessageBox(0,"File load unsuccesful. Please try again.","Error")
            print "File load unsuccesful, try again"
def saveCameraParameterClicked():
    dialog = QtGui.QFileDialog()
    dialog.AcceptMode(QtGui.QFileDialog.AcceptSave)
    dialog.setDirectory(wrk_drr)
    filename=dialog.getSaveFileName(None,"Save File","",".txt")
    with open(str(filename),'w')as f:
                            try:
                                #shutil.copyfile(os.path.join(wrk_drr,r'camera_calibration\calib_temp.txt'),f);
                                f.writelines(str(cameraCalib.plainTextEdit.toPlainText()).split('\n')[1:])
                                #win32api.MessageBox(0,"Result stored in"+str(filename),"Success")
                            except:
                                print "file save error, try again"
                                #win32api.MessageBox(0,"File save unsuccesful. Please try again.","Error")

def footprintExtractionClicked():
    dialog = QtGui.QFileDialog(None,"Open GoogleEarth.exe")
    dialog.setFileMode(QtGui.QFileDialog.AnyFile)
    dialog.setDirectory(wrk_drr)
    dialog.exec_()
    googleEarthPath= dialog.selectedFiles()[0]
    os.startfile(googleEarthPath)


def browseKMLClicked():
    print currentBuilding
    dialog = QtGui.QFileDialog(None,"Choose KML File")
    dialog.setFileMode(QtGui.QFileDialog.ExistingFile)
    dialog.setDirectory(wrk_drr)
    dialog.setFilter('*.kml')
    dialog.exec_()
    kmlPath= dialog.selectedFiles()[0]
    building= os.path.basename(str(kmlPath)).split(".")[0]
    testpath=os.path.join(projPath,"input")+"\\"+building
    os.chdir(testpath)
    try:
        shutil.copyfile(str(kmlPath),building+".kml")
    except:
        print "copy failed"
    
    return True
def browseCoordinates():
    dialog = QtGui.QFileDialog(None,"Choose Coordinate file")
    dialog.setFileMode(QtGui.QFileDialog.ExistingFile)
    dialog.setDirectory(wrk_drr)
    dialog.setFilter('*.txt')
    dialog.exec_()
    coordPath= dialog.selectedFiles()[0]
##    testpath=os.path.join(projPath,"coordinates.txt")
##    shutil.copy(str(kmlPath),testpath)
    
    return str(coordPath)
def loadKMLClicked():
    buildFolderCheck=os.listdir(os.path.join(projPath,"input"))
    numBuild=len(buildFolderCheck)
    print "Number of Buildings =",numBuild
    call=QtGui.QDialog()
    loadKML.setupUi(call,buildFolderCheck)
    build_no = 0
    for building in buildFolderCheck :
        global currentBuilding
        currentBuilding = building
        call.connect(loadKML.buttons[build_no],QtCore.SIGNAL("clicked()"),browseKMLClicked)
        build_no = build_no + 1
        print "testing button linking",building
    call.exec_()
   # if call.exec_()==1:-----------------------error
    if call.result()==1:
        threeD.pushButton_6.setEnabled(True)
        threeD.pushButton_3.setStyleSheet(_fromUtf8("color: rgb(0, 85,0);\n""font: 14pt \"Times New Roman\";"))
    return True
    
    

def onExtractHeight():
    dialog = QtGui.QFileDialog(None,"Select Directory")
    dialog.setFileMode(QtGui.QFileDialog.Directory)
    dialog.setDirectory(wrk_drr)
    dialog.setOption(QtGui.QFileDialog.ShowDirsOnly)
    dialog.exec_()
    heightDir= str(dialog.selectedFiles()[0])
    print projPath
    a=projPath+"\input"
    print a
    b=[heightDir,a]
    print 'callin utm_height'
    Utm_height.run(b)
    Height_param.pushButton_3.setStyleSheet(_fromUtf8("color: rgb(0, 85,0);\n""font: 10pt \"Times New Roman\";"))
    return True

def footProcessClicked():
    inputPath=str(projPath+"\\"+"input")
    flag=1
    if(len(inputPath) != 0):
        os.chdir(wrk_drr+'\\3d-modelling')
        fw = open('temp.txt','w')
        s = inputPath.replace("\\", "\\\\" )
        fw.write(s)
        fw.close()
        flag=0
    else:
        flag=1
    if(flag!=1):
        os.chdir(os.path.join (wrk_drr,'3d-modelling'))
        f= open("temp.txt","r")
        l= f.readline()
        f.close()
        print l
        x=os.listdir(l)
        iterator=len(x)
        print "iterator",iterator
        for i in range(iterator):
            
            for files in os.listdir(os.path.join(l,x[i])):
               
                if files.endswith(".kml"):
                    print "writing next build", x[i]
                    f_name=files
                    os.chdir(os.path.join(wrk_drr,'3d-modelling'))
                    fw = open('temp.txt','w')
                    fw.write(l+'\\\\'+x[i]+'\n')
                    fw.close()
                    print "calling Foot auto"
                    import foot_auto
                    foot_auto.main()
                    print "foot auto called"
                else:
                    print "file not writen"
    return True

                    
def constructBuildingClicked():
    footProcessClicked();
    global draw_flag
    draw_flag=1
    inputPath=os.path.join(projPath,"input")
    outputPath=os.path.join(projPath,"output")
    flag = True

    files=os.listdir(inputPath)
    
   
    for filename in files:
        countJPG=0;
        hght=0.0;
        print "inside for loop",filename
        os.chdir(inputPath)
        if os.path.isdir(filename):
            print "inside first if"
            for files_build in os.listdir(os.path.join(inputPath,filename)):
                os.chdir(os.path.join(inputPath,filename))
                
                with open("heights.txt",'r')as ht:
                    print "ht is",ht
                    for lines in ht:
                        list_ht=lines.split("\t")
                    print "list_ht is",list_ht

                
                with open(filename+".txt") as fp:
                    
                    line= fp.readline()
                    list_co= line.split("\t")
                    x= list_co[1:9:2]
                    y= list_co[2:9:2]
                    
                   
                    import numpy as np
                    import math
                    import UTM as con             
                    x= np.array(x,float)
                    y= np.array(y,float)
                    print "x coordinates is", x
                    print "y coordinates is", y
                    (z, x[0], y[0]) = con.LLtoUTM(23,x[0],y[0])
                    (z, x[1], y[1]) = con.LLtoUTM(23,x[1],y[1])
                    (z, x[2], y[2]) = con.LLtoUTM(23,x[2],y[2])
                    (z, x[3], y[3]) = con.LLtoUTM(23,x[3],y[3])
                    x=x-x[0]
                    y=y-y[0]
                    print "x coordinates is", x
                    print "y coordinates is", y
                if files_build.endswith('.jpg'):
                    countJPG=countJPG+1;
                    outputFileName=files_build.split(".")[0]
                    print "inside if jpg","calling testpycollada",list_ht[countJPG]                    
                    testpycollada.makeKML(os.path.join(inputPath,filename),os.path.join(outputPath,outputFileName) ,files_build,list_ht[countJPG],hght,x,y,filename,inputPath);            
                    hght=hght+float(list_ht[countJPG])
                    print "height of floor is",outputFileName,hght
    threeD.pushButton_8.setEnabled(True)
    addPlacemark_new.main()
    print "\n\n\nEntering values in the database..  Wait\n"
    database_enter.run()
    print "\n All values have been added  move to the query section"
    threeD.pushButton_6.setStyleSheet(_fromUtf8("color: rgb(0, 85,0);\n""font: 14pt \"Times New Roman\";"))
    return True

def visGeoClicked():

    dirPathVis=projPath+"\\output"
    print dirPathVis
    os.chdir(dirPathVis)
    files=os.listdir(dirPathVis)
    newfiles= os.listdir(dirPathVis)
    for filename in newfiles:
        print filename
        base_file, ext = os.path.splitext(filename)
        if ext == ".kmz":
            os.startfile(filename)     
        
    os.startfile("Placemark.kml")
    threeD.pushButton_8.setStyleSheet(_fromUtf8("color: rgb(0, 85,0);\n""font: 14pt \"Times New Roman\";"))
    return True
def cameraCalibClicked():
    call=QtGui.QDialog()
    cameraCalib.setupUi(call)
    f=open(os.path.join(wrk_drr,"camera_calibration\camera_database.txt"),'r')
    file1=f.readlines()
    for line in file1 :
        cameraCalib.comboBox.addItem(line)
    #cameraCalib.progressBar.setProperty("value", 0)
    call.connect(cameraCalib.pushButton_5,QtCore.SIGNAL("clicked()"),browseClicked)
    call.connect(cameraCalib.pushButton,QtCore.SIGNAL("clicked()"),calculateParameterClicked)
    call.connect(cameraCalib.pushButton_2,QtCore.SIGNAL("clicked()"),addNewCameraClicked)
    call.connect(cameraCalib.pushButton_3,QtCore.SIGNAL("clicked()"),loadCameraParameterClicked)
    call.connect(cameraCalib.pushButton_4,QtCore.SIGNAL("clicked()"),saveCameraParameterClicked)
    call.exec_()
    if call.result()  == 1:
        print "updating status"
        global status
        status = 2
        enableButtons()
        ui.pushButton_8.setStyleSheet(_fromUtf8("color: rgb(0, 85,0);\n""font: 14pt \"Times New Roman\";"))

def fieldPlanningClicked():
            call=QtGui.QDialog()
            field_param.setupUi(call)
            field_param.comboBox.addItem('60')
            field_param.comboBox.addItem('70')
            field_param.comboBox.addItem('80')
            field_param.comboBox.addItem('90')
            field_param.comboBox.addItem('100')
            call.connect(field_param.pushButton,QtCore.SIGNAL("clicked()"),OnCalcNumPhotos)
            call.exec_()
            if call.result()==1:
                ui.pushButton_9.setStyleSheet(_fromUtf8("color: rgb(0, 85,0);\n""font: 14pt \"Times New Roman\";"))
            return True
        
def threedModelClicked():
            call=QtGui.QDialog()
            threeD.setupUi(call)
            #call.connect(threeD.pushButton,QtCore.SIGNAL("clicked()"),addNewBuildingClicked)
            call.connect(threeD.pushButton_3,QtCore.SIGNAL("clicked()"),loadKMLClicked)
            call.connect(threeD.pushButton_6,QtCore.SIGNAL("clicked()"),constructBuildingClicked)
            call.connect(threeD.pushButton_8,QtCore.SIGNAL("clicked()"),visGeoClicked)
            call.exec_()
            if call.result()  == 1:#check if okay pressed and update
                global status
                status = 6
                with open(os.path.join(projPath,'status.txt'),'w')as f :
                    f.write('%d' % status)
                enableButtons()          
                ui.pushButton_13.setStyleSheet(_fromUtf8("color: rgb(0, 85,0);\n""font: 14pt \"Times New Roman\";"))
            return True
def onSaveQueryResults():
            root = Tk()
            root.withdraw()
            global current
            filename = tkFileDialog.asksaveasfilename(parent=root,initialfile="QueryResults",initialdir=current,defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
            print filename
            try:
                count = Database_param.listWidget_2.count()
                print count
                strings=[]
                with open(filename,'w') as f:
                    for i in range(count):
                        strings.append(str(Database_param.listWidget_2.item(i).text()))
                    print strings
                    for string in strings:
                        f.write( str(string) + "\n" )
            except:
                print"file save failed, try again"
            return True
def onloadattributes():
            Database_param.listWidget.setEnabled(True)
            Database_param.listWidget.clear()
            
            os.chdir(projPath)
            f = open(r'column.txt','r')
            names = f.readlines()
            print "names", names
            f.close()
        
            Database_param.listWidget.addItem('name(string)')
            Database_param.listWidget.addItem('latitude(string)')
            Database_param.listWidget.addItem('longitude(string)')
            Database_param.listWidget.addItem('alititude(float)')
        
            for name in names:
                print "appending name", name
                Database_param.listWidget.addItem(name.replace("\n",""))

            Database_param.listWidget.setEnabled(False)
            return True

def submitqueryclick():         
        Database_param.listWidget_2.clear() #output screen cleared
        q=""
        q=str(Database_param.plainTextEdit.toPlainText())
        print q    #stores input query
        print "inside submit after store input query "
        
        pathData = projPath.split('/')
        index=len(pathData)-1
        databaseName = pathData[index] + '.db'
        print databaseName
        try:
            conn = sqlite3.connect(databaseName)
            print "connection done"
            dbcursor = conn.cursor()
            print "dbcursor created"
            
            result=dbcursor.execute("SELECT * FROM information where "+q)
            print "query fired"
            print result
        
            count=0
            for row in result:
                count=0
                print "length of row", len(row)
                for item in row:
                    print item
                    Database_param.listWidget_2.addItem(str(Database_param.listWidget.item(count).text()) + " : " + str(item))
                    count+=1
                    print "adding results"
                Database_param.listWidget_2.addItem(" ")
        except :
            print "error in database "
        return True

def OnProceedButton():##segmentation
        global seg_image
        seg_image= os.path.join(wrk_drr,'pic_resize.jpg')
        shutil.copy(image_file,seg_image)
        
        call=QtGui.QDialog()
        segtest.setupUi(call)
        
        segtest.pushButton.setEnabled(True)
        
        call.connect(segtest.pushButton,QtCore.SIGNAL("clicked()"),guiCall)
        
        call.exec_()
        
            
def dQueryClicked():
            call=QtGui.QDialog()
            #Database_param=Database_query.Ui_Dialog()
            Database_param.setupUi(call)
            call.connect(Database_param.pushButton_2,QtCore.SIGNAL("clicked()"),onSaveQueryResults)
            call.connect(Database_param.pushButton_3,QtCore.SIGNAL("clicked()"),onloadattributes)
            call.connect(Database_param.pushButton,QtCore.SIGNAL("clicked()"),submitqueryclick)
            
            call.exec_()
            if call.result()  == 1:#check if okay pressed and update
                global status
                status = 6
                with open(os.path.join(projPath,'status.txt'),'w')as f :
                    f.write('%d' % status)
                enableButtons()
                ui.pushButton.setStyleSheet(_fromUtf8("color: rgb(0, 85,0);\n""font: 14pt \"Times New Roman\";"))
            return True
            

def sandMClicked():
            call=QtGui.QDialog()
            
            seg_param.setupUi(call)
            pcPath=os.path.join(projPath, "PointCloud/*.jpg")
            imageFiles=glob(pcPath)
            for images in imageFiles :
                #print images
                #index=len(images.split('\\'))
                seg_param.comboBox.addItem(images)
            
            #call.connect(seg_param.pushButton,QtCore.SIGNAL("clicked()"),browseClickSegNMask)
            #index
            
            call.connect(seg_param.pushButton,QtCore.SIGNAL("clicked()"),ShowImageSegNMask)
            
            call.connect(seg_param.pushButton_4,QtCore.SIGNAL("clicked()"),OnProceedButton)
            call.exec_()
            if call.result()  == 1:#check if okay pressed and update
                global status
                status = 5
                with open(os.path.join(projPath,'status.txt'),'w')as f :
                    f.write('%d' % status)
                enableButtons()
                ui.pushButton_11.setStyleSheet(_fromUtf8("color: rgb(0, 85,0);\n""font: 14pt \"Times New Roman\";"))
            return True
            
def pointCloudClicked():
            call=QtGui.QDialog()
            Point_param.setupUi(call)
            call.connect(Point_param.pushButton_2,QtCore.SIGNAL("clicked()"),browseClickedPointCloud)
            Point_param.pushButton_3.setEnabled(True)
            call.connect(Point_param.pushButton_3,QtCore.SIGNAL("clicked()"),generatePointCloudClicked)
            call.connect(Point_param.pushButton,QtCore.SIGNAL("clicked()"),georeference)
            Point_param.pushButton.setEnabled(True)
            #Point_param.plainTextEdit.setPlainText(path_calib)
            call.exec_()
            #ui.pushButton_11.setEnabled(True)
            if call.result()  == 1:#check if okay pressed and update
                global status
                status = 3
                with open(os.path.join(projPath,'status.txt'),'w')as f :
                    f.write('%d' % status)
                enableButtons()
                ui.pushButton_10.setStyleSheet(_fromUtf8("color: rgb(0, 85,0);\n""font: 14pt \"Times New Roman\";"))
            return True
def helpClicked():

    os.startfile(os.path.join(wrk_drr,"InstallationandUserManuals/COMPLETE_DOCUMENTATION.pdf"))
    return True
def aboutClicked():
    print "aboutClicked"
    msg=str("Trivim 1.0\n\nTrivim (alpha) is an open source application for generating 3D-Street Model. The application generates photorealistic georeferenced 3D Street Model using photogrammetric processing of overlapping 2D images.\n\nTechnical Advisors: Dr. Y.V.N.Krishnamurthy, Mr. P.L.N. Raju, Ms. Shefali Agrawal\n\nTeam: Dr. Poonam S Tiwari, Dr. Hina Pande, Mr. S. Raghavendra, Mr. K. Shiva Reddy,\n           Mr. Mayank Sharma, BITS Interns (2013,2014), Ms. Shweta Beniwal\n\n\n© IIRS, 2014")
    msgBox=QMessageBox()
    msgBox.setText(msg)
    msgBox.setWindowTitle("About Trivim")
    msgBox.exec_()
    return True

trivim.setupUi(window)
ui.setupUi(window)
ui.pushButton.setEnabled(True)
ui.pushButton_8.setEnabled(False)
ui.pushButton_9.setEnabled(False)
ui.pushButton_13.setEnabled(False)
ui.pushButton.setEnabled(False)
##ui.pushButton_12.setEnabled(False)
ui.pushButton_11.setEnabled(False)
ui.pushButton_10.setEnabled(False)
window.connect(ui.pushButton_2, QtCore.SIGNAL("clicked()"),newProjClicked)
window.connect(ui.pushButton_3, QtCore.SIGNAL("clicked()"),loadProjClicked)
window.connect(ui.pushButton_8, QtCore.SIGNAL("clicked()"),cameraCalibClicked)
window.connect(ui.pushButton_9, QtCore.SIGNAL("clicked()"),fieldPlanningClicked)    
window.connect(ui.pushButton_13, QtCore.SIGNAL("clicked()"),threedModelClicked)    
window.connect(ui.pushButton, QtCore.SIGNAL("clicked()"), dQueryClicked)  
window.connect(ui.pushButton_11, QtCore.SIGNAL("clicked()"), sandMClicked)    
window.connect(ui.pushButton_10, QtCore.SIGNAL("clicked()"), pointCloudClicked)
window.connect(ui.pushButton_4, QtCore.SIGNAL("clicked()"), helpClicked)
window.connect(ui.pushButton_5, QtCore.SIGNAL("clicked()"), aboutClicked)
image_file1=str(os.path.join(wrk_drr,"isro1.jpg"))
image_file2=str(os.path.join(wrk_drr,"iirs.jpg"))
image_file3=str(os.path.join(wrk_drr,"trivim1.jpg"))
ui.label.setPixmap(QPixmap(image_file1))
ui.label.show()
ui.label_2.setPixmap(QPixmap(image_file2))
ui.label_2.show()
ui.label_4.setPixmap(QPixmap(image_file3))
ui.label_4.show()
window.show()
app.exec_()
