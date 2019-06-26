# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 16:11:55 2019

@author:Wei Huajing
@company:Nanjing University
@e-mail:jerryweihuajing@126.com

@title：Module-Depth of Fraction
"""

import copy as cp
import numpy as np
import matplotlib.pyplot as plt

import sys,os

if os.getcwd() not in sys.path:
    
    sys.path.append(os.getcwd())
    
from Module import Dictionary as Dict
from Module import TargetExtraction as TE

#============================================================================== 
#calculate top and bottom coordinate
def FractionDepth(which_fraction,side):
    
    I_fraction=[this_pos[0] for this_pos in which_fraction.edge]
    J_fraction=[this_pos[1] for this_pos in which_fraction.edge]
    
    #rectangle boundary
    J_min,J_max=np.min(J_fraction),np.max(J_fraction)
    I_min,I_max=np.min(I_fraction),np.max(I_fraction)
    
    #result
    top_depth=[]
    bottom_depth=[]
    
    for j in range(J_min,J_max+1):
        
        I_this_j=[]
        
        for i in range(I_min,I_max+1):
            
            if [i,j] in which_fraction.content:
                
                I_this_j.append(i)
                
        top_depth.append([np.min(I_this_j),j])
        bottom_depth.append([np.max(I_this_j),j])  
            
    if side=='top':
       
        return top_depth
   
    if side=='bottom':
        
        return bottom_depth