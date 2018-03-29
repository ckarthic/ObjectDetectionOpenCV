# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 15:18:19 2018

@author: rithanya
"""

import os

def create_pos_n_neg():
    for file_type in ['Neg']:
        for img in os.listdir(file_type):
            if file_type == 'Train':
                line = file_type+'/'+img+' 1 0 0 50 50\n'
                with open('info.data','a') as f:
                    f.write(line)
            elif file_type == 'Neg':
                line = file_type+'/'+img+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)
                    
                    
def create_bgtxt(imgfolder = 'NegFromAds/Patches'):
    for img in os.listdir(imgfolder):
        line = imgfolder + "/" + img + "\n"
        with open('bg.txt','a') as f:
            f.write(line)
            
def create_infodata(imgfolder = 'Source/logo_orig'):
    for img in os.listdir(imgfolder):
        line = imgfolder + "/" + img + " 1 0 0 60 20\n"
        with open('info_pos_orig.data','a') as f:
            f.write(line)