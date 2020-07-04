import _thread as thread,time

stdoumutex = thread.allocate_lock()
exitmutex  = [False] *10

def counter(myId,count):
    for i in range(count):
        stdoumutex.acquire()
        print('[%s] ==> %s' %(myId,i))
        stdoumutex.release()
    exitmutex[myId] = True

for i in range(10):
    thread.start_new_thread(counter,(i,100))

while False in exitmutex:pass

print('Main thread exiting!')