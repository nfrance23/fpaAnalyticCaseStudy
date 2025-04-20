import sqlite3
import pandas as pd
import os
from datetime import datetime
import numpy as np

# Create a new SQLite database
conn = sqlite3.connect('fineWine.db')
cursor = conn.cursor()

# Create tables with appropriate data types and relationships
cursor.execute('''
CREATE TABLE IF NOT EXISTS Employees (
    Emp_ID INTEGER PRIMARY KEY,
    First_Name TEXT,
    Last_Name TEXT,
    E_mail_Address TEXT,
    Department TEXT,
    Job_Title TEXT,
    Address TEXT,
    City TEXT,
    State TEXT,
    Zip_Code INTEGER,
    Status TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Customers (
    Cust_Num TEXT PRIMARY KEY,
    Comp_Name TEXT,
    First_Name TEXT,
    Last_Name TEXT,
    Phone_Num TEXT,
    Street_Address TEXT,
    City TEXT,
    State TEXT,
    Zip INTEGER,
    Category TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Inventory (
    Brand_ID TEXT PRIMARY KEY,
    Brand_Name TEXT,
    Category TEXT,
    Price REAL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Sales_Order_Summary (
    SO_Num REAL PRIMARY KEY,
    SO_Date TEXT,
    Emp_ID INTEGER,
    Cust_Num TEXT,
    FOREIGN KEY (Emp_ID) REFERENCES Employees(Emp_ID),
    FOREIGN KEY (Cust_Num) REFERENCES Customers(Cust_Num)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Sales_Order_Detail (
    SO_Num REAL,
    Brand_ID TEXT,
    Quantity_Ordered INTEGER,
    Price REAL,
    PRIMARY KEY (SO_Num, Brand_ID),
    FOREIGN KEY (SO_Num) REFERENCES Sales_Order_Summary(SO_Num),
    FOREIGN KEY (Brand_ID) REFERENCES Inventory(Brand_ID)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Invoice_Summary (
    Invoice_Num TEXT PRIMARY KEY,
    Delivery_Date TEXT,
    Invoice_Date TEXT,
    SO_Num REAL,
    Sales_Total REAL,
    Freight_Charge REAL,
    FOREIGN KEY (SO_Num) REFERENCES Sales_Order_Summary(SO_Num)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Invoice_Detail (
    Invoice_Num TEXT,
    Brand_ID TEXT,
    Quantity_Sold INTEGER,
    PRIMARY KEY (Invoice_Num, Brand_ID),
    FOREIGN KEY (Invoice_Num) REFERENCES Invoice_Summary(Invoice_Num),
    FOREIGN KEY (Brand_ID) REFERENCES Inventory(Brand_ID)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Cash_Receipts (
    Remit_Nums TEXT,
    Receipt_Date TEXT,
    Invoice_Num TEXT,
    Discount REAL,
    Receipt_Amt REAL,
    Account_Num INTEGER,
    PRIMARY KEY (Remit_Nums, Invoice_Num),
    FOREIGN KEY (Invoice_Num) REFERENCES Invoice_Summary(Invoice_Num)
)
''')

conn.commit()

conn.close()