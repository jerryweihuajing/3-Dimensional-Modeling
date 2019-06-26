# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 13:45:47 2019

@author:Wei Huajing
@company:Nanjing University
@e-mail:jerryweihuajing@126.com

@title：MOdule-Display
"""

"""设计通过显示tag和part显示块体的函数"""

import numpy as np
import matplotlib.pyplot as plt

#============================================================================== 
#写一个同时能显示很多tag像素点的函数，混合tag，显示对象为fraction对象的集合
#显示多个fraction对象的函数
def ShowFractions(fractions,img_rgb,rgb_dict,output=False):
    
    #显示找到的内容
    background_rgb=np.array([255,255,255],dtype=np.uint8)
    img_temp=np.full(np.shape(img_rgb),background_rgb)
    
    #赋予目标对象的位置
    for this_fraction in fractions:
         
        #着色
        for pos in this_fraction.content:
            
            img_temp[pos[0],pos[1]]=rgb_dict[this_fraction.tag] 

    plt.imshow(img_temp)
        
    #是否输出矩阵
    if output:
        
        return img_temp
    
#============================================================================== 
#content is what is to presented
def ShowContent(which_content,img_tag):  
    
    #temp
    img_temp=np.full(np.shape(img_tag),1)
    
    for i,j in which_content:
    
        img_temp[i,j]=0
        
    plt.imshow(img_temp,cmap='gray')