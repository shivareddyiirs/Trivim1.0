import os
import sys
import shutil
import math
#import simplekml
import UTM as con

def run(a):

    src=a[0]
    dest=a[1]
    files=os.listdir(src)
    print src
    print dest
    dest_files=os.listdir(dest)


    for filed in files:
        inp=open(os.path.join(src,filed),"r")
        a=0
        s=''
        while filed[a]!='.':
            s=s+filed[a]
            a=a+1
       
        for dest_file in dest_files:
            t=dest_file[5:]
            if s==t :
                full_dest=os.path.join(dest,dest_file)
                paths=os.path.join(full_dest,"heights.txt")
                outp=open(r'%s' %paths,"w")
                outp.write('building_'+str(t))
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
                    x,y,z=line.split(',')
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
     
