import os,sys,glob,time
from subprocess import Popen,PIPE

testdir = sys.argv[1] if len(sys.argv)>1 else os.curdir

forcegen = len(sys.argv)>2
print('Start tester:',time.asctime())
print('in',os.path.abspath(testdir))


def verbose(*args):
    print('-'*80)
    for arg in args:
        print(arg)

def quiet(*args):
    pass

trace = quiet


testpatt = os.path.join(testdir,'Scripts','*.py')
testfiles = glob.glob(testpatt)
testfiles.sort()
trace(os.getcwd(),*testfiles)

numfail =0
for testpath in testfiles:
    testname = os.path.basename(testpath)

    infile =testname.replace('.py','.in')
    inpath =os.path.join(testdir,'inputs',infile)
    indate=open(inpath,'rb').read() if os.path.exists(inpath) else b''

    argfile = testname.replace('.py', '.arg')
    argpath = os.path.join(testdir, 'args', infile)
    argdate = open(argpath, 'rb').read() if os.path.exists(argpath) else ''

    outfile = testname.replace('.py','.out')
    outpath = os.path.join(testdir, 'outputs', outfile)
    outpathbad =outpath+ '.bad'
    if os.path.exists(outpathbad):os.remove(outpathbad)

    errfile=testname.replace('.py','.err')
    errpath=os.path.join(testdir,'errors',errfile)
    if os.path.exists(errpath):os.remove(errpath)
    pypath =sys.executable
    command='%s%s%s' %(pypath,testpath,argdate)
    trace(command,indate)

    process = Popen(command,shell=True,stdin=PIPE,stdout=PIPE,stderr=PIPE)
    process.stdin.write(indate)
    process.stdin.close()
    outdata=process.stdout.read()
    errdata = process.stderr.read()
    exitstatus=process.wait()
    trace(outdata,errdata,exitstatus)

    if exitstatus !=0:
        print('error status:',testname,exitstatus)
    if errdata:
        print('error stream:',testname,errpath)
        open(errpath,'wb').write(errdata)
    if exitstatus or errdata:
        numfail +=1
        open(outpathbad,'wb').write(outdata)
    elif not os.path.exists(outpath) or forcegen:
        print('generating:',outpath)
        open(outpath,'wb').write(outdata)
    else:
        priorout=open(outpath,'rb').read()
        if priorout==outdata:
            print('passed:',testname)
        else:
            numfail +=1
            print('failed output:',testname,outpathbad)
            open(outpathbad,'wb').write(outdata)

print('finidhed:',time.asctime())
print('%s tests run,%s tests failed,'%(len(testfiles),numfail))
