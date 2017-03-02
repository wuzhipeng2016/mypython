import os

def addhead(filename):
    data=[]
    fd=open(filename,'r','utf-8')
    data=fd.readlines()
    fd.close()

    fd=open(filenname,'w','utf-8')
    fd.write('delete from t_jw_glgz;')
    fd.writelines(data)
    fd.write('commit;')
    fd.close()    

path=''
filenname=''
addhead(os.path.join(path,filename))

