import sqlite3
import os

def run(projPath):
    print projPath
    pathDir=projPath
    os.chdir(projPath)
    print "current working directory is ", os.getcwd()
    paths = projPath.split('/')
    index=len(paths)-1
    projName = paths[index] + '.db'
    print "database name", projName
    
    conn= sqlite3.connect(projName)
     
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE information
                 (name text, latitude text, longitude text, altitude real)''')
    cursor.close()
    conn.close()

    




          
