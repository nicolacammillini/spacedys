#!/usr/bin/python2.7

import glob
import os

import cv2

def filtra_immagine(filename):
    img = cv2.imread('input/' + filename, 0)
    img = cv2.medianBlur(img, 5)
    thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
    cv2.imwrite('output/' + filename, thresh)


files = glob.glob(('input/*'))

print 'Job queue size: {}'.format(len(files))

for file in files:

    filtra_immagine(os.path.basename(file))


