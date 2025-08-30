import pandas as pd

def transform_data(df):
    """
    Transform: Membersihkan dan mengolah data
    """
    print("\n=== TRANSFORM PHASE ===")
    
    # Buat copy untuk transformasi
    df_clean = df.copy()
    
    print(f"Original data shape: {df_clean.shape}")
    
    # 1. Hapus duplikasi
    print("\n1. Removing duplicates...")
    before_dup = len(df_clean)
    df_clean = df_clean.drop_duplicates()
    after_dup = len(df_clean)
    print(f"Removed {before_dup - after_dup} duplicates")
    
    # 2. Handle missing values
    print("\n2. Handling missing values...")
    print("Missing values before cleaning:")
    print(df_clean.isnull().sum())
    
    # Hapus baris dengan CustomerID kosong (karena penting untuk analisis)
    df_clean = df_clean.dropna(subset=['CustomerID'])
    
    # Isi Description kosong dengan 'Unknown Product'
    df_clean['Description'] = df_clean['Description'].fillna('Unknown Product')
    
    print("Missing values after cleaning:")
    print(df_clean.isnull().sum())
    
    # 3. Konversi format tanggal
    print("\n3. Converting date format...")
    df_clean['InvoiceDate'] = pd.to_datetime(df_clean['InvoiceDate'])
    
    # 4. Tambah kolom baru untuk analisis
    print("\n4. Adding calculated columns...")
    df_clean['TotalAmount'] = df_clean['Quantity'] * df_clean['UnitPrice']
    df_clean['Year'] = df_clean['InvoiceDate'].dt.year
    df_clean['Month'] = df_clean['InvoiceDate'].dt.month
    df_clean['DayOfWeek'] = df_clean['InvoiceDate'].dt.day_name()
    
    # 5. Filter data yang valid (quantity dan price positif)
    print("\n5. Filtering valid transactions...")
    before_filter = len(df_clean)
    df_clean = df_clean[(df_clean['Quantity'] > 0) & (df_clean['UnitPrice'] > 0)]
    after_filter = len(df_clean)
    print(f"Filtered out {before_filter - after_filter} invalid transactions")
    
    # 6. Konversi tipe data
    df_clean['CustomerID'] = df_clean['CustomerID'].astype(int)
    df_clean['InvoiceNo'] = df_clean['InvoiceNo'].astype(str)
    df_clean['StockCode'] = df_clean['StockCode'].astype(str)
    
    print(f"\nFinal cleaned data shape: {df_clean.shape}")
    print("\nCleaned data info:")
    print(df_clean.info())
    
    return df_clean