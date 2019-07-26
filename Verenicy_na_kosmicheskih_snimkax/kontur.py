# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 15:49:55 2018

@author: User
"""

#контурирование

#import random
import glob
from PIL import Image, ImageDraw #Подключим необходимые библиотеки. 
import numpy
import scipy
from scipy import ndimage

#image = Image.open("C:/Users/User/Desktop/image/original.jpg") #Открываем изображение. 
path="C:/Users/User/Desktop/galaxy/2/binary"
images=glob.glob(path + "/*.jpg")

number=0
for image in images:
    #img = Image.open(image)
    im = scipy.misc.imread(image)
    im = im.astype('int32')
    dx = ndimage.sobel(im, 1)  # horizontal derivative
    dy = ndimage.sobel(im, 0)  # vertical derivative
    mag = numpy.hypot(dx, dy)  # magnitude
    mag *= 255.0 / numpy.max(mag)  # normalize (Q&D)
   
            
              
            
    number=number+1
    scipy.misc.imsave(path + "/kontur/" + str(number) + ".jpg",mag)
    #del draw

#сохраняем результат
#image.save("C:/Users/User/Desktop/image/result3factor10.jpg", "JPEG")
#del draw