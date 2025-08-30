import pandas as pd

def run_analysis_queries(engine):
    """
    Menjalankan query analisis
    """
    print(f"\n=== ANALYSIS QUERIES ===")
    
    if engine is None:
        print("No database connection available. Skipping SQL analysis.")
        return
    
    queries = {
        "Total Sales per Customer (Top 10)": """
            SELECT CustomerID, 
                   COUNT(*) as total_transactions,
                   SUM(TotalAmount) as total_spent
            FROM transactions 
            GROUP BY CustomerID 
            ORDER BY total_spent DESC 
            LIMIT 10;
        """,
        
        "Top 10 Best Selling Products": """
            SELECT StockCode, Description,
                   SUM(Quantity) as total_quantity_sold,
                   SUM(TotalAmount) as total_revenue
            FROM transactions 
            GROUP BY StockCode, Description 
            ORDER BY total_quantity_sold DESC 
            LIMIT 10;
        """,
        
        "Sales by Country": """
            SELECT Country,
                   COUNT(*) as total_transactions,
                   SUM(TotalAmount) as total_revenue
            FROM transactions 
            GROUP BY Country 
            ORDER BY total_revenue DESC;
        """,
        
        "Monthly Sales Trend": """
            SELECT Year, Month,
                   COUNT(*) as total_transactions,
                   SUM(TotalAmount) as total_revenue
            FROM transactions 
            GROUP BY Year, Month 
            ORDER BY Year, Month;
        """
    }
    
    with engine.connect() as conn:
        for query_name, query in queries.items():
            print(f"\n{query_name}:")
            print("-" * 50)
            result = pd.read_sql(query, conn)
            print(result)