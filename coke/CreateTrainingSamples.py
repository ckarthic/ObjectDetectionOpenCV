# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 23:19:39 2018

@author: rithanya
"""

import os
import cv2
#import matplotlib
#import numpy as np

def ExtractCropLogo(root = "C:/Users/rithanya/Documents/Python/Industrial_Safety/coke",
                    datafile = "info_pos_square.data", pathtowrite = "./Source/logo_square/"):

    #Set the current directory to the root
    os.chdir(root)
    #Verify the path is correct
    print(os.getcwd())
    
    #open datafile
    f = open(datafile)
    content = f.read()
    i = 1
    for l in content.split('\n'):
        
        words = l.split()
        #print(len(words))
        if(len(words) >= 6):
            #print(words)
            img_path = ' '.join(words[:-5])
            img_path = img_path.replace('\\','/')
            print(img_path)
            img = cv2.imread(img_path,0) # read the image using OpenCV
            #print(type(img))
            face = [int(w) for w in words[-4:]]
            #face =  np.asarray(face)
            x,y,w,h = face
            #print(len(face))
            #print(face)
            
            facegrab = img[y:y+h, x:x+w]
            cv2.imwrite( pathtowrite + str(i) + '.jpg', facegrab)
            i = i + 1
            #print(img_path)
            #print(words[-4:])
            
            #print( [list(map(int, x)) for x in words[-4:]])
        #print(type(content))
        #for l in f.readlines():
        #    print(l)
