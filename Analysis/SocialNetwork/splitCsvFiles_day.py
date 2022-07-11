# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 14:32:13 2022

@author: Owner
"""

import pandas as pd

### input variable
day = '03'
year = '2023'
fileName = 'SplitFiles_Day/'+year+'/SocialNetwork'+day+'.csv'

df = pd.read_csv(fileName)
cols = df.columns

# Source = [https://stackoverflow.com/questions/45001847/how-to-split-csv-file-into-respective-csv-files-based-on-date-in-first-column-p]

df['Year'] = df['timestamp'].apply(lambda x: x.split('-')[0])
df['Month'] = df['timestamp'].apply(lambda x: x.split('-')[1])

df['DayTime'] = df['timestamp'].apply(lambda x: x.split('-')[2])
df['Day'] = df['DayTime'].apply(lambda x: x.split('T')[0])



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
    filename = "SplitFiles_Day/"+year+"/SplitFiles"+day+"/SocialNetwork"+i+".csv"
    df.loc[df.Month == i].to_csv(filename,index=False,columns=cols)

