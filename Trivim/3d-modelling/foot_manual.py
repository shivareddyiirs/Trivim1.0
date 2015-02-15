import re
import os

def find(dr):
    print "inside foot_manual in 3d modelling"
    x=1
    y=0
    for files in os.listdir(dr):
	    if files.endswith(".kml"):
		    f=open(files)
        
    for line in f:
        if re.search("<coordinates>",line):
            print('start in line 1')
            req_string=''

            if re.search("</coordinates>",line):
                    print 'end in line 1 all coos in same line'
                    y = 1
                    line = re.sub("<coordinates>",'',line)
                    line = re.sub("</coordinates>",'',line)
                    req_string = line.strip()
                    break

            if(len(line.strip())==13):
                print'no coords in <coo> line'
                y = 0
            else:
                print'coords in <coo> line'
                y = 1
                line = re.sub("<coordinates>",'',line)
                req_string = line.strip()
                
            for line in f:
                x = x+1
                y = y+1
                req_string = req_string + line.strip()
                if re.search("</coordinates>",line):
                    print 'end in line' ,x
                    if(len(line.strip())==14):
                        print'no coords in </coo> line'
                        y = y-1
                        req_string = re.sub("</coordinates>",'',req_string)
                        break
                    else:
                        print'coords in </coo> line'
                        req_string = re.sub("</coordinates>",'',req_string)
                        break
    return req_string
    print x
    print y

def store(req_string,dr):
    for files in os.listdir(dr):
	    if files.endswith(".kml"):
		    f=(files)
    address=dr+'\\'+f[:-4]+'.txt'
    f_w=open(address,'w')
    
    count1 = 0
    a = 0
    while(a!=-1):
        a = req_string.find(',',a+1)
        count1 = count1+1
    ########
    req_string = re.sub(' ',',',req_string)
    num_coo= (count1-1-2)/2
    print num_coo
    f_w.write('%s'%(num_coo))
    #height = 10
    #f_w.write('\t'+'%s'%(height))
    p = 0
    x = 0
    z = 0
    count = 0
    count1 = 1
    print req_string
    
    while(count<=(3*num_coo-1)):
        x = req_string.find(',',x+1)
        ##code segment removed
        print (req_string[z:x])
        if((count-2)%3!=0):
            f_w.write('\t'+req_string[z:x])
        p = x
        z = p+1
        count = count+1
            
if __name__ == "__main__":
    #b=os.listdir('.\..\..')
    b=os.getcwd()
    #os.chdir('.\..\..')
    #c=os.getcwd()
    f=open(b+'\\temp.txt')
    #os.chdir(r'C:\pSApp\tempFiles')
    #f=open("temp.txt")
    line_count=0
    
    for line in f:
        line_count=line_count+1
        if(line_count==1):
            l=line
            break
    
    os.chdir(l)
    x=find(l)
    store(x,l)
        
        

        
