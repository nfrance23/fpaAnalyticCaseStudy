import sqlite3
import pandas as pd
import os

# Connect to the database
conn = sqlite3.connect('fineWine.db')
cursor = conn.cursor()

# Get all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()

print("Tables in database:")
for table in tables:
    table_name = table[0]
    print(f"\n{table_name} Schema:")
    
    # Get schema information for each table
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()
    
    # Create a DataFrame to display the schema nicely
    schema_df = pd.DataFrame(columns, 
                            columns=['cid', 'name', 'type', 'notnull', 'dflt_value', 'pk'])
    print(schema_df[['name', 'type', 'pk']])
    
    # Optionally, you can also get foreign key information
    cursor.execute(f"PRAGMA foreign_key_list({table_name})")
    foreign_keys = cursor.fetchall()
    
    if foreign_keys:
        print(f"\nForeign Keys for {table_name}:")
        fk_df = pd.DataFrame(foreign_keys, 
                           columns=['id', 'seq', 'table', 'from', 'to', 'on_update', 'on_delete', 'match'])
        print(fk_df[['table', 'from', 'to']])

# Close the connection
conn.close()