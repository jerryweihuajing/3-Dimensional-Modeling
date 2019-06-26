# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 13:20:47 2019

@author:Wei Huajing
@company:Nanjing University
@e-mail:jerryweihuajing@126.com

@title：Object-pixel
"""

import numpy as np

#==============================================================================  
#pixel class
#neighbor: 8 points nearby
#==============================================================================  
class pixel:
    def __int__(self,
                xpos=None,
                ypos=None,
                value=None,
                neighbor_index=None,
                neighbor_value=None):
        self.xpos=xpos
        self.ypos=ypos
        self.value=value
        self.neighbor_index=neighbor_index
        self.neighbor_value=neighbor_value
    
    #generate his neighbor
    def InitNeighbor(self,img_tag):      
       
        #true neighbor
        self.neighbor_index=[]
        self.neighbor_value=[]

        #逆时针遍历邻域内的点
        neighbordict={0:(0,-1),
                      1:(1,-1),
                      2:(1,0),
                      3:(1,1),
                      4:(0,1),
                      5:(-1,1),
                      6:(-1,0),
                      7:(-1,-1)}
        
        #[i,j-1],[i+1,j-1],[i+1,j],[i+1,j+1],[i,j+1],[i-1,j+1],[i-1,j],[i-1,j-1]
        for item in list(neighbordict.values()):

            #遍历新的坐标
            new_y=self.ypos+item[0]
            new_x=self.xpos+item[1]
            
            if 0<=new_y<np.shape(img_tag)[0] and 0<=new_x<np.shape(img_tag)[1]:
                
                self.neighbor_index.append([new_y,new_x])
                self.neighbor_value.append(img_tag[new_y,new_x])     
                
            else:
                
                self.neighbor_index.append(None)
                self.neighbor_value.append(None)
                             