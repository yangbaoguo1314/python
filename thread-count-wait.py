import  _thread as thread ,time

stdoumutex = thread.allocate_lock()
exitmutexs = [thread.allocate_lock() for i in range(10)]

def counter(myId,count):
    for i in range(count):
        stdoumutex.acquire()
        print('[%s] => %s' %(myId,i))
        stdoumutex.release()
    exitmutexs[myId].acquire()


for i in range(10):
    thread.start_new_thread(counter,(i,100))

for mutex in exitmutexs:
    while not mutex.locked():pass

print('Main thread exiting!')