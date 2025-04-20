# Overview

This FP&A Analytics case study is helpful for finance or data professionals who want a real world look at business practices for financial/accounting data analytics. You can follow along on my website www.NikoFrance.com for my writeup and step by step analysis and or you can view this repository for a deeper look at my files, datasets, and codebase for this project. 

The data, resources, and scripts for this project are all made to be self contained. For users who want to replicate themselves on their local machine, simply clone the repository to your own machine and run the required scripts in order and update the necessary file paths by either hardcoding or creating your own .env file.

## Project Setup

1. Set file paths for:
- output_folder
- csv_folder
- database_file

    These paths need to be updated inside of sqlitedb.py, csvpreprocessing.py, and import.py

    Conversely, the .env file can also be updated to reduce the amount of work spent manually updating file paths.

2. Install dependencies and libraries from requirements.txt

3. Run sqlitedb.py to initialize the sqlite database and create all of the necessary tables

4. Run csvpreprocessing.py to clean up the csv file imports and move them to a new folder

5. Run import.py to upload the cleaned up csv data into the database
