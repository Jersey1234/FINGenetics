# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 16:19:59 2020

@author: Jersey
"""

import pandas as pd

io = r'C:\HD\proj\code\output2.vcf'
vcf1 = pd.read_csv(io,sep='\t',skiprows=29)
new = vcf1.iloc[:,7]

def get_max(x):
    if x == '.':
        return '.'
    else :
        return max(x.split('|')[2:6])
a= vcf1.iloc[:,7].apply(get_max)
a.rename('SpliceAI_max',inplace=True)
new_vcf1 = pd.concat([vcf1,a],axis=1)
new_vcf1.rename(columns={'INFO':'SpliceAI_raw'},inplace=True)
new_vcf1.to_csv('spliceAI_result.csv', index=False)