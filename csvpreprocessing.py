import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

csv_folder = os.getenv('csv_folder')
output_folder = os.getenv('output_folder')

csv_folder = os.path.normpath(csv_folder)
output_folder = os.path.normpath(output_folder)

# Create output directory if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# File encoding mapping
file_encodings = {
    'Customers.csv': 'cp1252',
    'Inventory.csv': 'latin1',  # Try latin1 instead of cp1252 for Inventory.csv
    # Default for all others
    'default': 'utf-8'
}

# Process each CSV file
for filename in os.listdir(csv_folder):
    if filename.endswith('.csv'):
        input_path = os.path.join(csv_folder, filename)
        output_path = os.path.join(output_folder, filename)
        
        # Get the appropriate encoding
        encoding = file_encodings.get(filename, file_encodings['default'])
        
        try:
            print(f"Processing {filename} with {encoding} encoding...")
            # Read with the specified encoding
            df = pd.read_csv(input_path, encoding=encoding)
            
            # Save with consistent UTF-8 encoding
            df.to_csv(output_path, index=False, encoding='utf-8')
            print(f"Successfully converted and saved {filename}")
            
        except Exception as e:
            print(f"Error processing {filename}: {e}")
            
            # Fallback approach for problematic files
            if filename == 'Inventory.csv':
                try:
                    print(f"Trying fallback method for {filename}...")
                    # Try with errors='replace' to handle problematic characters
                    df = pd.read_csv(input_path, encoding='latin1', errors='replace')
                    df.to_csv(output_path, index=False, encoding='utf-8')
                    print(f"Successfully converted and saved {filename} with fallback method")
                except Exception as e2:
                    print(f"Fallback method also failed for {filename}: {e2}")