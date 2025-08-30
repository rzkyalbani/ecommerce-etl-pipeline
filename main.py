from config import mysql_params, file_paths
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data_to_csv, load_data_to_mysql
from analysis.queries import run_analysis_queries 

def main():
    print("Starting ETL Pipeline...")
    print("=" * 50)

    raw_data = extract_data(file_paths['raw_data'])
    cleaned_data = transform_data(raw_data)
    load_data_to_csv(cleaned_data, file_paths['cleaned_data'])
    engine = load_data_to_mysql(cleaned_data, mysql_params)

    # Analysis
    run_analysis_queries(engine) 

    print("\nPipeline completed successfully!")

if __name__ == "__main__":
    main()