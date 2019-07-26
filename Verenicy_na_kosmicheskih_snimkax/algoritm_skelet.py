# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 19:15:12 2018

@author: User
"""

#селетирование
import glob
import cv2
import os
from PIL import Image, ImageDraw #Подключим необходимые библиотеки. 
path="C:/Users/User/Desktop/galaxy/2"
images=glob.glob(path + "/2.jpg")
black = [] #массив черных пикселей определенного значения по х
x = [] #массив х

factor = 150
number = 0
for image in images:
    img = cv2.imread(image)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.bitwise_not(img_gray, img_gray)
    ret, thresh = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY)
    _, contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    rects = [cv2.boundingRect(cnt) for cnt in contours]
    top_x = min([x for (x, y, w, h) in rects])
    top_y = min([y for (x, y, w, h) in rects])
    bottom_x = max([x+w for (x, y, w, h) in rects])
    bottom_y = max([y+h for (x, y, w, h) in rects])
    img_gray = thresh[top_y:bottom_y, top_x:bottom_x]
    
    cv2.bitwise_not(img_gray, img_gray)
    
    img_gray = cv2.copyMakeBorder(img_gray, img_gray.shape[0], 0, img_gray.shape[1], img.shape[1], cv2.BORDER_CONSTANT,
							  value=[255, 255, 255])
    
    #image = os.path.split(image)[0]
    cv2.imwrite(path + "/kontur/" + 'prob2' + ".jpg", img_gray)
    #return img_name + "/binary.png"
            #draw.point((i, mid), (0, 0, 0))
    
    
            
    #number=number+1
    #img.save(path + "/kontur/" + 'prob' + ".bmp")
    #del draw

