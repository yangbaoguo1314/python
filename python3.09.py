#import subprocess
#subprocess.call('cmd /c "tkinte
from multiprocessing import Process
import os

def child():
    print('hello from child',os.getpid())
    os._exit(0)

def parent():
    while True:
        newpid = os.fork()
        if newpid ==0:
            child()
        else:
            print('hello from parent',os.getpid(),newpid)
            if input()=='q':break

parent()