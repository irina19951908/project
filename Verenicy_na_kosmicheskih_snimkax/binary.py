# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 14:15:53 2018

@author: User
"""

#бинаризация изображения

#import random
import glob
from PIL import Image, ImageDraw #Подключим необходимые библиотеки. 


#image = Image.open("C:/Users/User/Desktop/image/original.jpg") #Открываем изображение. 
path="C:/Users/User/Desktop/galaxy/2"
#path="C:/Users/User/Desktop/image"
images=glob.glob(path + "/*.jpg")
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
factor = 10
number = 0
for image in images:
    img = Image.open(image)
    draw = ImageDraw.Draw(img) #Создаем инструмент для рисования. 
    width = img.size[0] #Определяем ширину. 
    height = img.size[1] #Определяем высоту. 	
    pix = img.load() #Выгружаем значения пикселей.
    #черное-белое изображения
    #int(input('factor:'))
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = a + b + c
        
            if (S > (((255 + factor) // 2) * 3)): #если меньше - белый
                a, b, c = 255, 255, 255
            else:
                a, b, c = 0, 0, 0
            draw.point((i, j), (a, b, c))
    
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            '''
            if (a == 0 and i>7 and j>7 and i<(width-7) and j<(height-7)):
                for ind in range(7):
                    if (pix[i-ind,j-ind][0] == 255 and pix[i-ind,j][0] == 255 and pix[i-ind,j+ind][0] == 255 and pix[i,j-ind][0] == 255 and pix[i,j+ind][0] == 255 and pix[i+ind,j-ind][0] == 255 and pix[i+ind,j][0] == 255 and pix[i+ind,j+ind][0] == 255):
                        a = 255
                        b = 255
                        c = 255
            draw.point((i, j), (a, b, c))
            '''
            prov=20
            if (a == 255 and i>prov and j>prov and i<(width-prov) and j<(height-prov)):
                for ind in range(prov):
                    if (pix[i-ind,j-ind][0] == 0 and pix[i-ind,j][0] == 0 and pix[i-ind,j+ind][0] == 0 and pix[i,j-ind][0] == 0 and pix[i,j+ind][0] == 0 and pix[i+ind,j-ind][0] == 0 and pix[i+ind,j][0] == 0 and pix[i+ind,j+ind][0] == 0):
                        a = 0
                        b = 0
                        c = 0
            draw.point((i, j), (a, b, c))
                    
            
    number=number+1
    img.save(path + "/binary/" + str(number) + ".jpg")
    #img.save(path + "/" + str(number) + ".jpg")
    del draw

#сохраняем результат
#image.save("C:/Users/User/Desktop/image/result3factor10.jpg", "JPEG")
#del draw