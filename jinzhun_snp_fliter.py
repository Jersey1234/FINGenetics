# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 11:02:30 2020

@author: Jersey
"""

import pandas as pd
io = r'C:\HD\proj\data\PKD-WES-55-SNV.xls'
file = pd.read_csv(io, sep='\t')

def f(x):
    if x == '.':
        return -1
    else :
        return float(x)

file['ExACAF'] = file['ExACAF'].apply(f)
file['gnomAD_exome_ALL_AF'] = file['gnomAD_exome_ALL_AF'].apply(f)
file['gnomAD_exome_EAS_AF'] = file['gnomAD_exome_EAS_AF'].apply(f)
file['ExACEASHomAC'] = file['ExACEASHomAC'].apply(f)

fitler1 = file.loc[(file['ExACAF'] <= 0.01) & (file['gnomAD_exome_ALL_AF'] <= 0.01) & (file['gnomAD_exome_EAS_AF'] <= 0.01) & (file['ExACEASHomAC'] <= 2)]
fitler2 = fitler1.loc[(fitler1['Refer'] != '.') & (fitler1['Call'] != '.')]
fitler2.to_csv('filter_jinzhun.csv',index=None)
