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
    
from Module import Dictionary as Dict
from Module import Initialize as Init

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

load_path=r'C:\魏华敬\Spyder\3D model\Data\1.bmp'

'''
demand:
target abstraction in seismic image
'''

#导入图片，生成rgb矩阵
img_rgb=Init.LoadImage(load_path,show=True)

#生rgb相关的列表和字典
#rgb_dict=Init.InitDict(img_rgb)
rgb_dict=Init.InitDict(img_rgb,base_adjust=True,fault_exist=True)

#改变图片尺寸增加padding
img_tag,img_rgb=Init.AddPadding(img_rgb,rgb_dict,show=True)

#初始化fractions，并显示
#total_fractions=Pick.PickFractions(img_rgb,img_tag,rgb_dict)  
