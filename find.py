import os,os.path

def find(path):
    s=0
    sm=0
    qt=0
    for root,dirs,files in os.walk(path):
        for fname in files:
            fullname=os.path.join(root,fname)
            size=os.path.getsize(fullname)
            m=getmsize(size)
            if m>100:
                sm=sm+size
                s=s+m
                print('{:^5}'.format(m)+fullname)
            else:
                qt=qt+size

    print('total size:%10s,%5s,%10s'%(s,getmsize(qt),getmsize(sm+qt)/1024))

def getmsize(bytes):
    return bytes//(1024*1024)

path='d:\\'
find(path)

