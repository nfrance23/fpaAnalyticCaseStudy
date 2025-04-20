import sqlite3
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

output_folder = os.getenv('output_folder')

database_file = os.getenv('database_file')

table_names = ['Employees','Cash_Receipts','Customers', 'Inventory','Invoice_Detail','Invoice_Summary','Sales_Order_Detail','Sales_Order_Summary']

try:
    conn = sqlite3.connect('fineWine.db')
    cursor = conn.cursor()

    for table_name in table_names:
        csv_filename = os.path.join(output_folder, f"{table_name}.csv")

        if os.path.exists(csv_filename):
            print(f"Attempting to read: {csv_filename}")
            try:
                df = pd.read_csv(csv_filename, encoding = 'utf-8')

                columns = ", ".join(df.columns)
                placeholders = ", ".join(['?'] * len(df.columns))

                sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

                for index, row in df.iterrows():
                    cursor.execute(sql, row.values.tolist())

                conn.commit()
                print(f"Data from '{csv_filename}' imported successfully into '{table_name}' table. ")

            except pd.errors.EmptyDataError:
                print(f"Warning: '{csv_filename}' is empty. Skipping import for '{table_name}'.")
            except pd.errors.ParserError as e:
                print(f"Error parsing CSV file '{csv_filename}': {e}")
            except sqlite3.Error as e:
                conn.rollback()
                print(f"SQLite error while importing into '{table_name}': {e}")
        else:
            print(f"Warning: CSV file '{csv_filename}' not found.")

except sqlite3.Error as e: 
    print(f"Error connecting to the database: {e}")

finally:
    if conn:
        conn.close()

