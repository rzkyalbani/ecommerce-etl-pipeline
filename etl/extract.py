import pandas as pd

def extract_data(file_path):
    """
    Extract: Membaca data dari CSV
    """
    print("=== EXTRACT PHASE ===")
    print(f"Reading data from {file_path}...")
    
    df = pd.read_csv(file_path, encoding="ISO-8859-1")
    
    print(f"Data shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    print("\nData info:")
    print(df.info())
    print("\nFirst 5 rows:")
    print(df.head())
    
    return df