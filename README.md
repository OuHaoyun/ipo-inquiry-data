# IPO Business Inquiries Data Processing
## Table of Contents
* Introduction
* Features
* Prerequisites
* Installation
* Usage

## Introduction
This project aims to automate the processing of IPO business inquiries data. The code is capable of reading multiple CSV files, merging them based on industry codes, filtering and cleaning the text fields, and finally exporting the processed data to both CSV and TXT formats.

## Features
Reading Excel and CSV data files
Data cleaning and text preprocessing
Data merging based on industry classification
Exporting processed data to TXT and CSV formats

## Prerequisites
Before you begin, ensure you have met the following requirements:
* Python version 3.11
* pandas library (See requirements.txt for version details)

## Installation
Clone the repository to your local machine.
```
git clone https://gitlab.com/haoyunou/ipo-inquiry-editor.git
```

## Install the required packages
```
pip install -r requirements.txt
```

## Usage
Update the constants.py with the appropriate file paths.
Run main.py to execute the data processing.
```
python main.py
```

