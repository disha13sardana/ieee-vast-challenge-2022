# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 11:54:26 2022

@author: Owner
"""

import pandas as pd

### input variable
# day = '03'
# year = '2023'
filePath = 'C:/Users/Owner/Documents/Disha/My Research/IEEE VAST Challenge 2022/dataset/VAST-Challenge-2022/Datasets'
# fileName = filePath+'/Journals/SocialNetwork.csv'

i = '1' #activity log file number
fileName = filePath+"/Activity Logs/ParticipantStatusLogs"+i+".csv"

df = pd.read_csv(fileName)
cols = df.columns

df['Year'] = df['timestamp'].apply(lambda x: x.split('-')[0])
df['Month'] = df['timestamp'].apply(lambda x: x.split('-')[1])

df['DayTime'] = df['timestamp'].apply(lambda x: x.split('-')[2])
df['Day'] = df['DayTime'].apply(lambda x: x.split('T')[0])
df['Time'] = df['DayTime'].apply(lambda x: x.split('T')[1])

