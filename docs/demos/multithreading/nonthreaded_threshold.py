#!/usr/bin/python2.7

import glob
import os

import cv2

def filtra_immagine(filename):
    img = cv2.imread('input/' + filename, 0)
    ret, thresh = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)
    cv2.imwrite('output/' + filename, thresh)


files = glob.glob(('input/*'))

print 'Job queue size: {}'.format(len(files))

for file in files:

    filtra_immagine(os.path.basename(file))


