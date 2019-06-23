# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 15:31:00 2019

@author:Wei Huajing
@company:Nanjing University
@e-mail:jerryweihuajing@126.com

@title：三维建模
"""

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np

# %matplotlib inline

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['SimHei']

def plot_opaque_cube(ax,x, y, z, dx, dy, dz,which_color):
    
    xx = np.linspace(x, x+dx, 2)
    yy = np.linspace(y, y+dy, 2)
    zz = np.linspace(z, z+dz, 2)

    #wall:1,2
    xx, yy = np.meshgrid(xx, yy)
    
    ax.plot_surface(xx, yy, np.full(np.shape(xx),z),color=which_color)
    ax.plot_surface(xx, yy, np.full(np.shape(xx),z+dz),color=which_color)

    #wall:3,4
    yy, zz = np.meshgrid(yy, zz)
    ax.plot_surface(np.full(np.shape(yy),x), yy, zz,color=which_color)
    ax.plot_surface(np.full(np.shape(yy),x+dx), yy, zz,color=which_color)

    #wall：3,4
    xx, zz = np.meshgrid(xx, zz)
    ax.plot_surface(xx, np.full(np.shape(zz),y), zz,color=which_color)
    ax.plot_surface(xx, np.full(np.shape(zz),y+dy), zz,color=which_color)

    #坐标范围
    ax.set_xlim3d(0,100,20)
    ax.set_ylim3d(0,100,20)
    ax.set_zlim3d(0,100,20)
    
    #标题
    plt.title("Cube")
    plt.show()

def plot_linear_cube(x, y, z, dx, dy, dz, color='red'):
    
    fig = plt.figure()
    ax = Axes3D(fig)
    xx = [x, x, x+dx, x+dx, x]
    yy = [y, y+dy, y+dy, y, y]
    kwargs = {'alpha': 1, 'color': color}
    
    ax.plot3D(xx, yy, [z]*5, **kwargs)
    ax.plot3D(xx, yy, [z+dz]*5, **kwargs)
    ax.plot3D([x, x], [y, y], [z, z+dz], **kwargs)
    ax.plot3D([x, x], [y+dy, y+dy], [z, z+dz], **kwargs)
    ax.plot3D([x+dx, x+dx], [y+dy, y+dy], [z, z+dz], **kwargs)
    ax.plot3D([x+dx, x+dx], [y, y], [z, z+dz], **kwargs)
    
    plt.title('Cube')
    plt.show()

#plot_linear_cube(0, 0, 0, 100, 120, 130)
#   
#fig = plt.figure()
#ax = fig.add_subplot(1, 1, 1, projection='3d')
#
#plot_opaque_cube(ax,0, 0, 0, 100, 100, 30,'green')
#plot_opaque_cube(ax,50,0, 30, 50, 100, 30,'blue')
#plot_opaque_cube(ax,0, 0, 60, 100, 100, 30,'red')
#
##清除坐标轴
#ax.set_xticks([])
#ax.set_yticks([])
#ax.set_zticks([])
#
#plot_opaque_cube(ax,0, 0, 30, 50, 100, 30,'white')

#尖灭楔形体
def plot_opaque_wedge():
    return


x=[k for k in range(10)]

y=[-k+1 for k in range(10)]

xx,yy=np.meshgrid(x,y)

zz=np.full(np.shape(xx),1)


ax = fig.add_subplot(1, 1, 1, projection='3d')