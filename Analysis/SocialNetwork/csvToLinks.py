# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 15:21:13 2022

@author: Owner
"""

import pandas as pd

year = "2023"

### For any year
totalYears = [year] 

for i in set(totalYears): # for classified by years files
    filename = "SplitFiles_Year/SocialNetwork"+ i +".csv"
    df = pd.read_csv(filename)
    cols = df.columns
    df = df.rename(columns={'participantIdFrom': 'source', 'participantIdTo': 'target'})
    df['value'] = [1]*len(df)
    header = ['source', 'target', 'value']
    df.to_csv("SplitFiles_Year/links/SocialNetwork"+ i +"_links.csv", index=False, columns = header)

    
    
