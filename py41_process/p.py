#!/usr/bin/env python3


import os
import time
import random
import subprocess
from multiprocessing import Process
from multiprocessing import Pool
from multiprocessing import Queue

'''
print('Process (%s) start ...' % os.getpid())

pid = os.fork()
if pid == 0:
	print('I am child process (%s) and my parent process is (%s).' %(os.getpid(), os.getppid()))
else:
	print('I (%s) just created a child process (%s).' %(os.getpid(), pid)) 

#fork() 返回两次 pid==0为子进程
'''

'''
def run_proc(name):
	print('Run child process %s (%s).' %(name, os.getpid()))

if __name__ == '__main__':
	print('Parent process (%s).' %(os.getpid()))
	p = Process(target=run_proc, args=('test',))
	print('Child process will start...')
	p.start()
	p.join()    #join()方法等待子进程执行结束
	print('Child process end.')
'''

'''
def long_time_task(name):
	print('Run task %s (%s)...' %(name, os.getpid()))
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print('Task %s runs %0.2f seconds.' %(name, (end-start)))

if __name__ == '__main__':                                   
	print('Parent process (%s).' %(os.getpid()))             
	p = Pool(4)				#设置最大同时运行4个进程
	for i in range(5):		#开启5个进程 将有1个进程等待 注意这里跟CPU核心数有关 虚拟机开启虚拟化技术后 可能看不到等待现象
		p.apply_async(long_time_task, args=(i,))
	print('Waiting for all sub processes done...')                     
	p.close()          
	p.join()    #join()方法等待子进程执行结束                
	print('All subprocess end.') 
'''



'''
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)
'''


def write_queue(q):
	print('Process to write: %s.' % os.getpid())
	for value in ['a', 'b', 'c']:
		print('Put %s to queue.' % value)
		q.put(value)
		time.sleep(random.random())

def read_queue(q):
	print('Process to read: %s.' % os.getpid())
	while True:
		value = q.get(True)
		print('Get %s from queue.' % value)


if __name__ == '__main__':
	q = Queue()
	pw = Process(target=write_queue, args=(q,))
	pr = Process(target=read_queue, args=(q,))

	pw.start()
	pr.start()
	
	pw.join()

	pr.terminate()

