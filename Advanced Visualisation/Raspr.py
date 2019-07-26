# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import math
import numpy as np
import os
import sys
import fourcoeff
import draw_pcolor
import matplotlib.font_manager as font_manager

def MainGrapher(directory,Nmenu,dpi,format_image,colormap,vmin,vmax,Rd,radius,radius2,xlim,ylim,Param,mody,timeEnd):
    files = os.listdir(directory)
    #Получаем список файлов в переменную files
    #Фильтруем список 
    dat = filter(lambda x: x.endswith('.dat'), files)
    l = list(dat)
    dat = filter(lambda x: x.endswith('.dat'), files)
    number_of_files = len(l)
    #список радиусов в вещественный массив
    radius = list(map(lambda x: float(x),radius.split(',')))
    radius2 = list(map(lambda x: float(x),radius2.split(',')))
    Omega = 0.0
    Rd = Rd#30.0
    k = 0 #для меню №10
    N = len(radius) #для меню №10
    eps = sys.float_info.epsilon
    cmap=colormap#plt.cm.jet
    font = {'family': 'serif',
            #'color':  'black',
            'weight': 'normal',
            'size': 28,
            }
    font_legend = font_manager.FontProperties(family='serif',
                                              weight='normal', size=25)
    #size = 'float64';
    
    #---------------menu=6-------------Фурье-коэффициенты
    if Nmenu==6:
        fourcoeff.FourCoeff(directory,number_of_files,dat,font,font_legend,dpi,format_image,mody,timeEnd)
        
    #----------------------------------
    for img in dat:
        Input = open(directory + '//' + img,'rb')
        
        gam = np.fromfile(Input,np.float64,1)
        #print(Input.tell())
        t = np.fromfile(Input,np.float64,1)
        nrad = np.fromfile(Input,np.int32,1)
        nphi = np.fromfile(Input,np.int32,1)
        nz = np.fromfile(Input,np.int32,1)
        
        rad1 = np.fromfile(Input,np.float64,int(nrad))
        phi = np.fromfile(Input,np.float64,int(nphi))
        z1 = np.fromfile(Input,np.float64,int(nz))
        
        
        #параметры расчетной сетки не меняются во всех файлах
        if img == l[0]:
            rho = np.zeros((int(nrad),1))
            DS = np.zeros(nrad)
            x1 = np.zeros((int(nrad),int(nphi)))
            y1 = np.zeros((int(nrad),int(nphi)))
            #-----menu 10
            if Nmenu == 11:
                u1 = np.zeros((N,number_of_files))
                o1 = np.zeros((N,number_of_files))
                e1 = np.zeros((N,number_of_files))
                amp = np.zeros(number_of_files)
                nnn = np.zeros(N)
                            
            dr = rad1[2] - rad1[1]
            dphi = phi[2] - phi[1]
            for i in range(int(nrad)):
                DS[i] = math.pi*((rad1[i]+0.5*dr)**2 - ((rad1[i]-0.5*dr)**2))
                    
            for i in range(int(nrad)):
                for j in range(int(nphi)):
                    x1[i][j]=rad1[i]*np.cos(phi[j])
                    y1[i][j]=rad1[i]*np.sin(phi[j])
        
            for i in range(int(nrad)):
                x1[i][int(nphi)-1] = x1[i][0]
                y1[i][int(nphi)-1] = y1[i][0]
                
            
            if Nmenu==9:
                den0 = np.fromfile(Input,np.float64,(int(nrad)+4)*(int(nphi)+4)*int(nz)).reshape((int(nrad)+4,int(nphi)+4))
                den0 = den0[3:int(nrad+4)-1,3:int(nphi+4)-1]
                
        if Nmenu==0:
            rr = np.fromfile(Input,np.float64,(int(nrad)+4)*(int(nphi)+4)).reshape((int(nrad)+4,int(nphi)+4))
            pp = np.fromfile(Input,np.float64,(int(nrad)+4)*(int(nphi)+4)).reshape((int(nrad)+4,int(nphi)+4))
            ur = np.fromfile(Input,np.float64,(int(nrad)+4)*(int(nphi)+4)).reshape((int(nrad)+4,int(nphi)+4))
            uph = np.fromfile(Input,np.float64,(int(nrad)+4)*(int(nphi)+4)).reshape((int(nrad)+4,int(nphi)+4))
        elif Nmenu==9:
            rrr = np.fromfile(Input,np.float64,(int(nrad)+4)*(int(nphi)+4)*int(nz)).reshape((int(nrad)+4,int(nphi)+4))
            rrr = rrr[3:int(nrad+4)-1,3:int(nphi+4)-1]
        else:
            rrr = np.fromfile(Input,np.float64,(int(nrad)+4)*(int(nphi)+4)*int(nz)).reshape((int(nrad)+4,int(nphi)+4))
            rrr = rrr[3:int(nrad+4)-1,3:int(nphi+4)-1]
            ppp = np.fromfile(Input,np.float64,(int(nrad)+4)*(int(nphi)+4)*int(nz)).reshape((int(nrad)+4,int(nphi)+4))
            ppp = ppp[3:int(nrad+4)-1,3:int(nphi+4)-1]
            uuu = np.fromfile(Input,np.float64,(int(nrad)+4)*(int(nphi)+4)*int(nz)).reshape((int(nrad)+4,int(nphi)+4))
            uuu = uuu[3:int(nrad+4)-1,3:int(nphi+4)-1]
            vvv = np.fromfile(Input,np.float64,(int(nrad)+4)*(int(nphi)+4)*int(nz)).reshape((int(nrad)+4,int(nphi)+4))
            vvv = vvv[3:int(nrad+4)-1,3:int(nphi+4)-1]
            rf = np.fromfile(Input,np.float64,(int(nrad)+4)*(int(nphi)+4)*int(nz)).reshape((int(nrad)+4,int(nphi)+4))
            rf = rf[3:int(nrad+4)-1,3:int(nphi+4)-1]
            af = np.fromfile(Input,np.float64,(int(nrad)+4)*(int(nphi)+4)*int(nz)).reshape((int(nrad)+4,int(nphi)+4))
            af = af[3:int(nrad+4)-1,3:int(nphi+4)-1]
        Input.close()
                                
            #---------------menu=0-------------График распр начальных параметров
        if Nmenu==0:        
            V=uph[3:int(nrad+4)-1,int((nphi+4)/2)]
            vs=rr[3:int(nrad+4)-1,int((nphi+4)/2)]
            vp=pp[3:int(nrad+4)-1,int((nphi+4)/2)]
            r=rad1#.transpose()
            
            Vom = V + r*Omega
            vo = V/r # vo = V/r
            vc = (gam*vp)/vs
            v5 = np.gradient(vo,r[1]-r[0])
            v5[0] = 0.0
            vk = 4.0*pow(vo,2)+2.0*r*vo*v5
            vq = (np.sqrt(vc*vk)*(1/vs))/math.pi
            Lambda = (2*pow(math.pi,2)*vs)/vk
            #print('Q_{T} = ', min(vq[1:-2]))
            Param1=[Vom,V,vs,vo,pow(vk,0.5),vq]
            Param2=[r'$V_\phi$+r$\Omega$',r'$V_\phi$',r'$\sigma$',r'$\omega$',r'$\kappa$',r'$Q_T$']
            Parametry1=[]
            Parametry2=[]
            for i in range(len(Param)):
                if Param[i]==1:
                    Parametry1.append(Param1[i])
                    Parametry2.append(Param2[i])
            draw_pcolor.draw_grapher(r,Parametry1,Parametry2, #[Vom,V,vs,vo,vk**0.5,vq][r'$V_\phi$+r$\Omega$',r'$V_\phi$',r'$\sigma$',r'$\omega$',r'$\kappa$',r'$Q_T$']
                                 'r','',t,font,font_legend,img,directory,'ParamDataTVDPolar_menu_0',dpi,format_image,xlim,ylim)
            
            del rad1, phi,z1,rr,pp,ur,uph,r,V,vs,vp,Vom,vo,vc,v5,vk,vq,Lambda
            
            #---------------menu=1-------------плотность
        elif Nmenu==1:
            draw_pcolor.draw_pcolor(x1,y1,rrr,cmap,vmin,vmax,Rd,r'$\sigma$',t,font,img,directory,'Density_menu_1',dpi,format_image)
            del rad1, phi,z1,uuu,rrr,ppp,vvv,rf,af
                    #---------------menu=2-------------возмущение плотности
        elif Nmenu==2:
            rrr0 = np.zeros((int(nrad),int(nphi)))
            for i in range(int(nrad)):
                for j in range(int(nphi)):#rrr0 средняя плотность в кольце
                    rho[i] = rho[i]+rrr[i][j]*DS[i]/nphi
                    
                for j in range(int(nphi)):
                    rrr0[i][j] = rho[i]/DS[i]
                    
            Value = (rrr-rrr0)/rrr0
            Value[nrad-1,:] = Value[0,:]
            draw_pcolor.draw_pcolor(x1,y1,Value,cmap,vmin,vmax,Rd,r'($\sigma$ - <$\sigma$>)/<$\sigma$>',t,
                                    font,img,directory,'PertrubedDensity_menu_2',dpi,format_image)
            
            del rad1, phi,z1,uuu,rrr,ppp,vvv,rf,af,rrr0,Value
                
            #---------------menu=3-------------логарифм плотности
        elif Nmenu==3:
            Lrrr = np.log10(rrr+eps)
            draw_pcolor.draw_pcolor(x1,y1,Lrrr,cmap,vmin,vmax,Rd,r'lg($\sigma$)',t,font,img,directory,'LogDensity_menu_3',dpi,format_image)
            del rad1, phi,z1,uuu,rrr,ppp,vvv,rf,af,Lrrr
                
            #---------------menu=4-------------радиальная скорость
        elif Nmenu==4:
            draw_pcolor.draw_pcolor(x1,y1,uuu,cmap,vmin,vmax,Rd,r'radial velocity',t,font,img,directory,'RadialVelocity_menu_4',dpi,format_image)
            del rad1, phi,z1,uuu,rrr,ppp,vvv,rf,af
                
                #---------------menu=5-------------азимутальная скорость
        elif Nmenu==5:
            draw_pcolor.draw_pcolor(x1,y1,vvv,cmap,vmin,vmax,Rd,r'angular velocity',t,font,img,directory,'AngularVelocity_menu_5',dpi,format_image)
            del rad1, phi,z1,uuu,rrr,ppp,vvv,rf,af
                
                
            #---------------menu=7-------------радиальная сила
        elif Nmenu==7:
            draw_pcolor.draw_pcolor(x1,y1,rf,cmap,vmin,vmax,Rd,r'radial force',t,font,img,directory,'RadialForce_menu_7',dpi,format_image)
            del rad1, phi,z1,uuu,rrr,ppp,vvv,rf,af
                
                #---------------menu=8-------------азимутальная сила
        elif Nmenu==8:
            draw_pcolor.draw_pcolor(x1,y1,af,cmap,vmin,vmax,Rd,r'angular force',t,font,img,directory,'AngularForce_menu_8',dpi,format_image)
            del rad1, phi,z1,uuu,rrr,ppp,vvv,rf,af
                
                #---------------menu=9-------------возмущение плотности относительно ее начального распр
        elif Nmenu==9:
            Value = (rrr-den0)/den0#относительное возмущение плотности относительно ее начального распределения
            draw_pcolor.draw_pcolor(x1,y1,Value,cmap,vmin,vmax,Rd,r'($\sigma$ - $\sigma_0$)/$\sigma_0$',t,
                                    font,img,directory,'PertrubedDensity_menu_9',dpi,format_image)
                
            del rad1, phi,z1,rrr,Value
                
                #---------------menu=10-------------графики зависимости логарифма плотности от угла
        elif Nmenu==10:
            Lrrr = np.log10(rrr+eps)
            nnn = np.zeros(len(radius2))
            for i in range(len(radius2)):
                nnn[i] = radius2[i]
                nnn[i] = nnn[i]/dr
            
            nnn = np.fix(nnn+0.5)
            
            fig,ax = plt.subplots()
            for i in range(5):
                a = nnn[i]
                maxrrr = np.max(Lrrr[int(a),:])
                r = nnn[i]*dr+0.5
                ax.plot(phi,Lrrr[int(a),:],label='r=%d'% r)
                
            ax.axis([0, 6.2, -3.0, -0.5])
            plt.title(r'log($\sigma$)($\phi$), t=%1.1f'% t, fontdict=font)
            ax.legend(loc='upper right',prop=font_legend)
            plt.tick_params(axis='both', which='major', labelsize=20)
            plt.xlabel(r'$\phi$',fontdict=font)
            plt.ylabel(r'log($\sigma$)',fontdict=font)
                        
            fig.set_size_inches(9.5, 8.7)
            image = img.split('.')
            if not os.path.isdir(directory + '//LSigma_menu_10'):
                os.mkdir(directory + '//LSigma_menu_10')
            fig.savefig(directory + '//LSigma_menu_10//LSigma'+image[0]+format_image,dpi=int(dpi))
            #plt.close()
            plt.close('all')
            del rad1, phi,z1,uuu,rrr,ppp,vvv,rf,af,Lrrr,nnn
                
                #---------------menu=11-------------график зависимости возмущения плотности от времени на радиусах
        elif Nmenu==11:
            amp[k] = t
            dr = rad1[2] - rad1[1]
            dN = nrad/N
            dNN = 0
            
            nnn = np.zeros(N)
            for i in range(N):
                nnn[i] = radius[i]
                nnn[i] = nnn[i]/dr
            #nnn = np.array([6/dr,12/dr,18/dr,24/dr,30/dr])
            nnn = np.fix(nnn+0.5)
            #nnn=1
            
                
            for i in range(N):
                local_max = -1
                i_local_max = nnn[i]
                for j in range(int(nphi)):
                    if local_max < rrr[int(i_local_max),j]:
                        local_max = rrr[int(i_local_max),j]
                        #j_local_max = j
                        
                u1[i][k] = local_max
                o1[i][k] = np.sum(rrr[int(nnn[i])])/nphi
                e1[i][k] = (u1[i][k]-o1[i][k])/o1[i][k]
            #nnn = nnn*dr
            if float(timeEnd)==amp[k]:
                break
            k+=1
            
               
            
    if Nmenu==11:
        fig,ax = plt.subplots()
        #print(amp)
        nnn = nnn*dr
        #print(e1[0])
        for i in range(N):
            ax.plot(amp,np.log10(e1[i]),label='r=%d'%nnn[i])
            
        ax.set_xlim(0)
        ax.legend(loc='lower right',prop=font_legend)
        plt.xlabel('t',fontdict=font)
        plt.ylabel(r'($\sigma_{max}$ - <$\sigma$>)/<$\sigma$>  ',fontdict=font)
        plt.tick_params(axis='both', which='major', labelsize=20)
        
        #plt.show()
        fig.set_size_inches(9.5, 8.7)
        image = img.split('.')
        if not os.path.isdir(directory + '//LDen2_menu_11'):
                os.mkdir(directory + '//LDen2_menu_11')
        fig.savefig(directory + '//LDen2_menu_11//LDen2'+image[0]+format_image,dpi=int(dpi))
        plt.close('all')
        #plt.close(fig)
        del rad1, phi,z1,uuu,rrr,ppp,vvv,rf,af,nnn
        
    if Nmenu==9:
        del den0
    
    elif Nmenu==0 or Nmenu==1 or Nmenu==2 or Nmenu==3 or Nmenu==4 or Nmenu==5 or Nmenu==7 or Nmenu==8 or Nmenu==9 or Nmenu==10 or Nmenu==11:
        del rho, DS,x1,y1,l
       
    if Nmenu==11:
        del u1,e1,o1,amp
