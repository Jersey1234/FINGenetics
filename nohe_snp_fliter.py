# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 16:00:25 2020

@author: Jersey
"""

import pandas as pd
print ("@##################################################@")
print ("@脚本名称：snp基因频率&功能筛选器（诺禾版）           @")
print ("@脚本作者：Jersey                                   @")
print ("@脚本功能：对基因频率以及对区域功能进行筛选           @")
print ("@##################################################@")
print ()
io = input("请输入你的文件位置：")
io = io.replace('\\','/')
print("读取文件中。。请耐心等待。")
unenforceable = pd.read_csv(io,sep='\t')
print("读取完毕，开始筛选。")
def f(x):
    if x == '.':
        return -1
    else :
        return float(x)
    
unenforceable['1000g_EAS'] = unenforceable['1000g_EAS'].apply(f)
unenforceable['1000g_ALL'] = unenforceable['1000g_ALL'].apply(f)
unenforceable['GnomAD_ALL_AF'] = unenforceable['GnomAD_ALL_AF'].apply(f)
unenforceable['GnomAD_EAS_AF'] = unenforceable['GnomAD_EAS_AF'].apply(f)

filter1 = unenforceable.loc[(unenforceable['1000g_ALL'] <= 0.01) & (unenforceable['1000g_EAS'] <= 0.01) & (unenforceable['GnomAD_ALL_AF'] <= 0.01) & (unenforceable['GnomAD_EAS_AF'] <= 0.01)]
filter2 = filter1.loc[(filter1['ExonicFunc'] != "synonymous SNV")]
filter3= filter2.loc[(filter2['Func'] == "exonic") | (filter2['Func'] == "exonic;splicing")  | (filter2['Func'] == "splicing")]
print("筛选完毕，结果文件存放至当前文件目录下")
filter3.to_csv('filter_onlyf.csv',index=None)