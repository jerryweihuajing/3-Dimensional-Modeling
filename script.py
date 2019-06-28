# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 22:20:34 2019

@author:Wei Huajing
@company:Nanjing University
@e-mail:jerryweihuajing@126.com

@title：seismic profile model construction-execution script
"""

import matplotlib.pyplot as plt
import numpy as np
import copy as cp

import sys,os

if os.getcwd() not in sys.path:
    
    sys.path.append(os.getcwd())  

from Object.o_discrete_point import discrete_point

from Module import Image as Im
from Module import Depth as Dep
from Module import Display as Dis
from Module import Dictionary as Dict
from Module import Initialize as Init
from Module import Interpolation as Int
from Module import TargetExtraction as TE

load_path='./Data/1.bmp'

images_paths=['./Data/flat_1.bmp',
              './Data/flat_2.bmp',
              './Data/flat_3.bmp']

'''
demand:
target abstraction in seismic image
'''

def FractionSurface(load_path,k):
        
    #导入图片，生成rgb矩阵
    img_rgb=Init.LoadImage(load_path)
    
    #生rgb相关的列表和字典
    #rgb_dict=Init.InitDict(img_rgb)
    rgb_dict=Init.InitDict(img_rgb,base_adjust=True)
    
#    print(rgb_dict)
    
    #生成tag矩阵
    img_tag=Im.RGB2Tag(img_rgb,rgb_dict)
    
    #初始化fractions，并显示
    total_fractions=Init.InitFractions(img_rgb,img_tag,rgb_dict)
     
    total_layers=Init.InitLayers(total_fractions)
    total_faults=Init.InitFaults(total_fractions)
    
#    #all surfaces in this image
#    surfaces=[]
#    
#    for this_layer in total_layers:
#        
#        surfaces.append(Dep.FractionDepth(this_layer,'top'))
#
#    return surfaces

    return Dep.FractionDepth(total_fractions[k],'top')+Dep.FractionDepth(total_fractions[k],'bottom')

#list of discrete points
images=[]

for k in range(2):
    
    discrete_points=[]
    
    pos_x=0
    
    '''Display ERROR'''
    for this_load_path in images_paths:
    
        #different profile
        pos_x+=5
        
        #surface of this fraction
        pos_surface=FractionSurface(this_load_path,k)
        
    #    print(len(pos_surface))
        
        for pos_z,pos_y in pos_surface:
                 
            #new discrete_point object
            new_discrete_point=discrete_point()
            
            new_discrete_point.pos_x=pos_x
            new_discrete_point.pos_y=pos_y
            new_discrete_point.pos_z=pos_z
            
            discrete_points.append(new_discrete_point)    
        
        pixel_step=1
        
    #interpolation
    this_img=Int.GlobalIDWInterpolation(discrete_points,pixel_step)   
    
    plt.figure()
    
    plt.imshow(this_img,cmap='terrain')
    
    #collect all the image
    images.append(this_img)
    
fig = plt.figure()   
ax = fig.add_subplot(111, projection='3d')

colors=['red','blue']
count=0

for this_img in images:
    
    #3D coordinates
    X,Y,Z=[],[],[]
    
    for i in range(np.shape(this_img)[0]):
        
        for j in range(np.shape(this_img)[1]):
            
            X.append(j)
            Y.append(i)
            Z.append(this_img[i,j])
    
    ax.plot_trisurf(X, Y, Z,color=colors[count])
    plt.show()
    
    count+=1
    
ax.spines['top'].set_visible(False) 
ax.spines['bottom'].set_visible(False) 
ax.spines['left'].set_visible(False) 
ax.spines['right'].set_visible(False)
        
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

#plt.axis('equal')

plt.zlim(min(Z),max(Z))