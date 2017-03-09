import itertools
import os



def run(PointDir,geofile):
    outfile = os.path.join(PointDir,"bundle",r"bundle.out")
    os.chdir(PointDir)
    os.mkdir('ImageCoor')
    imagecoorfolder = os.path.join(PointDir,"ImageCoor")
    
    x=no_images(outfile)
    print x
    data_access(x,outfile,imagecoorfolder)
    data_access1(imagecoorfolder)
    combine(imagecoorfolder)
    image(outfile,x,imagecoorfolder,geofile)

def no_images(outfile):
    f=open(outfile,'r')
    lineno = 0
    for line in f.readlines():
        if lineno == 1:
            m = line.index(' ')
            l = line[:m]
            n=int(l)
            return n
        lineno = lineno + 1
            
def data_access(x,outfile,imagecoorfolder):
    f=open(outfile,'r')
    lineno = 0
    for line in f.readlines():
        if lineno > (x*5+1):  
            data=line.rstrip()
           
            os.chdir(imagecoorfolder)
            with open('imgcoor1.txt', "a") as myfile:
                myfile.write(data + "\n")            
        lineno = lineno + 1
          
    



def data_access1(imagecoorfolder):
    os.path.join(imagecoorfolder)
    f1=open('imgcoor1.txt','r')
    lineno = 1
    count=1
    for line in f1.readlines():
        
        if lineno%3 == 0:
            data=line.rstrip()
            #print data
            with open('imgcoor2.txt', "a") as myfile:
                myfile.write(data + "\n")
        elif lineno%3 == 1:
            data=line.rstrip()
            #print count
            with open('imgcoor2.txt', "a") as myfile:
               myfile.write(data+ " "+ str(count)+"\n")
            count=count+1
        lineno = lineno + 1
        

    
def combine(imagecoorfolder):
    os.path.join(imagecoorfolder)
    f=open('imgcoor2.txt','r')
    lineno=1
    s=[]
    
    for line in f.readlines():
        
        if lineno%2 == 1:
            x=line.rstrip()
            
           # with open("test5.txt", "a") as myfile:
               #myfile.write(x+"\n")
           
            
            s.append(x)
            

            
        elif lineno%2 == 0:
            data=line.rstrip()
            data1 = data.split(" ")                  
            data1.pop(0)  
            i=0
            new_list=[]
            while i<len(data1):
                new_list.append(data1[i:i+4])        
                i+=4
            index=1
            new_list1=[ (y[0:index] + y[index+1:])  for y in new_list]      
            #print new_list1
            s.append(new_list1)
            #print s
            
          
        lineno=lineno+1
    x=dict(itertools.izip_longest(*[iter(s)] * 2, fillvalue=""))
    #print x
    for key, value in x.iteritems():
        for value1 in value:
            #print value1 , key
            #print value1[0]
            af=" ".join(str(x1) for x1 in value1)
            #print af,key
            
            with open('image'+ value1[0] +'.txt','a') as eachfile:
               eachfile.write( af+ " "+key+ "\n")
               eachfile.close()
            
def image(outfile,imgno,imagecoorfolder,geofile):
    os.path.join(imagecoorfolder)
    imgno1=0
    while (imgno1 <= (imgno-1)):
        f=open('image'+ str(int(imgno1))+'.txt','r')
        for line in f.readlines():
            data=line.rstrip()
            y=data.split()
            y1=y[3:6]
            s=int(y[-1])
            f1=open(geofile,'r')
            lineno=1
            for lines in f1.readlines():
                if lineno == s:
                    x=lines.rstrip()
                    x1=x.split()
                    a=x1[:3]
                    y[3:6]=x1[:3]
                    ynew=" ".join(str(yy) for yy in y)
                    with open('imagenew'+ str(int(imgno1))+'.txt', "a") as myfile:
                        myfile.write(ynew+"\n")
                        
                lineno=lineno+1
        imgno1=imgno1+1
                       




  





    

   

  

