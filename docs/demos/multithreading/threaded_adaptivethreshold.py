#!/usr/bin/python2.7

import glob
import os
from Queue import Queue
from threading import Thread

import cv2

def filtra_immagine(filename):
    img = cv2.imread('input/' + filename, 0)
    img = cv2.medianBlur(img, 5)
    thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
    cv2.imwrite('output/' + filename, thresh)



files = glob.glob(('input/*'))

job_queue = Queue()

for file in files:
    job_queue.put(file)

print 'Job queue size: {}'.format(job_queue.qsize())

def worker():
    while not job_queue.empty():
        filename = job_queue.get(True)
        filtra_immagine(os.path.basename(filename))
        job_queue.task_done()

for thread in range(3):
    t = Thread(target=worker)
    t.daemon = False
    t.start()
    print 'Thread: {}'.format(thread)


job_queue.join()
