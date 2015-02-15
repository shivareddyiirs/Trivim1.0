import sqlite3
import os
from os.path import expanduser
##from Tkinter import *
##import tkMessageBox

def run():
##    root= Tk()
    
    home = expanduser("~")
    path = open(os.path.join(home,'Trivim.txt'),'r')
    trivim= path.readline()
    path.close()
    f = open(os.path.join(trivim,'curr_proj.txt'),'r')
    pathDir = f.readline()
    f.close()
    os.chdir(pathDir)
    paths = pathDir.split('/')
    index=len(paths)-1
    projName = paths[index] + '.db'
    print "databse is", projName
    try:
        conn= sqlite3.connect(projName)
    except:
        print "Connection Failed"# Name of database

    cursor = conn.cursor()
    count = 0
    #for row in cursor.execute('Select * FROM information where build_year > 2000'):
        #print row
        #count +=1

    #cursor.execute('DELETE FROM information')
    #conn.commit()
    '''
    Query insert test
    line1 = ['test','78.12345678901234','78.12345678901234',10,45,78.12345678901234,'shop','private',1999]
    s = 'Insert INTO information values(?,?,?,?,?,?,?,?,?)'
    cursor.execute(s,line1)
    conn.commit()
    '''

    #Below code is correct only it needs to be corrected such that
    #at right places integer values are inserted
    #by reading from the dataType.txt
    fw=open(pathDir+'\\dblist.txt','r')# Path
    #name of the text files having info of each segments of buildings

    line=fw.readlines()
    print line

    for i in range(0,len(line)):
        #line[i]=line[i].encode('ascii','ignore')
        line[i]=line[i].strip()
        a=line[i].split('_')
        
        print a[0]
        print a[1]
        
        s=pathDir+'\\input\\'+a[0]+'\\'+line[i]
        print s
        
        f=open(s,'r') # name of db.txt file with path

        line1=f.readlines()
        
        flag=1
        i=0
        arr=[]

        for i in range(0,len(line1)):
            line1[i]=line1[i].strip()
        
        for row in cursor.execute('SELECT * FROM information'):
            arr.append(row[0])

        b= line1[0].lower()
        b=b.strip()
        print len(line1)
        
        
        #here line1 needs to be edited according to the dataType.txt
        #so that it has
        #both long and string values and not string values
        #only

        
        line1[3] = float(line1[3]) #altitude always a long type

        typeFile = open(pathDir+'\\dataType.txt','r')
        type1 = typeFile.readlines()
        
        typeFile.close()
        try:
            for index in range(len(type1)):
                type1[index] = (type1[index])[:-1]
        except:
            pass
        
        #in try catch so that in case of exception like no data in file it does not halt the program
        index = 0
        try:
            for index in range(len(type1)):
                if(type1[index].upper() == 'REAL'):
                    line1[4+index] = float(line1[4+index])
                    print "converted to float"
                elif(type1[index].upper() == 'VARCHAR'):
                    line1[4+index] = line1[4+index]
                    print "converted to string"
                else:
                    print "Wrong datatype selected"
        except:
            pass
        
        for i in range(0,len(arr)):
            a= arr[i].lower()
            if a==b:
##                tkMessageBox.showinfo("Message","Value already exists")
                flag=0
                break
        i=0
        if flag==1:
            s='INSERT INTO information VALUES(?'
            print str(len(line1)) + "  " + str(line1) 
            while(i<(len(line1)-1)):
                s=s+',?'
                i+=1
            s=s+')'
     
            cursor.execute(s,line1)
            conn.commit()
            print "Message","Value added successfully"

    conn.close()   
##    root.destroy()
