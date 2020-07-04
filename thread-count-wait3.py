import _thread as thread ,time

stdoumutex = thread.allocate_lock()
numthreads = 5
exitmutexes = [thread.allocate_lock() for i in range(numthreads)]

def counter(myId,count,mutex):
    for i in range(count):
        time.sleep(1/(myId+1))
        with mutex:
            print('[%s] ==> %s' %(myId,i))
    exitmutexes[myId].acquire()

for i in range(numthreads):
    thread.start_new_thread(counter,(i,5,stdoumutex))

while not all(mutex.locked() for mutex in exitmutexes):time.sleep(0.25)
print('Main thread exiting!')