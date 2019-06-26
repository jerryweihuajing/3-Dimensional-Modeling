# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 23:44:28 2019

@author:Wei Huajing
@company:Nanjing University
@e-mail:jerryweihuajing@126.com

@title：Discrete points to mesh points
"""

import numpy as np
import matplotlib.pyplot as plt

import sys,os
sys.path.append(os.getcwd())

from Object import o_grid
from Object import o_mesh
from Object import o_discrete_point

#==============================================================================  
#构造网格点矩阵
def MeshGrid(which_discrete_points,step,show=False):
    
    #x,y方向上的步长
    step_x=step_y=step
    
    #首先找出网格的坐标范围
    x_discrete_points=[this_point.pos_x for this_point in which_discrete_points]
    y_discrete_points=[this_point.pos_y for this_point in which_discrete_points]
    
    #xy边界
    boundary_x=[min(x_discrete_points),max(x_discrete_points)]
    boundary_y=[min(y_discrete_points),max(y_discrete_points)]
    
    #xy边长
    length_x=boundary_x[1]-boundary_x[0]
    length_y=boundary_y[1]-boundary_y[0]
         
    #xy方向上的网格数
    amount_grid_x=int(np.ceil(length_x/step_x))
    amount_grid_y=int(np.ceil(length_y/step_y))
    
    #xy方向上的网格交点数
    amount_mesh_points_x=amount_grid_x+1
    amount_mesh_points_y=amount_grid_y+1
    
    #显示吗哥
    if show:
        
        #x向
        for k_x in range(amount_mesh_points_x):
            
            plt.vlines(boundary_x[0]+k_x*step_x,
                       boundary_y[0],
                       boundary_y[0]+amount_grid_y*step_y,
                       color='k',
                       linestyles="--")
            
        #y向
        for k_y in range(amount_mesh_points_y):
            
            plt.hlines(boundary_y[0]+k_y*step_y,
                       boundary_x[0],
                       boundary_x[0]+amount_grid_x*step_x,
                       color='k',
                       linestyles="--")
     
#    print('length_x:',amount_x)
#    print('length_y:',amount_y)
          
    #生成网格交点的坐标矩阵
    mesh_points=[]
    
    for k_x in range(amount_grid_x):
        
        for k_y in range(amount_grid_y):
            
            mesh_points.append([boundary_x[0]+k_x*step_x,boundary_y[0]+k_y*step_y])
            
#    print(len(mesh_points),amount_x*amount_y)
    
    return np.array(mesh_points).reshape((amount_grid_x,amount_grid_y,2)) 