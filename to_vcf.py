# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 10:11:55 2020

@author: Jersey
"""

import pandas as pd
from pandas import DataFrame

io = r'C:\HD\proj\code\filter.csv'
fliter1 = pd.read_csv(io)
vcf = fliter1.loc[:,["CHROM","POS","ID","REF","ALT"]]
vcf = vcf.reindex(columns=["CHROM","POS","ID","REF","ALT","QUAL","FILTER","INFO"],fill_value='.')
new = pd.DataFrame({'CHROM':['##fileformat=VCFv4.2',\
                             '##fileDate=20191004',\
                             '##reference=GRCh37/hg19',\
                             '##contig=<ID=1,length=249250621>',\
                             '##contig=<ID=2,length=243199373>',\
                             '##contig=<ID=3,length=198022430>',\
                             '##contig=<ID=4,length=191154276>',\
                             '##contig=<ID=5,length=180915260>',\
                             '##contig=<ID=6,length=171115067>',\
                             '##contig=<ID=7,length=159138663>',\
                             '##contig=<ID=8,length=146364022>',\
                             '##contig=<ID=9,length=141213431>',\
                             '##contig=<ID=10,length=135534747>',\
                             '##contig=<ID=11,length=135006516>',\
                             '##contig=<ID=12,length=133851895>',\
                             '##contig=<ID=13,length=115169878>',\
                             '##contig=<ID=14,length=107349540>',\
                             '##contig=<ID=15,length=102531392>',\
                             '##contig=<ID=16,length=90354753>',\
                             '##contig=<ID=17,length=81195210>',\
                             '##contig=<ID=18,length=78077248>',\
                             '##contig=<ID=19,length=59128983>',\
                             '##contig=<ID=20,length=63025520>',\
                             '##contig=<ID=21,length=48129895>',\
                             '##contig=<ID=22,length=51304566>',\
                             '##contig=<ID=X,length=155270560>',\
                             '##contig=<ID=Y,length=59373566>',\
                             ]})
new1 = DataFrame({'CHROM':'#CHROM','POS':'POS','ID':'ID','REF':'REF','ALT':'ALT','QUAL':'QUAL','FILTER':'FILTER','INFO':'INFO'},index=[0])
new2 = pd.concat([new1,vcf])
new3 = pd.concat([new,new2])
new3.to_csv('input_1M.vcf', sep='\t', index=False, header=False)
