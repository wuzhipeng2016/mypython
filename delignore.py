import os.path
import os,sys
from addignore import *

def mydel(path,filename,data):
    flist = findfile(path,filename)
    for f in flist:
        find = checkExists(f,data)
        if find:
            delData(f,data)

def delData(f,data):
    if not os.path.isfile(f):
        return
    fd=open(f,'r')
    old=fd.readlines()
    fd.close()

    fd=open(f,'w')
    for key in old:
        if not data in key:
            fd.write(key)
    fd.close()

#test code
mydir=r'E:\book\ignore\emap'
myfile='EMAP_APP'
data='aabbccdd'
mydel(mydir,myfile,data)

