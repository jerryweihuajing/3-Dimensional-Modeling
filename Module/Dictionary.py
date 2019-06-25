# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 21:48:57 2019

@author:Wei Huajing
@company:Nanjing University
@e-mail:jerryweihuajing@126.com

@title：Module-Dictionary
"""

#============================================================================== 
#字典按value搜索key
def DictKeyOfValue(dictionary,value):
    
    keys=list(dictionary.keys())
    values=list(dictionary.values())
    
    #要查询的值为value
    key=keys[values.index(value)]
    
    return key

#============================================================================== 
#重新排序，以某个中间节点为起点，前部接在后部之后
def SortFromStart(which_list,start_index):

    #新老列表
    old_list=cp.deepcopy(which_list)
    new_list=which_list[start_index:]+which_list[:start_index]
    
    #新老列表的索引
    old_index=[k for k in range(len(old_list))]
    new_index=old_index[start_index:]+old_index[:start_index]
    
    #新老列表索引的对应关系
    map_new_old_index=dict(zip(old_index,new_index))
    
    return new_list,map_new_old_index 

#============================================================================== 
#让字典索引以某列表的顺序排列
def DictSortByIndex(which_dict,which_keys):
    
    #结果
    that_dict={}
    
    #遍历新列表，并填充字典
    for this_key in which_keys:
        
        that_dict[this_key]=which_dict[this_key]
        
    return that_dict