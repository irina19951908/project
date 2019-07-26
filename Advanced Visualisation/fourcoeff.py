# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import math
import os
def FourCoeff(directory,number_of_files,dat,font,font_legend,dpi,format_image,mody,timeEnd):
    t = np.zeros((number_of_files,1))
    
    gamp_1 = np.zeros((number_of_files,1))
    gamp_2 = np.zeros((number_of_files,1))
    gamp_3 = np.zeros((number_of_files,1))
    gamp_4 = np.zeros((number_of_files,1))
    gamp_5 = np.zeros((number_of_files,1))
    gamp_6 = np.zeros((number_of_files,1))
    
    '''
    s1 = np.zeros((1,1))
    s2 = np.zeros((1,1))
    s3 = np.zeros((1,1))
    s4 = np.zeros((1,1))
    s5 = np.zeros((1,1))
    s6 = np.zeros((1,1))
    '''
    
    k=0
    for img in dat:
        Input = open(directory + '//' + img,'rb')
        
        gam = np.fromfile(Input,np.float64,1)
        t[k] = np.fromfile(Input,np.float64,1)
        nrad = np.fromfile(Input,np.int32,1)
        nphi = np.fromfile(Input,np.int32,1)
        nz = np.fromfile(Input,np.int32,1)
        
        rad = np.fromfile(Input,np.float64,int(nrad))
        phi = np.fromfile(Input,np.float64,int(nphi))
        z = np.fromfile(Input,np.float64,int(nz))
        
        d = np.fromfile(Input,np.float64,(int(nrad)+4)*(int(nphi)+4)*int(nz)).reshape((int(nrad)+4,int(nphi)+4))
        d = d[3:int(nrad+4)-1,3:int(nphi+4)-1]
        Input.close()
        
        dr = rad[1]-rad[0]
        #dphi = phi[1]-phi[0]
        
        disk_mass = 0.0
        DS = np.zeros(nrad)
        
        for i in range(int(nrad)):
            DS[i] = math.pi*((rad[i]+0.5*dr)*(rad[i]+0.5*dr)-(rad[i]-0.5*dr)*(rad[i]-0.5*dr))/nphi
            for j in range(int(nphi)):
                disk_mass=disk_mass+d[i,j]*DS[i]
                
        #disp(disk_mass)
        s1=0.0
        s2=0.0
        s3=0.0
        s4=0.0
        s5=0.0
        s6=0.0
        
        s1_ = 0.0
        s2_ = 0.0
        s3_ = 0.0
        s4_ = 0.0
        s5_ = 0.0
        s6_ = 0.0
        
        for i in range(int(nrad)):
            for j in range(int(nphi)):
                s1 = s1+d[i,j]*math.cos(1*phi[j])*DS[i]
                s2 = s2+d[i,j]*math.cos(2*phi[j])*DS[i]
                s3 = s3+d[i,j]*math.cos(3*phi[j])*DS[i]
                s4 = s4+d[i,j]*math.cos(4*phi[j])*DS[i]
                s5 = s5+d[i,j]*math.cos(5*phi[j])*DS[i]
                s6 = s6+d[i,j]*math.cos(6*phi[j])*DS[i]
                
                s1_ = s1_ +d[i,j]*math.sin(1*phi[j])*DS[i]
                s2_ = s2_ +d[i,j]*math.sin(2*phi[j])*DS[i]
                s3_ = s3_ +d[i,j]*math.sin(3*phi[j])*DS[i]
                s4_ = s4_ +d[i,j]*math.sin(4*phi[j])*DS[i]
                s5_ = s5_ +d[i,j]*math.sin(5*phi[j])*DS[i]
                s6_ = s6_ +d[i,j]*math.sin(6*phi[j])*DS[i]
        
        gamp_1[k] = math.sqrt((pow(s1,2)+pow(s1_,2)))
        gamp_2[k] = math.sqrt((pow(s2,2)+pow(s2_,2)))
        gamp_3[k] = math.sqrt((pow(s3,2)+pow(s3_,2)))
        gamp_4[k] = math.sqrt((pow(s4,2)+pow(s4_,2)))
        gamp_5[k] = math.sqrt((pow(s5,2)+pow(s5_,2)))
        gamp_6[k] = math.sqrt((pow(s6,2)+pow(s6_,2)))
        '''  
        gamp_1[k+1] = pow((pow(s1,2)+pow(s1_,2)),0.5)
        gamp_2[k+1] = pow((pow(s2,2)+pow(s2_,2)),0.5)
        gamp_3[k+1] = pow((pow(s3,2)+pow(s3_,2)),0.5)
        gamp_4[k+1] = pow((pow(s4,2)+pow(s4_,2)),0.5)
        gamp_5[k+1] = pow((pow(s5,2)+pow(s5_,2)),0.5)
        gamp_6[k+1] = pow((pow(s6,2)+pow(s6_,2)),0.5)
        '''
        print(k/number_of_files*100)
        if float(timeEnd)==t[k]:
            break
        k+=1
             
        
        
    
    
    gamp_1 = np.log10(abs(gamp_1)/disk_mass)
    gamp_2 = np.log10(abs(gamp_2)/disk_mass)
    gamp_3 = np.log10(abs(gamp_3)/disk_mass)
    gamp_4 = np.log10(abs(gamp_4)/disk_mass)
    gamp_5 = np.log10(abs(gamp_5)/disk_mass)
    gamp_6 = np.log10(abs(gamp_6)/disk_mass)
    
    Param1=[gamp_1,gamp_2,gamp_3,gamp_4,gamp_5,gamp_6]
    Param2=['m=1','m=2','m=3','m=4','m=5','m=6']
    Parametry1=[]
    Parametry2=[]
    for i in range(len(mody)):
        if mody[i]==1:
            Parametry1.append(Param1[i])
            Parametry2.append(Param2[i])
    
    fig,ax = plt.subplots()
    for i in range(len(Parametry1)):
        ax.plot(t,Parametry1[i],label=Parametry2[i])
    '''
    ax.plot(t,gamp_1,label='m=1')
    ax.plot(t,gamp_2,label='m=2')
    ax.plot(t,gamp_3,label='m=3') 
    ax.plot(t,gamp_4,label='m=4') 
    ax.plot(t,gamp_5,label='m=5') 
    ax.plot(t,gamp_6,label='m=6')
    '''
    ax.set_xlim(0)
    #ax.set_ylim(-1,60)
    ax.legend(loc='lower right',prop=font_legend)
    plt.xlabel(r't',fontdict=font)
    plt.ylabel(r'$\hat A$',fontdict=font)
    ax.grid(True)
    plt.title('global amplitude a growing',fontdict=font)
    plt.tick_params(axis='both', which='major', labelsize=24)
    #plt.show()
    fig.set_size_inches(11, 8.7)
    #image = img.split('.')
    if not os.path.isdir(directory + '//FourierCoefficients_menu_6'):
        os.mkdir(directory + '//FourierCoefficients_menu_6')
    fig.savefig(directory + '//FourierCoefficients_menu_6//FourierCoefficients'+str(k)+format_image,dpi=int(dpi))
    #plt.close()
    plt.close('all')
    del rad, phi,z,t,gamp_1,gamp_2,gamp_3,gamp_4,gamp_5,gamp_6,s1,s2,s3,s4,s5,s6,DS,d

