# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 10:30:01 2020

@author: Jersey
"""

import pandas as pd

io1 = r'C:\HD\proj\code\filter_jinzhun.csv'
io2 = r'C:\HD\proj\data\OUTPUT_jinzhun_1.vcf'

vcf1 = pd.read_csv(io2,sep='\t',skiprows=29)
csv1 = pd.read_csv(io1)

def get_max(x):
    if x == '.':
        return '.'
    else :
        return max(x.split('|')[2:6])
a= vcf1.iloc[:,7].apply(get_max)
b= vcf1['INFO']

new_csv = pd.concat([csv1,b],axis=1)
new_csv1 = pd.concat([new_csv,a],axis=1)
