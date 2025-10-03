# IEEE VAST Challenge 2022

### This repository contains data files and Python codes for data pre-processing for analyzing *Social Network* and *Activity Logs* data from the IEEE VAST challenge 2022 dataset: https://vast-challenge.github.io/2022/.


Below are the steps to create JSON files for use as an input for plotting '**Force-Directed Graph**' at Observable <https://observablehq.com/d/4deea9e48e5f9da4>:

**🧪 Step 1: Download the original file** - Download the original *'SocialNetwork.csv'* file from the link: https://vast-challenge.github.io/2022/. It should be found in the folder "VAST-Challenge-2022/Datasets/Journals".

**🧪 Step 2: Create files for a specific *Day*** - Create an empty folder named "SplitFiles*Day*" (example, SplitFiles01) at location "/Analysis/SocialNetwork/SplitFiles_Day/2022", for the year 2022. Run script 'SplitCsvFiles_day.py' to create SocialNetwork files for a particular day and time, based on months.

**🧪 Step 3: Convert the CSV files to the links format** - Create an empty folder named "links" inside the "SplitFiles*Day*" folder. Run script *'CsvToLinks_Month.py'*.

**🧪 Step 4: Convert the links files to the JSON format** - Create an empty folder named "json_links" inside the  "SplitFiles*Day*" folder. Run script *'CsvToJson_Month.py'*.

**🧪 Step 5: Choose variableOfInterest representing the color of the nodes and create node files** - Create an empty folder named "day*Day*" (example, day01) at location "/Analysis/SocialNetwork/Nodes/currentMode/2022", for year 2022 and variableOfInterest: currentMode. Create an empty folder named "nodes" inside the "day*Day*" folder. Run script *'currentModetoCsv_nodes.py'*.

**🧪 Step 6: Convert the node files to the JSON format** - Create an empty folder named "json_nodes" inside the "day*Day*" folder. Run script *'CsvToJson_Month.py'*.

**🧪 Step 7: Combine nodes and links into one JSON file** - Create an empty folder named "*Day*" (example, 01) at location "/Analysis/SocialNetwork/Files for Observable/currentMode/Day", for variableOfInterest: currentMode. Run script *'concatenateNodesLinks.py'*.

**🧪 Step 8: Upload the JSON files to the Observable link** - The JSON files are ready to be plugged into the '**Force-Directed Graph**' at Observable <https://observablehq.com/d/4deea9e48e5f9da4>. Upload the JSON files from the location "/Analysis/SocialNetwork/Files for Observable" to the online Observable link.

**🧪 Step 9: Edit the filename on Observable and view the graph** - Edit the filename at the online Observable link at line: "SocialNetwork = FileAttachment("filename.json").json()", for example, FileAttachment("SocialNetwork20220303.json"). Hit play to view the graph.

--

💡Figma design board: https://www.figma.com/proto/uJhwBBpo6kkk0aCJmvxOff/IEEE-VAST-Challenge-2022
