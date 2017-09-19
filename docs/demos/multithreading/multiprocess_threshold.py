#!/usr/bin/python2.7

import glob
import os
from multiprocessing import Queue, Process

import cv2

def filtra_immagine(filename):
    img = cv2.imread('input/' + filename, 0)
    ret, thresh = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)
    cv2.imwrite('output/' + filename, thresh)


files = glob.glob(('input/*'))

job_queue = Queue()

for file in files:
    job_queue.put(file)

print 'Job queue size: {}'.format(job_queue.qsize())

def worker(queue):
    while not queue.empty():
        filename = queue.get(True)
        filtra_immagine(os.path.basename(filename))

for process in range(4):
    p = Process(target=worker, args=(job_queue,))
    p.start()
    print 'Process: {}'.format(process)


