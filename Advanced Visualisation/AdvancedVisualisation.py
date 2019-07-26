#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

This example shows a tooltip on 
a window and a button.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
import matplotlib.pyplot as plt
import os
import numpy as np
from PyQt5.QtWidgets import (QMainWindow,QWidget, QToolTip, 
    QPushButton, QApplication,QLineEdit,QGroupBox,QLabel,QComboBox,QCheckBox,QGraphicsView,QErrorMessage)
from PyQt5.QtGui import QFont,QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from Raspr import MainGrapher


class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
              
    def initUI(self):
        _translate = QtCore.QCoreApplication.translate
        #self.setToolTip('This is a <b>QWidget</b> widget')
        #-------------выбор дикертории------------
        #строка для директории
        self.lineEditDirectory = QtWidgets.QLineEdit(self)
        self.lineEditDirectory.setText(_translate("MainWindow", "Выберите папку"))
        self.lineEditDirectory.setGeometry(QtCore.QRect(10, 10, 471, 31))
        self.lineEditDirectory.setObjectName("lineEditDirectory")
        #кнопака выбора директории
        pushButtonDirectory = QtWidgets.QPushButton(self)
        pushButtonDirectory.setText(_translate("MainWindow", "Выбрать"))
        pushButtonDirectory.setGeometry(QtCore.QRect(490, 10, 131, 28))
        pushButtonDirectory.setObjectName("pushButtonDirectory")
        #--------------------------------------------------------------
        #----------выбор характеристики распределения-----------
        label_19 = QtWidgets.QLabel(self)
        label_19.setText(_translate("MainWindow", "Выбрать характеристику для визуализации"))
        label_19.setGeometry(QtCore.QRect(20, 56, 351, 20))
        label_19.setObjectName("label_19")
        #
        self.comboBoxGrapher = QtWidgets.QComboBox(self)
        self.comboBoxGrapher.addItems(["График распределения параметров системы вдоль r",
                                  "Распределение плотности",
                                  "Распределение возмущения поверхностной плотности",
                                  "Распределение логарифма плотности",
                                  "Распределение радиальной скорости",
                                  "Распределение азимутальной скорости",
                                  "График зависимости Фурье-коэффициентов от времени",
                                  "Распределение радиальной силы",
                                  "Распределение азимутальной силы",
                                  "Распределение возмущения плотности относительно t=0",
                                  "График зависимости логарифма плотности от угла на различных радиусах",
                                  "График зависимости возмущения плотности от времени на различных радиусах"])
        self.comboBoxGrapher.setGeometry(QtCore.QRect(10, 80, 901, 31))
        self.comboBoxGrapher.setEditable(True)
        self.comboBoxGrapher.setCurrentText("")
        self.comboBoxGrapher.setModelColumn(0)
        self.comboBoxGrapher.setObjectName("comboBoxGrapher")
        #-------------------------------------------------------
        #-----------выбор формат выходного изображения-------------------
        #название
        groupBoxImageOut = QtWidgets.QGroupBox(self)
        groupBoxImageOut.setTitle(_translate("MainWindow", "Параметры изображения"))
        groupBoxImageOut.setGeometry(QtCore.QRect(10, 160, 441, 111))
        groupBoxImageOut.setObjectName("groupBoxImageOut")
        #разрешение
        label = QtWidgets.QLabel(groupBoxImageOut)
        label.setText(_translate("MainWindow", "Разрешение:"))
        label.setGeometry(QtCore.QRect(10, 20, 111, 31))
        label.setObjectName("label")
        #
        self.lineEditDpi = QtWidgets.QLineEdit(groupBoxImageOut)
        self.lineEditDpi.setText(_translate("MainWindow", "100"))
        self.lineEditDpi.setGeometry(QtCore.QRect(132, 30, 241, 22))
        self.lineEditDpi.setObjectName("lineEditDpi")
        #
        label_2 = QtWidgets.QLabel(groupBoxImageOut)
        label_2.setText(_translate("MainWindow", "dpi"))
        label_2.setGeometry(QtCore.QRect(390, 30, 31, 21))
        label_2.setObjectName("label_2")
        #формат изображения
        label_4 = QtWidgets.QLabel(groupBoxImageOut)
        label_4.setText(_translate("MainWindow", "Формат изображения:"))
        label_4.setGeometry(QtCore.QRect(10, 45, 181, 31))
        label_4.setObjectName("label_4")
        #
        self.lineEditFormat = QtWidgets.QLineEdit(groupBoxImageOut)
        self.lineEditFormat.setText(_translate("MainWindow", ".png"))
        self.lineEditFormat.setGeometry(QtCore.QRect(132, 70, 241, 22))
        self.lineEditFormat.setObjectName("lineEditFormat")
        #------------------------------------------------------
        #-------------параметры для построения распределений---------------------
        #назвние
        self.groupBoxRaspr = QtWidgets.QGroupBox(self)
        self.groupBoxRaspr.setTitle(_translate("MainWindow", "Параметры построения распределений:"))
        self.groupBoxRaspr.setEnabled(False)
        self.groupBoxRaspr.setGeometry(QtCore.QRect(10, 280, 441, 241))
        self.groupBoxRaspr.setObjectName("groupBoxRaspr")
        #цветовая карта
        label_3 = QtWidgets.QLabel(self.groupBoxRaspr)
        label_3.setText(_translate("MainWindow", "Цветовая шкала:"))
        label_3.setGeometry(QtCore.QRect(10, 20, 131, 21))
        label_3.setObjectName("label_3")
        #
        self.comboBoxColormap = QtWidgets.QComboBox(self.groupBoxRaspr)
        self.comboBoxColormap.addItems(["brg",
                                  "cmrmap",
                                  "cubehelix",
                                  "gist_earth",
                                  "gist_stern",
                                  "gnuplot",
                                  "hsv",
                                  "jet",
                                  "ocean",
                                  "terrain"])
        self.comboBoxColormap.setGeometry(QtCore.QRect(150, 20, 271, 31))
        self.comboBoxColormap.setObjectName("comboBoxColormap")
        #
        self.label_Colormap = QtWidgets.QLabel(self.groupBoxRaspr)
        self.label_Colormap.setGeometry(QtCore.QRect(200, 60, 221, 31))
        self.label_Colormap.setPixmap(QPixmap("C:/Users/390/Python37/Scripts/colormap/brg.PNG"))
        self.label_Colormap.setText("")
        self.label_Colormap.setObjectName("label_Colormap")
        self.cmp=None
        #vmin для шкалы
        label_5 = QtWidgets.QLabel(self.groupBoxRaspr)
        label_5.setText(_translate("MainWindow", "Минимальное значение шкалы:"))
        label_5.setGeometry(QtCore.QRect(10, 100, 261, 16))
        label_5.setObjectName("label_5")
        #
        self.lineEditVmin = QtWidgets.QLineEdit(self.groupBoxRaspr)
        self.lineEditVmin.setText(_translate("MainWindow", "-1"))
        self.lineEditVmin.setGeometry(QtCore.QRect(230, 120, 191, 22))
        self.lineEditVmin.setObjectName("lineEditVmin")
        #vmax для шкалы
        label_6 = QtWidgets.QLabel(self.groupBoxRaspr)
        label_6.setText(_translate("MainWindow", "Максимальное значение шкалы:"))
        label_6.setGeometry(QtCore.QRect(10, 140, 261, 16))
        label_6.setObjectName("label_6")
        #
        self.lineEditVmax = QtWidgets.QLineEdit(self.groupBoxRaspr)
        self.lineEditVmax.setText(_translate("MainWindow", "1"))
        self.lineEditVmax.setGeometry(QtCore.QRect(230, 160, 191, 22))
        self.lineEditVmax.setObjectName("lineEditVmax")
        #Rd область распределения
        label_7 = QtWidgets.QLabel(self.groupBoxRaspr)
        label_7.setText(_translate("MainWindow", "Максимальный радиус диска:"))
        label_7.setGeometry(QtCore.QRect(10, 190, 321, 16))
        label_7.setObjectName("label_7")
        #
        self.lineEditVmax_2 = QtWidgets.QLineEdit(self.groupBoxRaspr)
        self.lineEditVmax_2.setText(_translate("MainWindow", "30"))
        self.lineEditVmax_2.setGeometry(QtCore.QRect(230, 210, 191, 22))
        self.lineEditVmax_2.setObjectName("lineEditVmax_2")
        #-------------------------------------------------
        #---------------график начальных параметров-----------------
        #название
        self.groupBoxNachParametry = QtWidgets.QGroupBox(self)
        self.groupBoxNachParametry.setTitle(_translate("MainWindow", "График распределения параметров системы вдоль r"))
        #self.groupBoxNachParametry.setEnabled(False)
        self.groupBoxNachParametry.setGeometry(QtCore.QRect(460, 420, 441, 131))
        self.groupBoxNachParametry.setObjectName("groupBoxNachParametry")
        #предел по х
        label_8 = QtWidgets.QLabel(self.groupBoxNachParametry)
        label_8.setText(_translate("MainWindow", "Интервал по x:"))
        label_8.setGeometry(QtCore.QRect(210, 30, 131, 16))
        label_8.setObjectName("label_8")
        #
        label_15 = QtWidgets.QLabel(self.groupBoxNachParametry)
        label_15.setText(_translate("MainWindow", "от:"))
        label_15.setGeometry(QtCore.QRect(210, 50, 21, 16))
        label_15.setObjectName("label_15")
        #
        label_16 = QtWidgets.QLabel(self.groupBoxNachParametry)
        label_16.setText(_translate("MainWindow", "до:"))
        label_16.setGeometry(QtCore.QRect(330, 50, 31, 16))
        label_16.setObjectName("label_16")
        #
        self.lineEditXlim1 = QtWidgets.QLineEdit(self.groupBoxNachParametry)
        self.lineEditXlim1.setText(_translate("MainWindow", "0"))
        self.lineEditXlim1.setGeometry(QtCore.QRect(240, 50, 71, 22))
        self.lineEditXlim1.setObjectName("lineEditXlim1")
        #
        self.lineEditXlim_2 = QtWidgets.QLineEdit(self.groupBoxNachParametry)
        self.lineEditXlim_2.setText(_translate("MainWindow", "10"))
        self.lineEditXlim_2.setGeometry(QtCore.QRect(360, 50, 71, 22))
        self.lineEditXlim_2.setObjectName("lineEditXlim_2")
        #предел по у
        label_9 = QtWidgets.QLabel(self.groupBoxNachParametry)
        label_9.setText(_translate("MainWindow", "Интервал по y:"))
        label_9.setGeometry(QtCore.QRect(210, 70, 131, 21))
        label_9.setObjectName("label_9")
        #
        label_17 = QtWidgets.QLabel(self.groupBoxNachParametry)
        label_17.setText(_translate("MainWindow", "от:"))
        label_17.setGeometry(QtCore.QRect(210, 100, 21, 16))
        label_17.setObjectName("label_17")
        #
        label_18 = QtWidgets.QLabel(self.groupBoxNachParametry)
        label_18.setText(_translate("MainWindow", "до:"))
        label_18.setGeometry(QtCore.QRect(330, 100, 31, 16))
        label_18.setObjectName("label_18")
        #
        self.lineEditYlim1 = QtWidgets.QLineEdit(self.groupBoxNachParametry)
        self.lineEditYlim1.setText(_translate("MainWindow", "0"))
        self.lineEditYlim1.setGeometry(QtCore.QRect(240, 100, 71, 22))
        self.lineEditYlim1.setObjectName("lineEditYlim1")
        #
        self.lineEditYlim_2 = QtWidgets.QLineEdit(self.groupBoxNachParametry)
        self.lineEditYlim_2.setText(_translate("MainWindow", "60"))
        self.lineEditYlim_2.setGeometry(QtCore.QRect(360, 100, 71, 22))
        self.lineEditYlim_2.setObjectName("lineEditYlim_2")
        #выбор функций
        # r'$V_phi$+r$Omega$\'
        self.label_vphi = QtWidgets.QLabel(self.groupBoxNachParametry)
        self.label_vphi.setGeometry(QtCore.QRect(30, 40, 101, 21))
        self.label_vphi.setPixmap(QPixmap("C:/Users/390/Python37/Scripts/colormap/1.PNG"))
        self.label_vphi.setText("")
        self.label_vphi.setObjectName("label_vphi")
        self.checkBoxVphi = QtWidgets.QCheckBox(self.groupBoxNachParametry)
        #self.checkBoxVphi.setText(_translate("MainWindow", ''))
        font = QtGui.QFont()
        font.setFamily("Symbol")
        font.setPointSize(10)
        self.checkBoxVphi.setFont(font)
        self.checkBoxVphi.setGeometry(QtCore.QRect(10, 40, 81, 21))
        self.checkBoxVphi.setObjectName("checkBoxVphi")
        #r'$V_phi$\'
        self.label_vphi_2 = QtWidgets.QLabel(self.groupBoxNachParametry)
        self.label_vphi_2.setGeometry(QtCore.QRect(30, 70, 91, 21))
        self.label_vphi_2.setPixmap(QPixmap("C:/Users/390/Python37/Scripts/colormap/2.PNG"))
        self.label_vphi_2.setText("")
        self.label_vphi_2.setObjectName("label_vphi_2")
        self.checkBoxVphi_2 = QtWidgets.QCheckBox(self.groupBoxNachParametry)
        #self.checkBoxVphi_2.setText(_translate("MainWindow", 'u_f'))
        font = QtGui.QFont()
        font.setFamily("Symbol")
        font.setPointSize(10)
        self.checkBoxVphi_2.setFont(font)
        self.checkBoxVphi_2.setGeometry(QtCore.QRect(10, 60, 81, 41))
        self.checkBoxVphi_2.setObjectName("checkBoxVphi_2")
        #r'$\sigma$'
        self.label_vphi_4 = QtWidgets.QLabel(self.groupBoxNachParametry)
        self.label_vphi_4.setGeometry(QtCore.QRect(30, 100, 91, 21))
        self.label_vphi_4.setPixmap(QPixmap("C:/Users/390/Python37/Scripts/colormap/5.PNG"))
        self.label_vphi_4.setText("")
        self.label_vphi_4.setObjectName("label_vphi_4")
        self.checkBoxSigma = QtWidgets.QCheckBox(self.groupBoxNachParametry)
        #self.checkBoxSigma.setText(_translate("MainWindow", 's'))
        font = QtGui.QFont()
        font.setFamily("Symbol")
        font.setPointSize(10)
        self.checkBoxSigma.setFont(font)
        self.checkBoxSigma.setGeometry(QtCore.QRect(10, 100, 81, 20))
        self.checkBoxSigma.setObjectName("checkBoxSigma")
        #r'$\omega$'
        self.label_vphi_5 = QtWidgets.QLabel(self.groupBoxNachParametry)
        self.label_vphi_5.setGeometry(QtCore.QRect(160, 40, 41, 21))
        self.label_vphi_5.setPixmap(QPixmap("C:/Users/390/Python37/Scripts/colormap/4.PNG"))
        self.label_vphi_5.setText("")
        self.label_vphi_5.setObjectName("label_vphi_5")
        self.checkBoxOmega = QtWidgets.QCheckBox(self.groupBoxNachParametry)
        #self.checkBoxOmega.setText(_translate("MainWindow", 'W'))
        font = QtGui.QFont()
        font.setFamily("Symbol")
        font.setPointSize(10)
        self.checkBoxOmega.setFont(font)
        self.checkBoxOmega.setGeometry(QtCore.QRect(140, 40, 81, 20))
        self.checkBoxOmega.setObjectName("checkBoxOmega")
        #r'$\kappa$'
        self.label_vphi_6 = QtWidgets.QLabel(self.groupBoxNachParametry)
        self.label_vphi_6.setGeometry(QtCore.QRect(160, 70, 41, 21))
        self.label_vphi_6.setPixmap(QPixmap("C:/Users/390/Python37/Scripts/colormap/6.PNG"))
        self.label_vphi_6.setText("")
        self.label_vphi_6.setObjectName("label_vphi_6")
        self.checkBoxKappa = QtWidgets.QCheckBox(self.groupBoxNachParametry)
        #self.checkBoxKappa.setText(_translate("MainWindow", 'k'))
        font = QtGui.QFont()
        font.setFamily("Symbol")
        font.setPointSize(10)
        self.checkBoxKappa.setFont(font)
        self.checkBoxKappa.setGeometry(QtCore.QRect(140, 70, 81, 20))
        self.checkBoxKappa.setObjectName("checkBoxKappa")
        #r'$Q_T$'
        self.checkBoxQt = QtWidgets.QCheckBox(self.groupBoxNachParametry)
        self.label_vphi_3 = QtWidgets.QLabel(self.groupBoxNachParametry)
        self.label_vphi_3.setGeometry(QtCore.QRect(160, 100, 51, 21))
        self.label_vphi_3.setPixmap(QPixmap("C:/Users/390/Python37/Scripts/colormap/3.PNG"))
        self.label_vphi_3.setText("")
        self.label_vphi_3.setObjectName("label_vphi_3")
        #self.checkBoxQt.setText(_translate("MainWindow", 'Q_T'))
        self.checkBoxQt.setGeometry(QtCore.QRect(140, 100, 81, 20))
        self.checkBoxQt.setObjectName("checkBoxQt")
        #----------------------------------------------------
        #-----------временные зависимости------------
        #название
        self.groupBoxTimeGrapher = QtWidgets.QGroupBox(self)
        self.groupBoxTimeGrapher.setTitle(_translate("MainWindow", "Зависимости характеристик от времени"))
        self.groupBoxTimeGrapher.setEnabled(False)
        self.groupBoxTimeGrapher.setGeometry(QtCore.QRect(460, 160, 451, 141))
        self.groupBoxTimeGrapher.setObjectName("groupBoxTimeGrapher")
        #выбор радиусов
        self.lineEditRadTimeGrapher = QtWidgets.QLineEdit(self.groupBoxTimeGrapher)
        self.lineEditRadTimeGrapher.setText(_translate("MainWindow", "6,12,18,24,30"))
        self.lineEditRadTimeGrapher.setGeometry(QtCore.QRect(210, 20, 231, 22))
        self.lineEditRadTimeGrapher.setObjectName("lineEditRadTimeGrapher")
        #
        label_10 = QtWidgets.QLabel(self.groupBoxTimeGrapher)
        label_10.setText(_translate("MainWindow", "Радиусы:"))
        label_10.setGeometry(QtCore.QRect(10, 20, 71, 21))
        label_10.setObjectName("label_10")
        #время t
        label_14 = QtWidgets.QLabel(self.groupBoxTimeGrapher)
        label_14.setText(_translate("MainWindow", "Максимальное t:"))
        label_14.setGeometry(QtCore.QRect(10, 50, 131, 16))
        label_14.setObjectName("label_14")
        #
        self.lineEditTime = QtWidgets.QLineEdit(self.groupBoxTimeGrapher)
        self.lineEditTime.setGeometry(QtCore.QRect(210, 50, 231, 20))
        self.lineEditTime.setObjectName("lineEdit")
        #для Фурье
        label_11 = QtWidgets.QLabel(self.groupBoxTimeGrapher)
        label_11.setText(_translate("MainWindow", "Для графика изменения Фурье-коэффициентов"))
        label_11.setGeometry(QtCore.QRect(10, 70, 391, 31))
        label_11.setObjectName("label_11")
        #Выбор мод
        label_12 = QtWidgets.QLabel(self.groupBoxTimeGrapher)
        label_12.setText(_translate("MainWindow", "Выбор мод:"))
        label_12.setGeometry(QtCore.QRect(10, 100, 91, 21))
        label_12.setObjectName("label_12")
        #
        self.checkBox_1 = QtWidgets.QCheckBox(self.groupBoxTimeGrapher)
        self.checkBox_1.setText(_translate("MainWindow", "1"))
        self.checkBox_1.setGeometry(QtCore.QRect(210, 100, 31, 20))
        self.checkBox_1.setObjectName("checkBox_1")
        #
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBoxTimeGrapher)
        self.checkBox_2.setText(_translate("MainWindow", "2"))
        self.checkBox_2.setGeometry(QtCore.QRect(250, 100, 31, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        #
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBoxTimeGrapher)
        self.checkBox_3.setText(_translate("MainWindow", "3"))
        self.checkBox_3.setGeometry(QtCore.QRect(290, 100, 31, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        #
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBoxTimeGrapher)
        self.checkBox_4.setText(_translate("MainWindow", "4"))
        self.checkBox_4.setGeometry(QtCore.QRect(330, 100, 31, 20))
        self.checkBox_4.setObjectName("checkBox_4")
        #
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBoxTimeGrapher)
        self.checkBox_5.setText(_translate("MainWindow", "5"))
        self.checkBox_5.setGeometry(QtCore.QRect(370, 100, 31, 20))
        self.checkBox_5.setObjectName("checkBox_5")
        #
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBoxTimeGrapher)
        self.checkBox_6.setText(_translate("MainWindow", "6"))
        self.checkBox_6.setGeometry(QtCore.QRect(410, 100, 31, 20))
        self.checkBox_6.setObjectName("checkBox_6")
        #--------------------------------------------
        #-------------график логарифма плотности от угла
        #название
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setTitle(_translate("MainWindow", "График зависимости логарифма плотности от угла"))
        self.groupBox.setEnabled(False)
        self.groupBox.setGeometry(QtCore.QRect(460, 330, 451, 71))
        self.groupBox.setObjectName("groupBox")
        #выбор радиусов
        label_13 = QtWidgets.QLabel(self.groupBox)
        label_13.setText(_translate("MainWindow", "Радиусы:"))
        label_13.setGeometry(QtCore.QRect(10, 30, 81, 21))
        label_13.setObjectName("label_13")
        #
        self.lineEditRadTimeGrapher_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditRadTimeGrapher_2.setText(_translate("MainWindow", "6,12,18,24,30"))
        self.lineEditRadTimeGrapher_2.setGeometry(QtCore.QRect(210, 30, 231, 22))
        self.lineEditRadTimeGrapher_2.setObjectName("lineEditRadTimeGrapher_2")
        #-------------------------------------------
        #-----------кнопка выхода-----------
        pushButtonQuit = QtWidgets.QPushButton(self)
        pushButtonQuit.setText(_translate("MainWindow", "Выйти"))
        pushButtonQuit.setGeometry(QtCore.QRect(790, 10, 121, 28))
        pushButtonQuit.setObjectName("pushButtonQuit")
        #---------------------
        #---------------кнопка построения-------------------
        pushButtonCreate = QtWidgets.QPushButton(self)
        pushButtonCreate.setText(_translate("MainWindow", "Построить"))
        pushButtonCreate.setGeometry(QtCore.QRect(640, 10, 131, 28))
        pushButtonCreate.setObjectName("pushButtonCreate")
        #--------------------------------------
        #-------------когда графики готовы, выводится сообщение-----------
        self.label_create = QtWidgets.QLabel(self)
        self.label_create.setGeometry(QtCore.QRect(10, 50, 201, 16))
        self.label_create.setText("")
        self.label_create.setTextFormat(QtCore.Qt.AutoText)
        self.label_create.setObjectName("label_create")
        #-----------------
        self.setFixedSize(920, 668)
        self.setWindowTitle('Advanced Visualisation')  
        font1 = QtGui.QFont()
        font1.setPointSize(10)
        self.setFont(font1)
        self.show()
        #--------------выбор colormap---------------
        self.comboBoxColormap.activated[str].connect(self.onActivatedCombo3)
        #-------------вызов выбора директории--------
        pushButtonDirectory.clicked.connect(self.browse_folder)
        #------------действие при выборе графика------------------
        self.comboBoxGrapher.activated[str].connect(self.onActivatedCombo2)
        pushButtonCreate.clicked.connect(self.onActivatedCombo)
        #-----------кнопка выхода---------------
        pushButtonQuit.clicked.connect(sys.exit)
    #----------функция выбора директории------------
    def browse_folder(self):
        self.directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        # открыть диалог выбора директории и установить значение переменной
        # равной пути к выбранной директории
        if self.directory:  # не продолжать выполнение, если пользователь не выбрал директорию
            self.lineEditDirectory.setText(self.directory)
    #---------------функция выбор colormap----------------------
    def onActivatedCombo3(self):
        index = self.comboBoxColormap.currentIndex()
        if index==0:
            self.cmp=plt.cm.brg
            self.label_Colormap.setPixmap(QPixmap("C:/Users/390/Python37/Scripts/colormap/brg.PNG"))
        if index==1:
            self.cmp=plt.cm.CMRmap
            self.label_Colormap.setPixmap(QPixmap("C:/Users/390/Python37/Scripts/colormap/cmrmap.PNG"))
        if index==2:
            self.cmp=plt.cm.cubehelix
            self.label_Colormap.setPixmap(QPixmap("C:/Users/390/Python37/Scripts/colormap/cubehelix.PNG"))
        if index==3:
            self.cmp=plt.cm.gist_earth
            self.label_Colormap.setPixmap(QPixmap("C:/Users/390/Python37/Scripts/colormap/gist_earth.PNG"))
        if index==4:
            self.cmp=plt.cm.gist_stern
            self.label_Colormap.setPixmap(QPixmap("C:/Users/390/Python37/Scripts/colormap/gist_stern.PNG"))
        if index==5:
            self.cmp=plt.cm.gnuplot
            self.label_Colormap.setPixmap(QPixmap("C:/Users/390/Python37/Scripts/colormap/gnuplot.PNG"))
        if index==6:
            self.cmp=plt.cm.hsv
            self.label_Colormap.setPixmap(QPixmap("C:/Users/390/Python37/Scripts/colormap/hsv.PNG"))
        if index==7:
            self.cmp=plt.cm.jet
            self.label_Colormap.setPixmap(QPixmap("C:/Users/390/Python37/Scripts/colormap/jet.PNG"))
        if index==8:
            self.cmp=plt.cm.ocean
            self.label_Colormap.setPixmap(QPixmap("C:/Users/390/Python37/Scripts/colormap/ocean.PNG"))
        if index==9:
            self.cmp=plt.cm.terrain
            self.label_Colormap.setPixmap(QPixmap("C:/Users/390/Python37/Scripts/colormap/terrain.PNG"))
    #-----------------функция активации группбоксок----------------
    def onActivatedCombo2(self):
        index = self.comboBoxGrapher.currentIndex()
        if index==0:
            self.groupBoxNachParametry.setEnabled(True)
            self.groupBoxRaspr.setEnabled(False)
            self.groupBoxTimeGrapher.setEnabled(False)
            self.groupBox.setEnabled(False)
        elif index==1 or index==2 or index==3 or index==4 or index==5 or index==7 or index==8 or index==9:
            self.groupBoxRaspr.setEnabled(True)
            self.groupBoxTimeGrapher.setEnabled(False)
            self.groupBox.setEnabled(False)
            self.groupBoxNachParametry.setEnabled(False)
        elif index==6 or index==11:
            self.groupBoxTimeGrapher.setEnabled(True)
            self.groupBoxRaspr.setEnabled(False)
            self.groupBox.setEnabled(False)
            self.groupBoxNachParametry.setEnabled(False)
        elif index==10:
            self.groupBox.setEnabled(True)
            self.groupBoxRaspr.setEnabled(False)
            self.groupBoxTimeGrapher.setEnabled(False)
            self.groupBoxNachParametry.setEnabled(False)
    #-----------выбор гафика, при выборе сразу выводит----------------------
    def onActivatedCombo(self):
        index = self.comboBoxGrapher.currentIndex()
        if self.lineEditDirectory.text()=="Выберите папку":
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.showMessage('Выберите папку с файлами!')
        else:# index!=0:
            #формат выходного изображения
            dpi = self.lineEditDpi.text()
            format_image = self.lineEditFormat.text()
            #директория
            der = self.directory
            #распределения
            if not self.cmp:
                colormap=plt.cm.jet
            else:
                colormap = self.cmp     
            vmin = self.lineEditVmin.text()
            vmax = self.lineEditVmax.text()
            Rd = self.lineEditVmax_2.text()
            #временные графики
            radius = self.lineEditRadTimeGrapher.text()
            timeEnd = self.lineEditTime.text()
            m_1, m_2,m_3,m_4,m_5,m_6=0,0,0,0,0,0
            if self.checkBox_1.isChecked():
                m_1 = 1
            if self.checkBox_2.isChecked():
                m_2 = 1
            if self.checkBox_3.isChecked():
                m_3 = 1
            if self.checkBox_4.isChecked():
                m_4 = 1
            if self.checkBox_5.isChecked():
                m_5 = 1
            if self.checkBox_6.isChecked():
                m_6 = 1
            #графики логарифма плотности от угла
            radius2 = self.lineEditRadTimeGrapher_2.text()
            #начальные параметры
            xlim1 = self.lineEditXlim1.text()
            xlim2 = self.lineEditXlim_2.text()
            ylim1 = self.lineEditYlim1.text()
            ylim2 = self.lineEditYlim_2.text()
            Vphi, vphi_2,sigma,omega,kappa,qt=0,0,0,0,0,0
            if self.checkBoxVphi.isChecked():
                Vphi = 1
            if self.checkBoxVphi_2.isChecked():
                vphi_2 = 1
            if self.checkBoxSigma.isChecked():
                sigma = 1
            if self.checkBoxOmega.isChecked():
                omega = 1
            if self.checkBoxKappa.isChecked():
                kappa = 1
            if self.checkBoxQt.isChecked():
                qt = 1
            #проверка максимального t
            if not self.lineEditTime.text():
                timeEnd = -1
                MainGrapher(der,index,dpi,format_image,colormap,float(vmin),float(vmax),float(Rd),radius,radius2,
                        [xlim1,xlim2],[ylim1,ylim2],[Vphi,vphi_2,sigma,omega,kappa,qt],[m_1,m_2,m_3,m_4,m_5,m_6],timeEnd)
                #self.label_create.setText("ГОТОВО!!!")
            else:
                files = os.listdir(der)
                dat = filter(lambda x: x.endswith('.dat'), files)
                l = list(dat)
                dat = filter(lambda x: x.endswith('.dat'), files)
                length = len(l)
                Input = open(der + '//' + l[length-1],'rb')
                gam = np.fromfile(Input,np.float64,1)
                t = np.fromfile(Input,np.float64,1)
                Input.close()
                if float(timeEnd)>t:
                    error_dialog = QtWidgets.QErrorMessage(self)
                    MainGrapher(der,index,dpi,format_image,colormap,float(vmin),float(vmax),float(Rd),radius,radius2,
                        [xlim1,xlim2],[ylim1,ylim2],[Vphi,vphi_2,sigma,omega,kappa,qt],[m_1,m_2,m_3,m_4,m_5,m_6],timeEnd)
                    error_dialog.showMessage('Указанное значение t превышает время выбранного расчета! Расчет будет произведен до t=%.2f'%t)
                    #self.label_create.setText("ГОТОВО!!!")
                else:
                    MainGrapher(der,index,dpi,format_image,colormap,float(vmin),float(vmax),float(Rd),radius,radius2,
                        [xlim1,xlim2],[ylim1,ylim2],[Vphi,vphi_2,sigma,omega,kappa,qt],[m_1,m_2,m_3,m_4,m_5,m_6],timeEnd)
                    #self.label_create.setText("ГОТОВО!!!")
            
    
    
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())