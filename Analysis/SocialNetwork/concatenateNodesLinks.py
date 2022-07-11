# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 15:56:41 2022

@author: Owner
"""

import json

### input variable
year = "2023"
day = '01'
variableOfInterest = 'currentMode'

jsonType = ['nodes', 'links'] ## either links or nodes
folderName = [r'Nodes/'+variableOfInterest+'/', r'SplitFiles_Day/']
internalFolderName = ['/day', '/SplitFiles']

### For year 2022
if year=="2022":
    totalMonths = ['03','04','05','06','07','08','09','10','11','12']

### For year 2023
if year=="2023":
    totalMonths = ['01','02','03','04','05']

for i in set(totalMonths): # for classified by months files
   
    ### nodes for financial stability data
    jsonFilePath1 = folderName[0] + year + internalFolderName[0] + day +'/json_'+jsonType[0]
    jsonFile1 = jsonFilePath1 +'/SocialNetwork'+ i +'_'+jsonType[0]+'.json'       

    ### links from Month data
    # jsonFile2 = 'SplitFiles_Month/'+ year +'/json_'+jsonType[1]+'/SocialNetwork'+ month +'_'+jsonType[1]+'.json'    
    # jsonFileOutput = r'Files for Observable/Month/SocialNetwork'+year + month +'.json'

    ### links from Day data (example: 2022-03-01T00:00:00Z)
    jsonFilePath2 = folderName[1] + year + internalFolderName[1] + day +'/json_'+jsonType[1]
    jsonFile2 = jsonFilePath2 +'/SocialNetwork'+ i +'_'+jsonType[1]+'.json'    

    jsonFileOutputPath = r'Files for Observable/'+variableOfInterest+'/Day/' + day
    jsonFileOutput = jsonFileOutputPath + '/SocialNetwork' + year + i + day + '.json'
   
    # load json file into dictionaries
    # Opening JSON file
    with open(jsonFile1) as json_file:
        dict1 = json.load(json_file)
    
    with open(jsonFile2) as json_file:
        dict2 = json.load(json_file)
    
    dict3={"nodes":dict1, "links":dict2}
    
    with open(jsonFileOutput, "w") as outfile:
        json.dump(dict3, outfile, indent=4)
