import os
import sys

def run(a):

    src=a[0]
    file_name=os.listdir(src)
    c=1000

    for files in file_name :
        
        #print files
        os.chdir(src)
        os.rename(files,'photo'+str(c)+'.jpg')
        c=c+1
    
    
