import sqlite3
import pandas as pd
import numpy
import os

conn = sqlite3.connect('fineWine.db')
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")

results = cursor.fetchall()

print(results)

conn.commit()

conn.close()