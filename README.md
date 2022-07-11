# IEEE VAST Challenge 2022

### This repository contains data files and python codes for data pre-processing for analyzing Social Network data from the IEEE VAST challenge 2022 dataset: https://vast-challenge.github.io/2022/.

Below are the steps to create json files for using as an input for plotting '**Force-Directed Graph**' at Observable <https://observablehq.com/d/4deea9e48e5f9da4>:

**Step 1: Download the original file**

Download the original *'SocialNetwork.csv'* file from the link: https://vast-challenge.github.io/2022/. It should be found in folder "VAST-Challenge-2022/Datasets/Journals".

**Step 2: Create files for a specific *Day***

Create an empty folder named "SplitFiles*Day*" (example, SplitFiles01) at location "/Analysis/SocialNetwork/SplitFiles_Day/2022", for year 2022. Run script 'SplitCsvFiles_day.py' to create SocialNetwork files for a particular day and time, based on months.

**Step 3: Convert the csv files to the links format** 

Create an empty folder named "links" inside the "SplitFiles*Day*" folder. Run script *'CsvToLinks_Month.py'*.

**Step 4: Covert the links files to the json format**

Create an empty folder named "json_links" inside the  "SplitFiles*Day*" folder. Run script *'CsvToJson_Month.py'*.

**Step 5: Choose variableOfInterest representing the color of the nodes and create nodes files**
 
Create an empty folder named "day*Day*" (example, day01) at location "/Analysis/SocialNetwork/Nodes/currentMode/2022", for year 2022 and variableOfInterest: currentMode. Create an empty folder named "nodes" inside the "day*Day*" folder. Run script *'currentModetoCsv_nodes.py'*.

**Step 6: Convert the nodes files to the json format** 

Create an empty folder named "json_nodes" inside the "day*Day*" folder. Run script *'CsvToJson_Month.py'*.

**Step 7: Combine nodes and links into one json file** 

Create an empty folder named "*Day*" (example, 01) at location "/Analysis/SocialNetwork/Files for Observable/currentMode/Day", for variableOfInterest: currentMode. Run script *'concatenateNodesLinks.py'*.

**Step 8: Upload the json files to the Observable link** 

The json files are ready to be plugged into '**Force-Directed Graph**' at Observable <https://observablehq.com/d/4deea9e48e5f9da4>. Upload the json files from the location "/Analysis/SocialNetwork/Files for Observable" to the online Observable link.

**Step 9: Edit filename on Observable and view the graph** 

Edit the filename at the online Observable link at line: "SocialNetwork = FileAttachment("filename.json").json()", for example FileAttachment("SocialNetwork20220303.json"). Hit play to view the graph.
