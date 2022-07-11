# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 13:04:04 2022

@author: Owner
"""
import pandas as pd
import csv
import json

csvFilePath = r'SocialNetwork1_links.csv'
jsonFilePath = r'SocialNetwork1_links.json'

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
          
csv_to_json(csvFilePath, jsonFilePath)
