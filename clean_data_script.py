# clean_data_script.py
import pandas as pd
import numpy as np
import sys
import logging
from datetime import datetime

# Configure logging to save errors to a log file
LOG_FILE = f'error_log_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
logging.basicConfig(filename=LOG_FILE, level=logging.WARNING,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def clean_data(input_file, output_file='clean_output.csv'):
    """
    Automates the cleaning, standardization, and transformation of CSV data
    using Pandas, saving the result to a new CSV file.
    """
    print(f"Starting data cleaning for: {input_file}...")
    
    # 1. Data Intake and Error Check
    try:
        # Attempt to read the file, handling common encoding issues
        df = pd.read_csv(input_file, encoding='utf-8')
    except UnicodeDecodeError:
        try:
            df = pd.read_csv(input_file, encoding='latin1')
        except Exception as e:
            print(f"Fatal Error: Could not read file due to encoding or format issues.")
            logging.error(f"File read failure: {e}")
            sys.exit(1)

    initial_rows = len(df)
    
    # --- CORE CLEANING LOGIC (Session 2 Focus) ---
    
    # 2. Column Standardization (TRIM column names)
    df.columns = df.columns.str.strip().str.replace('[^A-Za-z0-9_]+', '', regex=True)
    
    # 3. Data Cleaning (TRIM, Remove Duplicates)
    
    # a. TRIM whitespace from all string columns (Key Fiverr deliverable)
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.strip().replace('', np.nan) # Replace empty strings with NaN
    
    # b. Drop Exact Duplicates
    df.drop_duplicates(inplace=True)
    rows_dropped = initial_rows - len(df)
    
    # 4. Data Transformation (Example of CONCAT/Formatting)
    
    # **NOTE:** The following lines are placeholders. They should be customized
    # based on the client's exact column names and requirements.
    
    # Example 1: CONCAT (Creating a new ID)
    if 'Product_ID' in df.columns and 'SKU_Suffix' in df.columns:
        df['Full_SKU'] = df['Product_ID'].astype(str) + '-' + df['SKU_Suffix'].astype(str)

    # Example 2: Simple Data Validation (Flagging rows with missing critical data)
    # Assuming 'Name' and 'Cost' are critical columns
    for index, row in df.iterrows():
        if pd.isna(row['Name']) or pd.isna(row['Cost']):
            logging.warning(f"Row {index}: Missing critical data (Name/Cost).")

    # --- END CORE CLEANING LOGIC ---

    # 5. Output Generation
    try:
        df.to_csv(output_file, index=False)
    except Exception as e:
        print(f"Error: Could not write output file.")
        logging.error(f"Output write failure: {e}")

    print("\n--- Processing Complete ---")
    print(f"Original rows: {initial_rows}")
    print(f"Total duplicates removed: {rows_dropped}")
    print(f"Clean data saved to: {output_file}")
    print(f"Check {LOG_FILE} for any data irregularities.")


if __name__ == "__main__":
    # Ensure pandas is installed: pip install pandas
    if len(sys.argv) < 2:
        print("Usage: python clean_data_script.py <input_file.csv>")
    else:
        # The input file is the first argument passed to the script
        clean_data(sys.argv[1])
