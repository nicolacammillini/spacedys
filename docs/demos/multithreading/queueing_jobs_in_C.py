from queue import Queue
from subprocess import call
from threading import Thread
from time import time

numbers = [2139079, 1214759, 1516637, 1852285, 7834682, 34234223, 22087259, 6554269, 3675475, 7685843]

job_queue = Queue()

for number in numbers:
    job_queue.put(number)


def worker():
    
    while True: 
        job = job_queue.get(block=True)
        call(["./factorize", str(job)])
        job_queue.task_done()

start = time()

for thread in range(3):
    t = Thread(target=worker, daemon=True)
    t.start()
    #print('Thread: {}'.format(thread))


job_queue.join()

end = time()

print('Took %.3f seconds' % (end - start))