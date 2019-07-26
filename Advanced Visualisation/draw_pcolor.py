# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import os
import matplotlib.font_manager as font_manager
from matplotlib import ticker
def draw_pcolor(x1,y1,Value,cmap,vmin,vmax,Rd,title2,t,font,img,directory,save_directory,dpi,format_image):
    fig,ax = plt.subplots()
    ax.axis([-Rd, Rd, -Rd, Rd])
    plt.title(title2+',t=%1.1f'% t, fontdict=font)
    if cmap==0:
        c = ax.pcolor(x1,y1,Value,vmin=vmin,vmax=vmax)
    else:
        c = ax.pcolor(x1,y1,Value,cmap=cmap,vmin=vmin,vmax=vmax)
    cb = plt.colorbar(c,extend='both')
    tick_locator = ticker.MaxNLocator(nbins=5) 
    cb.locator = tick_locator 
    cb.update_ticks()
    #font_pcolor = font_manager.FontProperties(family='times new roman', style='italic', size=16)
    #text.set_font_properties(font_legend)
    plt.tick_params(axis='both', which='major', labelsize=25)
    #plt.show()
    fig.set_size_inches(11, 8.7)
    image = img.split('.')
    save_img = save_directory.split('_')
    if not os.path.isdir(directory + '//' +save_directory):
        os.mkdir(directory + '//' + save_directory)
    fig.savefig(directory + '//' + save_directory + '//'+save_img[0]+image[0]+format_image,dpi=int(dpi))
    #plt.close()
    plt.close('all')
    
def draw_grapher(x,y,label,xlabel,ylabel,t,font,font_legend,img,directory,save_directory,dpi,format_image,xlim,ylim):
    xlim = list(map(lambda x: float(x),xlim))
    ylim = list(map(lambda x: float(x),ylim))
    fig,ax = plt.subplots()
    for i in range(len(y)):
        ax.plot(x,y[i],label=label[i])
    
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    plt.title(r't=%1.1f'% t, fontdict=font)
    ax.legend(loc='upper right',prop=font_legend)
    ax.grid(True)
    plt.tick_params(axis='both', which='major', labelsize=25)
    plt.xlabel(xlabel,fontdict=font)
    plt.ylabel(ylabel,fontdict=font)
    #plt.show()
    fig.set_size_inches(11, 8.7)
    image = img.split('.')
    save_img = save_directory.split('_')
    if not os.path.isdir(directory + '//' +save_directory):
        os.mkdir(directory + '//' +save_directory)
    fig.savefig(directory + '//' + save_directory + '//'+save_img[0]+image[0]+format_image,dpi=int(dpi))
    plt.close('all')
    #plt.close(fig)
    #fig.savefig('C://Users//390//Desktop//VKR//ParamDataTVDPolar_menu_0//ParamDataTVDPolar'+image[0]+'.png',format='png',dpi=200)
    #fig.savefig('C://Users//390//Desktop//VKR//ParamDataTVDPolar_menu_0//ParamDataTVDPolar000'+str(img)+'.png',format='png',dpi=200)
    #plt.close()