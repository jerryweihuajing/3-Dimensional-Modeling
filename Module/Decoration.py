# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 22:04:45 2019

@author:Wei Huajing
@company:Nanjing University
@e-mail:jerryweihuajing@126.com

@title：Module-Decoration
"""

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