def create_database_schema():
    """
    Membuat schema database dan tabel
    """
    schema_sql = """
    CREATE DATABASE IF NOT EXISTS ecommerce_etl;
    USE ecommerce_etl;
    
    DROP TABLE IF EXISTS transactions;
    
    CREATE TABLE transactions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        InvoiceNo VARCHAR(20) NOT NULL,
        StockCode VARCHAR(20) NOT NULL,
        Description TEXT,
        Quantity INT NOT NULL,
        InvoiceDate DATETIME NOT NULL,
        UnitPrice DECIMAL(10,2) NOT NULL,
        CustomerID INT NOT NULL,
        Country VARCHAR(50) NOT NULL,
        TotalAmount DECIMAL(10,2) NOT NULL,
        Year INT NOT NULL,
        Month INT NOT NULL,
        DayOfWeek VARCHAR(10) NOT NULL,
        INDEX idx_customer (CustomerID),
        INDEX idx_invoice (InvoiceNo),
        INDEX idx_date (InvoiceDate),
        INDEX idx_country (Country)
    );
    """
    return schema_sql