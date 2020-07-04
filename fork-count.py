# import os , time
# # from multiprocessing import Process
# # def counter(count):
# #     time.sleep(1)
# #     print('[%s] => %s' (os.getpid(),i))
# #
# # for i in range(5):
# #     pid = Process(target=counter(),args=('test',))
# #     #pid=os.fork()
# #     if pid !=0:
# #         print('Process %d spawned' %pid)
# #     else:
# #         counter(5)
# #         os._exit(0)
# #
# # print('Main process exiting')

from multiprocessing import Process
import os

def run_proc(name):
    print('运行子进程%s(%s)......'%(name,os.getpid()))

if __name__ == '__main__':
    print('父进程%s'%os.getpid())
    p = Process(target=run_proc,args=('test',))
    print('子进程将开始')
    p.start()
    p.join()
    print('子进程结束')