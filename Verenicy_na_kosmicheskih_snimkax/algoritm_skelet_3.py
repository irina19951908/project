# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 20:54:08 2018

@author: User
"""
from __future__ import division 
import mahotas as mh 
#import pymorph as pm 
import numpy as np 
import glob
import os 
import math 

import cv2 
from skimage import io 
import scipy 
from skimage import morphology

#complete_path = 'C:/Users/User/Desktop/galaxy/2/binary1/10.bmp' 
#p = 'SDSS9_colored'
#p = 'DSS_colored'
#p = 'DSS2_Blue'
#p = 'DSS2_Red'
#p = 'galex'
#path="C:/Users/User/Desktop/hyperleda/" + p + "/cubeh/binary"
path="C:/Users/User/Desktop/photoshop"
images=glob.glob(path + "/resizeNGC0799_9_del_fon.bmp")
for image in images:
    name = image.split('/')[-1]
    name = name.split('\\')[-1]

    gray = cv2.imread(image,0) 
    originale = gray 

    shape = list(gray.shape) 
    w = int((shape[0]/100)*5) 
    h = int((shape[1]/100)*5) 
    print(w) 
    print(h) 
    element = cv2.getStructuringElement(cv2.MORPH_CROSS,(w,h)) #con 4,4 si vede tutta la stella e riconosce piccoli oggetti 
    from skimage.morphology import square 

    graydilate = np.array(gray, dtype=np.float64) 
    graydilate = morphology.binary_dilation(graydilate, square(w)) 
    graydilate = morphology.binary_dilation(graydilate, square(w)) 
    #graydilate = morphology.binary_dilation(graydilate, square(w))
    #graydilate = morphology.binary_dilation(graydilate, square(w))


    out = morphology.skeletonize(graydilate>0) 
    img = out.astype(float) 
    #cv2.imshow('scikitimage',img) 
    #cv2.waitKey() 
    #img.save('C:/Users/User/Desktop/galaxy/2/binary/kontur/' + '2' + ".jpg")
    #scipy.misc.imsave('C:\\Users\\User\\Desktop\\hyperleda\\' + p + '\\cubeh\\kontur2\\' + name,img)
    scipy.misc.imsave('C:/Users/User/Desktop/photoshop/result/' + '1' + name,img)
