import sqlite3
import pandas as pd
import os
from datetime import datetime
import numpy as np

# Create a new SQLite database
conn = sqlite3.connect('fineWine.db')
cursor = conn.cursor()

cursor.execute('''
    SELECT emp_id FROM employees;
''')

results = cursor.fetchall()

print(results)

conn.close()