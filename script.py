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
from Module import TargetExtraction as TE

load_path=r'C:\魏华敬\Spyder\3D model\Data\1.bmp'

images_paths=[r'C:\魏华敬\Spyder\3D model\Data\1.bmp',
              r'C:\魏华敬\Spyder\3D model\Data\2.bmp',
              r'C:\魏华敬\Spyder\3D model\Data\3.bmp']

'''
demand:
target abstraction in seismic image
'''

def FractionSurface(load_path):
        
    #导入图片，生成rgb矩阵
    img_rgb=Init.LoadImage(load_path,show=True)
    
    #生rgb相关的列表和字典
    #rgb_dict=Init.InitDict(img_rgb)
    rgb_dict=Init.InitDict(img_rgb,base_adjust=True,fault_exist=True)
    
    #生成tag矩阵
    img_tag=Im.RGB2Tag(img_rgb,rgb_dict)
    
    #初始化fractions，并显示
    total_fractions=Init.InitFractions(img_rgb,img_tag,rgb_dict)
     
    total_layers=Init.InitLayers(total_fractions)
    total_faults=Init.InitFaults(total_fractions)
    
    return Dep.FractionDepth(total_layers[0],'top')

#    plt.figure()
#    Dis.ShowContent(top_depth,img_tag) 

discrete_points=[]

pos_x=0

'''Display ERROR'''
for this_load_path in images_paths[:1]:
    
    #different profile
    pos_x+=10
    
    #surface of this fraction
    pos_surface=FractionSurface(this_load_path)
    
    for pos_z,pos_y in pos_surface:
        
        print(pos_z,pos_y)
        
        #new discrete_point object
        new_discrete_point=discrete_point()
        
        new_discrete_point.pos_x=pos_x
        new_discrete_point.pos_y=pos_y
        new_discrete_point.pos_z=pos_z
        
        discrete_points.append(new_discrete_point)
        
        
#interpolation
    
    