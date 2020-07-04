numconsumers = 2
numproducers = 4
nummessages  = 4


import  _thread as thread ,time,queue

safeprint = thread.allocate_lock()
dataqQueue = queue.Queue()

def producer(idum):
    for msgnum in range(nummessages):
        time.sleep(idum)
        dataqQueue.put('[producer id = %d,count = %d]' %(idum,msgnum))
def cousumer(idum):
    while True:
        time.sleep(0.1)
        try:
            data = dataqQueue.get(block=False)
        except queue.Empty:
            pass
        else:
            with safeprint:
                print('consumer',idum,'got =>',data)

if __name__ == '__main__':
    for i in range(numconsumers):
        thread.start_new_thread(cousumer,(i,))
    for i in range(numproducers):
        thread.start_new_thread(producer,(i,))
    time.sleep(((numproducers-1)*nummessages)+1)
    print('Main thread exiting!')