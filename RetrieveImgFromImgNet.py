# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 14:25:30 2018

@author: rithanya
"""

#http://www.image-net.org/synset?wnid=n07928696

import urllib.request
import cv2
import numpy as np
import os

def store_raw_images():
    pos_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07928696'   
    pos_image_urls = urllib.request.urlopen(pos_images_link).read().decode()
    pic_num = 1
    
    if not os.path.exists('pos_imgnet'):
        os.makedirs('pos_imgnet')
        
    for i in pos_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, "pos_imgnet/"+str(pic_num)+".jpg")
            img = cv2.imread("pos_imgnet/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            # should be larger than samples / pos pic (so we can place our image on it)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("pos/"+str(pic_num)+".jpg",resized_image)
            pic_num += 1
            
        except Exception as e:
            print(str(e))  