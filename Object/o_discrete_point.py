# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 19:55:26 2019

@author:Wei Huajing
@company:Nanjing University
@e-mail:jerryweihuajing@126.com

@title：Object-discrete_point

for xyz format
"""

#==============================================================================
#pos: 3D coordiante
#==============================================================================  
class discrete_point:
    def __init__(self,
                 pos_x=None,
                 pos_y=None,
                 pos_z=None):
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.pos_z=pos_z