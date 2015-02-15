import os
from os.path import expanduser
home = expanduser("~")
trf= open(os.path.join(home,"Trivim.txt"),'r')
trivim= trf.readline()

placemarkStr = ''

#function to add placemarks 
def placemark(filename,values,lat,longi,altitude): #values is a list of values to be filled in the placemark file
    global placemarkStr
    f = open(filename,'r')
    linesCol = f.readlines()
    totalLength = len(linesCol)
    f.close()

    placemarkStr += '<Placemark>\n\
        <ExtendedData>\n'
    placemarkStr += '<Data name="Name">\n\
            <value>'+values[0]+'</value>\n\
          </Data>\n'
    for i in range(totalLength):
        placemarkStr += '<Data name="'+(linesCol[i])[:-1]+'">\n\
            <value>'+values[i+1]+'</value>\n\
          </Data>\n'
    placemarkStr += '<Data name="Height:">\n\
            <value>'+altitude+'</value>\n\
          </Data>\n'
    placemarkStr += '</ExtendedData>\n\
        <Point>\n\
          <coordinates>'+lat+','+longi+','+altitude+'</coordinates>\n\
              <altitudeMode>relativeToGround</altitudeMode>\n\
              <extrude>1</extrude>\n\
        </Point>\n\
    </Placemark>\n'

def main():
    global placemarkStr
    f = open(os.path.join(trivim,'curr_proj.txt'),'r')
    pathDir = f.readline()
    f.close()

    #pathDir has the path of the current project
    os.chdir(pathDir)
    fw = open(r'dblist.txt','w')
    #print "inside add_placemark main function"
    #print "this is placemarkstr"

    #print placemarkStr
    
    f = open(os.path.join(trivim,r'3d-modelling\Placemark.kml'),'r') #reading from the previously created Placemark file
    linespp = f.readlines()
    temp = len(linespp)
    f.close()
    placemarkStr += linespp[0]
    placemarkStr += linespp[1]
    placemarkStr += linespp[2]
    shortPath = '\\input'
    #print "this is second placemarkstr formed"
    #print placemarkStr

    #the placemark data is fed into placemarkStr
    
    #changing the directory to input folder of the current project
    os.chdir(pathDir + shortPath)

    DIR=os.listdir(pathDir + shortPath)
    print DIR

    # build1 , build2 ... are iterated
    for dir1 in DIR:
        print dir1
        os.chdir(pathDir + shortPath + '\\' + dir1)
        fHeight = open(r'heights.txt','r')
        hstr = fHeight.readline()
        fHeight.close()
        #reading the heights.txt file of each building

        tempList = hstr.split('\t')
        num_floors = len(tempList) - 1

        #build1.txt is opened
        fcoord = open(dir1+'.txt','r')
        cstr = fcoord.readline()
        fcoord.close()

        #heights are read of build1
        
        lat = (cstr.split('\t'))[1]
        longi = (cstr.split('\t'))[2]
        height = 0.0
      
        with open(pathDir+'\\column.txt','r') as f:
            numColumns=len(f.readlines())

        #all the floors of the building are iterated
        for i in range(num_floors):
            filename = (dir1 + '_' + '%s' %(i+1))

            #they are read
            fdetail = open(filename+'.txt','r')
            lines = fdetail.readlines()
            temp = len(lines)
            fdetail.close()
            values=[]
            for j in range(temp):
                tempStr = (lines[j])[:-1]
                values.append(tempStr)
          
            
            print values
            height += float(tempList[i+1])
            altitude = str(height)
            print altitude
            print lat
            print longi
            ##Snehil's FILE

            #for example build1_1db.txt
            filename1 = filename+'db.txt'
            
            fsnehil = open(filename1,'w')
#the values are entered 
            fsnehil.writelines(values[0]+'\n')
            fsnehil.writelines(lat+'\n')
            fsnehil.writelines(longi+'\n')
            fsnehil.writelines(altitude+'\n')
            if temp-1<=numColumns:
                columnsToEnter=temp-1
            else:
                columnsToEnter=numColumns
            for i in range(columnsToEnter) :
                fsnehil.writelines(values[i+1]+'\n')
            fsnehil.close()
            #the filename is added in the dblist file
            fw.write(filename1+'\n')

            placemark(pathDir+'\\column.txt',values,lat,longi,altitude)
    placemarkStr += linespp[3]
    placemarkStr += linespp[4]
    print placemarkStr
    fw.close()
    
##    f = open(r'C:\3d-Model\bin\curr_proj.txt','r')
##    pathDir = f.readline()
##    f.close()
    shortPath = '\\output'
    filenmP = pathDir + shortPath + '\\Placemark.kml'
    
    fw = open(filenmP,'w')
    fw.writelines(placemarkStr)
    fw.close()
