# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 15:21:13 2022

@author: Owner
"""

import pandas as pd

year = "2022-2023"

### For any year
totalDays = ['01','02','03','04','05', 
             '06','07','08','09','10',
             '11','12','13','14','15', 
             '16','17','18','19','10',
             '21','22','23','24','25', 
             '26','27','28','29','30','31'] 

for i in set(totalDays): # for classified by months files
    filename = "SplitFiles_Day/"+ year +"/SocialNetwork"+ i +".csv"
    df = pd.read_csv(filename)
    cols = df.columns
    df = df.rename(columns={'participantIdFrom': 'source', 'participantIdTo': 'target'})
    df['value'] = [1]*len(df)
    header = ['source', 'target', 'value']
    df.to_csv("SplitFiles_Day/"+ year +"/links/SocialNetwork"+ i +"_links.csv", index=False, columns = header)

    
    
