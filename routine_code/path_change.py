# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 14:21:46 2021

@author: DELL
"""

def path_change(path):
    if path[0]=='/':
        path=path[5].upper()+':'+path[6:]
        for i in range(len(path)):
            if path[i]=='/':
                path=path[:i]+'\\'+path[i+1:]
    else:
        path='/mnt/'+path[0].lower()+path[2:]
        for i in range(len(path)):
            if path[i]=='\\':
                path=path[:i]+'/'+path[i+1:]
    return path

#print(path_change(r"F:\日常文件\python_code\windows_grid_22_3_23.py"))