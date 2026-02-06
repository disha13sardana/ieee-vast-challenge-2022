# IEEE VAST Challenge 2022 - Social Network Analysis

A data preprocessing pipeline for analyzing Social Network and Activity Logs data from the IEEE VAST Challenge 2022 dataset, designed to create interactive force-directed graph visualizations.

## 📊 Overview

This project processes social network data from the [IEEE VAST Challenge 2022](https://vast-challenge.github.io/2022/) and prepares it for visualization using Observable's Force-Directed Graph. The pipeline transforms raw CSV data into JSON files with nodes and links formatted for graph visualization.

## 🎯 Features

- **Day-wise data splitting**: Break down social network data by specific days and months
- **Flexible node attributes**: Support for various node characteristics (currentMode, etc.)
- **JSON generation**: Automated conversion from CSV to visualization-ready JSON format
- **Observable integration**: Direct compatibility with Observable notebooks

## 🚀 Quick Start

### Prerequisites

- Python 3.x
- Required Python libraries - No external pip installs needed beyond standard data science stack
- Access to the IEEE VAST Challenge 2022 dataset

### Installation

1. Clone this repository:
```bash
git clone https://github.com/disha13sardana/ieee-vast-challenge-2022.git
cd ieee-vast-challenge-2022
```

2. Download the original dataset:
   - Visit [IEEE VAST Challenge 2022](https://vast-challenge.github.io/2022/)
   - Download `SocialNetwork.csv` from `VAST-Challenge-2022/Datasets/Journals`

## 📖 Usage Guide

### Step 1: Download Original Data
Download `SocialNetwork.csv` from the [IEEE VAST Challenge 2022 dataset](https://vast-challenge.github.io/2022/) located in `VAST-Challenge-2022/Datasets/Journals`.

### Step 2: Split Data by Day
Create day-specific files organized by month:

```bash
# Create directory structure
mkdir -p Analysis/SocialNetwork/SplitFiles_Day/2022

# Run the splitting script
python SplitCsvFiles_day.py
```

This creates files for each specific day and time based on months.

### Step 3: Generate Links Format
Convert CSV files to links format:

```bash
# Create links directory
mkdir -p Analysis/SocialNetwork/SplitFiles_Day/links

# Run conversion
python CsvToLinks_Month.py
```

### Step 4: Convert Links to JSON
Transform links files into JSON format:

```bash
# Create JSON links directory
mkdir -p Analysis/SocialNetwork/SplitFiles_Day/json_links

# Run JSON conversion
python CsvToJson_Month.py
```

### Step 5: Create Node Files
Generate node files with your chosen attribute (e.g., `currentMode`):

```bash
# Create directory for node data
mkdir -p Analysis/SocialNetwork/Nodes/currentMode/2022/day01/nodes

# Generate node CSV files
python currentModetoCsv_nodes.py
```

### Step 6: Convert Nodes to JSON
Transform node CSV files to JSON:

```bash
# Create JSON nodes directory
mkdir -p Analysis/SocialNetwork/Nodes/currentMode/2022/day01/json_nodes

# Run conversion
python CsvToJson_Month.py
```

### Step 7: Combine Nodes and Links
Merge nodes and links into unified JSON files:

```bash
# Create output directory
mkdir -p "Analysis/SocialNetwork/Files for Observable/currentMode/Day/01"

# Concatenate data
python concatenateNodesLinks.py
```

### Step 8: Visualize on Observable
Upload your generated JSON files to the [Force-Directed Graph on Observable](https://observablehq.com/d/4deea9e48e5f9da4).

### Step 9: View Your Graph
In Observable, update the file reference:

```javascript
SocialNetwork = FileAttachment("SocialNetwork20220303.json").json()
```

Replace `"SocialNetwork20220303.json"` with your filename and click play to render the visualization.

## 📁 Project Structure

```
ieee-vast-challenge-2022/
├── Analysis/
│   └── SocialNetwork/
│       ├── SplitFiles_Day/
│       │   └── 2022/
│       ├── Nodes/
│       │   └── currentMode/
│       │       └── 2022/
│       └── Files for Observable/
├── Figma design board/
├── SplitCsvFiles_day.py
├── CsvToLinks_Month.py
├── CsvToJson_Month.py
├── currentModetoCsv_nodes.py
└── concatenateNodesLinks.py
```

## 🎨 Design Resources

View the project design board: [Figma Design Board](https://www.figma.com/proto/uJhwBBpo6kkk0aCJmvxOff/IEEE-VAST-Challenge-2022)

## 🔗 Resources

- **Dataset**: [IEEE VAST Challenge 2022](https://vast-challenge.github.io/2022/)
- **Visualization**: [Force-Directed Graph on Observable](https://observablehq.com/d/4deea9e48e5f9da4)
- **Design Board**: [Figma Project](https://www.figma.com/proto/uJhwBBpo6kkk0aCJmvxOff/IEEE-VAST-Challenge-2022)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/disha13sardana/ieee-vast-challenge-2022/issues).

## 📝 License

This project is part of the IEEE VAST Challenge 2022. Please refer to the [IEEE VAST Challenge](https://vast-challenge.github.io/2022/) for data usage terms.

## 👤 Author

**Disha Sardana**
- GitHub: [@disha13sardana](https://github.com/disha13sardana)

## 🙏 Acknowledgments

- IEEE VAST Challenge organizers for providing the dataset
- Observable community for the force-directed graph visualization template

