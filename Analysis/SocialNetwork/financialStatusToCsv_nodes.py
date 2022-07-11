# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 13:12:53 2022

@author: Owner
"""

import pandas as pd

### input variable
year = "2023"
day = '03'
time = 'T00:00:00Z'
variableOfInterest = 'finanicalStatus'

### For year 2022
if year=="2022":
    totalMonths = ['03','04','05','06','07','08','09','10','11','12']
    rangeMin_Months = 3
    rangeMax_Months = 12
    rangeMin_activityLogFile = 1
    rangeMax_activityLogFile = 50
    
### For year 2023
if year=="2023":
    totalMonths = ['01','02','03','04','05']
    rangeMin_Months = 1
    rangeMax_Months = 5
    rangeMin_activityLogFile = 49
    rangeMax_activityLogFile = 73
    

filePath = "C:/Users/Owner/Documents/Disha/My Research/IEEE VAST Challenge 2022/dataset/VAST-Challenge-2022/Datasets"

i = rangeMin_activityLogFile
j = rangeMin_Months

while j< rangeMax_Months+1:
    ## Read data file
    fileName = filePath+"/Activity Logs/ParticipantStatusLogs"+str(i)+".csv"
    df = pd.read_csv(fileName)
    
    ## Formatting months
    if j<10:
        strJ = '0'+str(j)
    else:
        strJ = str(j)
        
    ## Get the required data for the specific timestamp  
    financialStatus = df.loc[df['timestamp'] == year + '-' + strJ + '-'+ day + time].financialStatus
    participantId = df.loc[df['timestamp'] == year + '-' + strJ + '-' + day + time].participantId                                                 
    
    ## Creating a new dataframe with participants id and financial status
    df2 = pd.DataFrame(participantId)
    
    if df2.shape[0] != 0:
        df2['group'] = financialStatus
        df2['group'] = df2['group'].replace(['Stable','Unstable','Unknown'],['1','2','3'])
        df2 = df2.rename(columns={'participantId': 'id'})
        
        ## Converting the dataframe to csv file
        # header = ['id', 'group']
        # df2.to_csv("SplitFiles_Month/"+year+"/nodes/SocialNetwork"+ strJ +"_nodes.csv", index=False)
        # df2.to_csv("SplitFiles_Month/"+year+'/day'+day+"/nodes/SocialNetwork"+ strJ +"_nodes.csv", index=False)
        df2.to_csv('Nodes/'+ variableOfInterest + '/' + year +'/day' + day + "/nodes/SocialNetwork"+ strJ +"_nodes.csv", index=False)
        j = j+1
    else:
        i = i+1
        print ('Activity Log file:', i)
        print ('Month:', j)
