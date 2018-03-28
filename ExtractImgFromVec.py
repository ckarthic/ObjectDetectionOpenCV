# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 00:28:37 2018

@author: rithanya
"""

import struct,array

import cv2
import numpy as np
import os

def ExtractImgFromVec(root = "C:/Users/rithanya/Documents/Python/Industrial_Safety",
            fn="./pos.vec", width=20, height=20, resize=4.0):
    
    #print(len(fn.split('/')))
    assert len(fn.split('/')) == 3, "fn should be like './akash/2.vec'"
    #os.chdir(root)
    f = open(fn,'rb')
    HEADERTYP = '<iihh' # img count, img size, min, max
    
    # read header
    imgcount,imgsize,_,_ = struct.unpack(HEADERTYP, f.read(12))
    
    for i in range(imgcount):
        img  = np.zeros((height,width),np.uint8)
    
        f.read(1) # read gap byte
        
        data = array.array('h')
        
        ###  buf = f.read(imgsize*2)
        ###  data.fromstring(buf)
        
        data.fromfile(f,imgsize)
        i = i
        for r in range(height):
            for c in range(width):
                img[r,c] = data[r * width + c]
        
        img = cv2.resize(img, (0,0), fx=resize, fy=resize, interpolation=cv2.INTER_LINEAR)
        vec_prefix = fn.split('/')[-1].split('.')[0]
        pathtosave = "./" +fn.split('/')[1] + "/samples" +  "/vec_" + vec_prefix + "_" + str(i) + '.jpg'
        #print(pathtosave)
        cv2.imwrite(pathtosave, img)
        i = i + 1
        #cv2.imshow('vec_img',img)
        #k = 0xFF & cv2.waitKey(0)
        #if k == 27:         # esc to exit
        #  break
    
def showvec(root = "C:/Users/rithanya/Documents/Python/Industrial_Safety/Coke",
            fn="posfrom1.vec", width=50, height=50, resize=4.0):
  f = open(fn,'rb')
  HEADERTYP = '<iihh' # img count, img size, min, max

  # read header
  imgcount,imgsize,_,_ = struct.unpack(HEADERTYP, f.read(12))

  for i in range(imgcount):
    img  = np.zeros((height,width),np.uint8)

    f.read(1) # read gap byte

    data = array.array('h')

    ###  buf = f.read(imgsize*2)
    ###  data.fromstring(buf)

    data.fromfile(f,imgsize)

    for r in range(height):
      for c in range(width):
        img[r,c] = data[r * width + c]

    img = cv2.resize(img, (0,0), fx=resize, fy=resize, interpolation=cv2.INTER_LINEAR)
    cv2.imshow('vec_img',img)
    k = 0xFF & cv2.waitKey(0)
    if k == 27:         # esc to exit
      break
  
def ExtractImgForAllVec(start = 1, end = 5, folder = 'akash'):
    while( start <= end):
        fn = './' + folder + '/' + str(start) + '.vec'
        #print(fn)
        ExtractImgFromVec(fn = fn)
        start = start + 1
    
        