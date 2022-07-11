# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 13:04:04 2022

@author: Owner
"""

import csv
import json

### input variable
year = "2023"
day = '01'
j = 0 ## 0 for nodes, 1 for links
variableOfInterest = 'currentMode'

jsonType = ['nodes', 'links'] ## either links or nodes
folderName = [r'Nodes/'+variableOfInterest+'/', r'SplitFiles_Day/']
internalFolderName = ['/day', '/SplitFiles']

# csvFilePath = r'SplitFiles_Month/'+ year +'/'+jsonType[j]
# jsonFilePath = r'SplitFiles_Month/'+ year +'/json_'+jsonType[j]

csvFilePath = folderName[j] + year + internalFolderName[j] + day +'/'+jsonType[j]
jsonFilePath = folderName[j] + year + internalFolderName[j] + day +'/json_'+jsonType[j]

# [Source: https://pythonexamples.org/python-csv-to-json/]
def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
 

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
    csvFileName  = csvFilePath +'/SocialNetwork'+ i +'_'+jsonType[j]+'.csv'
    jsonFileName = jsonFilePath +'/SocialNetwork'+ i +'_'+jsonType[j]+'.json'       
    csv_to_json(csvFileName, jsonFileName)
