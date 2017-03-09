import os
import sys
import shutil
import math
#import simplekml
import UTM as con

def run(src,dest):
    
   # src=a[0]
   # dest=a[1]
    files=os.listdir(src)
    print src
    print dest
    print files
    dest_files=os.listdir(dest)
    print dest_files
    
    for dest_file in dest_files:
        full_dest=os.path.join(dest,dest_file)
        paths=os.path.join(full_dest,"heights.txt")
        outp=open(r'%s' %paths,"w")
        outp.write(str(dest_file))


    for filed in files:
        inp=open(os.path.join(src,filed),"r")
        print inp
        a=0
        s=''
        while filed[a]!='.':
            s=s+filed[a]
            a=a+1

       
        for dest_file in dest_files:
            t=dest_file[-1:]
            print "t", t
            if s[-3]==t :
                full_dest=os.path.join(dest,dest_file)
                paths=os.path.join(full_dest,"heights.txt")
                outp=open(r'%s' %paths,"a")
                
               # outp.write('building_'+str(t))
                outp.write('\t')
                count=0
                l=[]
                m=[]
                n=[]
        
              
                for line in inp:
                    count=count+1

                inp.seek(0)
                c=0
                for line in inp:
                    print line
                    x,y,z,z1=line.split()
                    
            
                    l.append(x)
                    m.append(y)
                    n.append(z)
    

                while c<count-1:
                    y1=float(n[c])
                    y2=float(n[c+1])
                    c=c+1
                    e=math.sqrt(  (y2-y1)**2  )
                    d=(str(e))
                    outp.write(d)
                    if c<count-1:
                        outp.write('\t')
        #outp.seek(0)
       #outp.write('building_'+str(t))                  
    
                
##heightDir="C:\Users\Diksha\Desktop\diksha\Height"                       
##projPath="C:\Users\Diksha\Desktop\diksha\input"    
####a=projPath+"\input"
####print a
####b=[heightDir,a]
####print 'callin utm_height'
##run(heightDir,projPath)
