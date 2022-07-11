# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 13:04:04 2022

@author: Owner
"""

import csv
import json


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
 

year = "2022-2023"

### For any year
totalDays = ['01','02','03','04','05', 
             '06','07','08','09','10',
             '11','12','13','14','15', 
             '16','17','18','19','10',
             '21','22','23','24','25', 
             '26','27','28','29','30','31'] 

for i in set(totalDays): # for classified by months files
    csvFilePath  = r'SplitFiles_Day/'+ year +'/links/SocialNetwork'+ i +'_links.csv'
    jsonFilePath = r'SplitFiles_Day/'+ year +'/json_links/SocialNetwork'+ i +'_links.json'       
    csv_to_json(csvFilePath, jsonFilePath)
