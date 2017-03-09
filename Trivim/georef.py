import os
import numpy as np
import re
import transformations as trans
numcam=0
def getGroundCoord(grCoordFilePath,order):
    f=open(grCoordFilePath,'r')
    lines = f.readlines()
    grCoords=[lines[int(i)+1] for i in order]
##    print grCoords
    grCoordsPath="GroundCoordinates.txt"
    with open(grCoordsPath,'w') as grCoordinates:
        for li in grCoords:
            grCoordinates.write(li)
    return True
def readply(ply,skip=0,skip_foot=0):
    data = np.genfromtxt(ply,skip_header=skip,skip_footer= skip_foot,usecols=(0,1,2))
    data1 = np.matrix(data,dtype=np.float64, copy=False)
    with open(ply,'r')as input:
        header=input.readlines()[:skip]
       
    return data1        
def add1(x):
    columns= np.shape(x)
    ones= np.ones(columns[1])
    temp=np.vstack((x,ones))
    return temp

def applyTransform(tranformMatrix,mdlCoords):
    x = add1(mdlCoords)
    print "mdlcoords", x
    y= np.dot(tranformMatrix,x)
    return y.T
    
def writeply(header,grCoords,trfile):
    with open(trfile,'w') as output:
        output.writelines(header)
        np.savetxt(output,grCoords,fmt="%s")
    return True

def georef(ply,camCoords,output):
    print "Inside georef",os.getcwd()
    header=""
    camImgCoords =  readply(camCoords)
    print "camImgCoords", camImgCoords
    grCord = np.genfromtxt("GroundCoordinates.txt", usecols=(0,1,2))
    camGrCoords = np.matrix(grCord,dtype=np.float64, copy=False)
    print "camGrCoords", camGrCoords
    mdlCoords = readply(ply,12,2*numcam)
    print "mdlCoords", mdlCoords
    Tr = trans.superimposition_matrix(camImgCoords.T,camGrCoords.T,True)
    print "Transformation", Tr
    print trans.decompose_matrix(Tr)
    grCoords = applyTransform(Tr,mdlCoords.T)
    print "grCoords", grCoords
    tempclr=grCoords[:,:-1]
    writeply("",tempclr,output)

def getOrder(outPath):
    outFile=open(outPath,'r')
    f=outFile.readlines()
    i=0
    flag=0
    order=[]
    order1=[]
    numLines=len(outFile.readlines())
    for lines in reversed(f):
        if re.search("focal",lines)==None:
            i=i+1
        else:
            break
    for j in range(0,i):
       if re.search("SifterApp::DumpOutputFile",f[numLines-(i-j)])==None:
           content=f[numLines-(i-j)].split(" ")
           order.append(content[7].replace(';',""))
       else:
           break;
    outFile.close()
    for e in reversed(order):
        order1.append(e)
    return order1


    
    

def getCam(pointdir,camGrCoords):
    bundir=os.path.join(pointdir,"bundle")
    os.chdir(bundir)
##    bundlefile= open("bundle.out",'r')
    
    i=0;
    order=getOrder("out")
    getGroundCoord(camGrCoords,order)
    print order 
##    for lines in bundlefile:
##        if i<2:
##            totalnumcam=lines.split(" ");
##            global numcam
##            if i==1:
##                numcam=int(totalnumcam[0]);
##            i=i+1;
##        else:
##            break;
    global numcam
    numcam=len(order)
    i=0;
    j=0;

    f = os.listdir(bundir)
    print f
    for file in f:
        if file.endswith(".ply"):
            f= [(file)]
            print f
    print "output"
    for item in f:
        print [item]
    print item
    CamCoords= str(item)  
##    CamCoords= "points0"+str(numcam)+".ply"
    plyfile=open(CamCoords,'r')
    numcamd=numcam*2;
    print numcam
    print "done"
    outpath= "cameraCoordinates.txt"
    with open(outpath,'w') as camCoordFile:        
        for lines in reversed(plyfile.readlines()):
            if i<numcamd:
                if i%2==0:
                    content=lines.split(" ")
##                    print content
##                    print "try"
                    camCoordFile.write(content[0]+"\t"+content[1]+"\t"+content[2]+"\t"+order[j]+"\n")
                    j=j+1;
##                else:
##                    print "reading odd line"
                i=i+1;
            else:
                break;
##        bundlefile.close()
        plyfile.close()
    return os.path.join(bundir,outpath)
    
def run(pointdir,camGrCoords,output):
    CamCoordsfile= getCam(pointdir,camGrCoords)
    ply = os.path.join(pointdir,"bundle","points0"+str(numcam)+".ply")
    georef(ply,CamCoordsfile,output)




    


    
