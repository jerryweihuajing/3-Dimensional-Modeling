# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 21:54:03 2019

@author:Wei Huajing
@company:Nanjing University
@e-mail:jerryweihuajing@126.com

@title：Module-Image
"""

import numpy as np
import matplotlib.pyplot as plt

import sys,os

if os.getcwd() not in sys.path:
    
    sys.path.append(os.getcwd())

from Module import Dictionary as Dict

#============================================================================== 
def RGB2Gray(which_img_rgb):
    
    #r,g,b 3 tunnel
    R=which_img_rgb[:,:,0]
    G=which_img_rgb[:,:,1]
    B=which_img_rgb[:,:,2]
    
    return 0.3*R+0.59*G+0.11*B

#==============================================================================    
#由img_rgb生成img_tag
def RGB2Tag(img_rgb,rgb_dict,show=False,axis=False):
    
    img_tag=np.zeros((np.shape(img_rgb)[0],np.shape(img_rgb)[1]))
    
    #给img_tag矩阵赋值
    for i in range(np.shape(img_tag)[0]):
        
        for j in range(np.shape(img_tag)[1]):
            
            img_tag[i,j]=Dict.DictKeyOfValue(rgb_dict,list(img_rgb[i,j].astype(int)))
    
    #显示
    if show:
        
        plt.figure()
        plt.imshow(img_tag,cmap='gray')
        
        #显示坐标轴吗
        if axis:
            
            plt.axis('off')
            
    return img_tag

#==============================================================================    
#由img_tag生成img_rgb
def Tag2RGB(img_tag,rgb_dict,show=False,axis=False):
    
    #初始化这个rgb矩阵
    img_rgb=np.zeros((np.shape(img_tag)[0],np.shape(img_tag)[1],3))

    #给img_rgb矩阵赋值
    for i in range(np.shape(img_rgb)[0]):
        
        for j in range(np.shape(img_rgb)[1]):
            
#            print(img_tag[i,j])
#            print(rgb_dict[int(img_tag[i,j])])

            #注意dtype，必须是uint8才能正常显示RGB
            img_rgb[i,j]=np.array(rgb_dict[img_tag[i,j]])
    
    #转化为正确输出格式      
    img_rgb=np.array(img_rgb,dtype=np.uint8)  
      
    #显示
    if show:
        
        plt.figure()
        plt.imshow(img_rgb)
        
        #显示坐标轴吗
        if axis:
            
            plt.axis('off')
            
    return img_rgb