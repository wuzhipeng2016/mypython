import os.path
import os,sys

def myadd(path,filename,data):
    flist = findfile(path,filename)
    for f in flist:
        find = checkExists(f,data)
        if not find:
            addData(f,data)

def findfile(path,filename):
    flist=[]
    for root,dirs,files in os.walk(path):
        for fname in files:
            if fname.startswith(filename):
                flist.append(os.path.join(root,fname))
    return flist

def checkExists(f,data):
    if not os.path.isfile(f):
        return
    fd=open(f,'r')
    old=fd.readlines()
    fd.close()

    for key in old:
        if data in key:
            return True
    return False 

def addData(f,data):
    if not os.path.isfile(f):
        return
    fd=open(f,'a')
    fd.write(data+'\n')
    fd.close()

#test code
mydir=r'E:\book\ignore\emap'
myfile='EMAP_APP'
data='aabbccdd'
myadd(mydir,myfile,data)

