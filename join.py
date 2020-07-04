import sys,os
readsize=1024

def join(fromdir,tofile):
    output=open(tofile,'wb')
    parts =os.listdir(fromdir)
    parts.sort()
    for filename in parts:
        fileobj = os.path.join(fromdir,filename)
        fileobj =open(fileobj,'rb')
        while True:
            filebytes = fileobj.read(readsize)
            if not filebytes:
                break
            output.write(filebytes)
        fileobj.close()
    output.close()


if __name__=='__main__':
    if len(sys.argv)==2 and sys.argv[1]=='-help':
        print('Use:join.py [from - dir-name to-file-name]')
    else:
        if len(sys.argv) !=3:
            interactive=True
            fromdir =input('目录包含零件文件?')
            tofile  =input('要重新创建的文件的名称?')
        else:
            interactive=False
            fromdir,tofile = sys.argv[1:]
        absfrom,absto = map(os.path.abspath,[fromdir,tofile])
        print('Joining',absfrom,'to make',absto)

        try:
            join(fromdir,tofile)
        except:
            print('Error joining files:')
            print(sys.exc_info()[0],sys.exc_info()[1])
        else:
            print('join comlete:see',absto)
        if interactive:
            input('press enter key')