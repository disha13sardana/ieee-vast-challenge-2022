# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 15:21:13 2022

@author: Owner
"""

import pandas as pd

### input variable
year = "2023"
day = '03'
j = 1

jsonType = ['nodes', 'links'] ## either links or nodes

# filePath = "SplitFiles_Month/"+ year

filePath = "SplitFiles_Day/"+ year +'/SplitFiles'+day

### For year 2022
if year=="2022":
    totalMonths = ['03','04','05','06','07','08','09','10','11','12']

### For year 2023
if year=="2023":
    totalMonths = ['01','02','03','04','05']

### For year 2022-2023
if year=="2022-2023":
    totalMonths = ['01','02','03','04','05','06','07','08','09','10','11','12']


for i in set(totalMonths): # for classified by months files
    fileName = filePath +"/SocialNetwork"+ i +".csv"
    df = pd.read_csv(fileName)
    df = df.rename(columns={'participantIdFrom': 'source', 'participantIdTo': 'target'})
    df['value'] = [1]*len(df)
    header = ['source', 'target', 'value']
    df.to_csv(filePath +"/links/SocialNetwork"+ i +"_links.csv", index=False, columns = header)

    
    
