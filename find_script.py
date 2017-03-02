import os,os.path

def find(path,text):
    for root,dirs,files in os.walk(path):
        for fname in files:
            if fname.startswith('version') and fname.endswith('xml'):
                fullname=os.path.join(root,fname)
                if checkContent(fullname,text):
                    print(fullname)


def checkContent(filename,text):
    fd=open(filename,'r',encoding= 'utf-8')
    lines=fd.readlines()
    for line in lines:
        s=line.upper()
        if text in s:
            return True

    return False

text='SFSDPK'
path='C:\\a\\com'
find(path,text)

