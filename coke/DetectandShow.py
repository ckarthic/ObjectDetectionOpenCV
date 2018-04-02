# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 17:09:27 2018

@author: rithanya
"""

import os
import cv2

import cv2
import sys
import logging as log
import datetime as dt
from time import sleep
import os
import itertools
import operator

def DetectAndShow(imgfolder = 'NegFromAds/coca cola advertisements/'):
    cokelogo_cascade = "./cascade4/cokelogoorigfullds.xml"
    cokecascade = cv2.CascadeClassifier(cokelogo_cascade)
    for i in os.listdir(imgfolder):
        filepath = imgfolder + i
        img = cv2.imread(filepath)
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cokelogos = detect(cokecascade, gray, 1.25, 6)
        for (x, y, w, h) in cokelogos:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imshow('positive samples',img)
        k = 0xFF & cv2.waitKey(0)
        if k == 27:         # esc to exit
            break
        #print(img.shape)
    

def detect(cascade, gray_,  scaleFactor_ = 1.1, minNeighbors = 5, minsize_ = (30,30)):
    detects = cascade.detectMultiScale(gray_,
                    scaleFactor= scaleFactor_,
                    minNeighbors=5,
                    minSize= minsize_, #(30,30), #(60, 20),
                    flags = cv2.CASCADE_SCALE_IMAGE
                )
    return detects

def DetectAndShowFromVideo(videofile = '../../../Camtasia Studio/CokeCascadeDemo1/CokeCascadeDemo1.mp4',
                           scalefactor = 1.3, minneighbors = 6, minsize = (30,30)):
    cokelogo_cascade = "./cascade4/cokelogoorigfullds.xml"
    cokecascade = cv2.CascadeClassifier(cokelogo_cascade)
    
    video_capture = cv2.VideoCapture(videofile)
    
        
    while video_capture.isOpened():
   
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        cokelogos = detect(cokecascade, gray, scalefactor, minneighbors, minsize)
        for (x, y, w, h) in cokelogos:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
        # Display the resulting frame
        cv2.imshow('Video', frame)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()