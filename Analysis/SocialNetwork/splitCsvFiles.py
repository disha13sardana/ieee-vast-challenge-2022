# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 14:32:13 2022

@author: Owner
"""

import pandas as pd

### input variable
fileName = 'SplitFiles_Year/SocialNetwork2023.csv'


df = pd.read_csv(fileName)
cols = df.columns

# Source = [https://stackoverflow.com/questions/45001847/how-to-split-csv-file-into-respective-csv-files-based-on-date-in-first-column-p]

df['Year'] = df['timestamp'].apply(lambda x: x.split('-')[0])
df['Month'] = df['timestamp'].apply(lambda x: x.split('-')[1])

df['DayTime'] = df['timestamp'].apply(lambda x: x.split('-')[2])
df['Day'] = df['DayTime'].apply(lambda x: x.split('T')[0])

# for i in set(df.Year): # for classified by years files
#     filename = "path/"+i+".csv"
#     df.loc[df.Year == i].to_csv(filename,index=False,columns=cols)


# for i in set(df.Month): # for classified by months files
#     filename = "SplitFiles_Month/2022/SocialNetwork"+i+".csv"
#     df.loc[df.Month == i].to_csv(filename,index=False,columns=cols)

for i in set(df.Day): # for classified by months files
    filename = "SplitFiles_Day/2023/SocialNetwork"+i+".csv"
    df.loc[df.Day == i].to_csv(filename,index=False,columns=cols)