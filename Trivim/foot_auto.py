import re
import os

def find(q,dr):
    x=1
    y=0
    
        
    drec=os.chdir(dr)
    dx=os.listdir(dr)
    print dr
    print dx
    print q
    address=os.path.join(dr,dx[q])
    #print "this is address"
    #print address
    f=open(address)
    #if f.endswith(".kml"):
               
    for line in f:
            
        if re.search("<coordinates>",line):
            
            #print "This is line in for loop"
            #print line
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
            break
        
            '''else:
                print "NOT A KML FILE"
                req_string=""'''
    #else:
        #print "other file"
        #req_string=""
    
    #print "this is x" 
    print x
    #print "this is y"
    print y
    return req_string

def store(req_string,q,dr):
    #req string without comma replacing space
    #f_w = open(r'C:\pSApp\input\build%d\build%d.txt'%(q,q),'w')
    #########
    drec=os.chdir(dr)
    dx=os.listdir(dr)
    print dr
    print dx
    addr=dr+'\\'+dx[q]+'.txt'
    address=addr.replace(".kml","")
    #print "This is the address in store"
    #print address
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
        #print "file successfully written "
        
def main():
    f=open("temp.txt",'r')
    line_count=0
    global check
    check=0;
    
    for line in f.readlines():
        line_count=line_count+1
        #print "printing line in main for loop"
        #print line
        if(line_count>0):
            l=line.replace("\n","")
            ##l.replace("\n"," ")
            #print "This is l inside foot_auto.py"
            #print l
            os.chdir(l)
            num_dir=len(os.listdir(l))
            dir_list=os.listdir(l)
            #print "this is range in dir"
            #print range(num_dir)
            for i in range(num_dir):
                if dir_list[i].endswith(".kml"):
                    x=find(i,l)
                    store(x,i,l)
             
    #print "program is finished"
        
