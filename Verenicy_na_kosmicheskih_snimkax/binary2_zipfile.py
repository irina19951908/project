# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 14:15:53 2018

@author: User
"""

#бинаризация изображения

#import random
import glob
from PIL import Image, ImageDraw #Подключим необходимые библиотеки. 
import zipfile
import os

#image = Image.open("C:/Users/User/Desktop/image/original.jpg") #Открываем изображение. 
#path="C:/Users/User/Desktop/image/original"
#images=glob.glob(path + "/*.jpg")
zip = zipfile(os.path, 'r')
n=0
for i in range(len(os.filepath)-1,0,-1):
    if(os.filepath[i]!="/"):
        n+=1

zip.extractall(os.filepath[:n])
#draw = ImageDraw.Draw(image) #Создаем инструмент для рисования. 
#width = image.size[0] #Определяем ширину. 
#height = image.size[1] #Определяем высоту. 	
#pix = image.load() #Выгружаем значения пикселей.

#оттенки серого
'''
for i in range(width):
    for j in range(height):
        a = pix[i, j][0]
        b = pix[i, j][1]
        c = pix[i, j][2]
        S = (a + b + c) // 3
        draw.point((i, j), (S, S, S))
'''
number = 0
for file in zip.namelist():
    img = Image.open(os.filepath[:n] + '\\' +file)
    draw = ImageDraw.Draw(img) #Создаем инструмент для рисования. 
    width = img.size[0] #Определяем ширину. 
    height = img.size[1] #Определяем высоту. 	
    pix = img.load() #Выгружаем значения пикселей.
    #черное-белое изображения
    factor = 50#int(input('factor:'))
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = a + b + c
        
            if (S < (((255 + factor) // 2) * 3)): #если меньше - белый
                a, b, c = 255, 255, 255
            else:
                a, b, c = 0, 0, 0
            draw.point((i, j), (a, b, c))
    
    
            
    number=number+1
    img.save(os.filepath[:n] + '\\' + 'binary_image' + '\\' + file)
    del draw
'''
number = 0
for image in images:
    img = Image.open(image)
    draw = ImageDraw.Draw(img) #Создаем инструмент для рисования. 
    width = img.size[0] #Определяем ширину. 
    height = img.size[1] #Определяем высоту. 	
    pix = img.load() #Выгружаем значения пикселей.
    #черное-белое изображения
    factor = 50#int(input('factor:'))
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = a + b + c
        
            if (S < (((255 + factor) // 2) * 3)): #если меньше - белый
                a, b, c = 255, 255, 255
            else:
                a, b, c = 0, 0, 0
            draw.point((i, j), (a, b, c))
    
    
            
    number=number+1
    img.save(path + "/binary2/" + str(number) + ".jpg")
    del draw
'''
#сохраняем результат
#image.save("C:/Users/User/Desktop/image/result3factor10.jpg", "JPEG")
#del draw