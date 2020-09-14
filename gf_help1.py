# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 22:12:47 2020

@author: Jersey
"""
import time
import pandas as pd
from re import sub
start_time = time.time() 
io = r'C:\Users\Jersey\Documents\Tencent Files\876870298\FileRecv\pfam1.csv'
file = pd.read_csv(io)
def f(x):
    a = x.replace('.','')
    b = sub("[a-z]",'',a)
    return b
file.iloc[:,1]=file.iloc[:,1].apply(f)
file.to_csv('pfam1_result.csv',index=False)
print('running took %fs!' % (time.time() - start_time))
