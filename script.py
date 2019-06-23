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

#============================================================================== 
#坐标轴和边框
def TicksAndSpines(ax,ticks=False,spines=False):
    
    #去掉坐标轴
    if not ticks:

        ax.set_xticks([])
        ax.set_yticks([])
        
     #去掉上下左右边框
    if not spines:

        ax.spines['top'].set_visible(False) 
        ax.spines['bottom'].set_visible(False) 
        ax.spines['left'].set_visible(False) 
        ax.spines['right'].set_visible(False)

#============================================================================== 
def RGB2Gray(which_img_rgb):
    
    #r,g,b 3 tunnel
    R=which_img_rgb[:,:,0]
    G=which_img_rgb[:,:,1]
    B=which_img_rgb[:,:,2]
    
    return 0.3*R+0.59*G+0.11*B

load_path=r'C:\魏华敬\Spyder\3D model\Data\profile_model_1.bmp'

img_rgb=plt.imread(load_path)

plt.imshow(img_rgb)

'''
demand:
target abstraction in seismic image
'''