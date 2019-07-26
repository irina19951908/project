# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 21:13:54 2018

@author: User
"""

from PIL import Image
import glob

#p='SDSS9_colored'
#p = 'DSS_colored'
#p = 'DSS2_Blue'
#p = 'DSS2_Red'
#p = 'galex'
#path="C:\\Users\\User\\Desktop\\hyperleda\\" + p + "\\cubeh\\binary"
path="C:\\Users\\User\\Desktop\\photoshop"
images=glob.glob(path + "\\NGC4079_18.bmp")

width = 100
for image in images:
    name = image.split('\\')[-1]
    name = name.split('\\')[-1]
    img = Image.open(image)
    ratio = (width / float(img.size[0]))
    height = int((float(img.size[1]) * float(ratio)))
    img = img.resize((width, height), Image.ANTIALIAS)
    #img.save('C:\\Users\\User\\Desktop\\hyperleda\\' + p + '\\cubeh\\resize\\' + name)
    img.save('C:/Users/User/Desktop/photoshop/' + 'resize' + name)