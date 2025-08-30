import pandas as pd
from sqlalchemy import create_engine, text
from etl.schema import create_database_schema

def load_data_to_csv(df, output_file):
    print(f"\n=== LOAD TO CSV ===")
    df.to_csv(output_file, index=False)
    print(f"Data saved to {output_file}")

def load_data_to_mysql(df, connection_params):
    print(f"\n=== LOAD TO MYSQL ===")
    try:
        engine = create_engine(
            f"mysql+mysqlconnector://{connection_params['user']}:{connection_params['password']}@{connection_params['host']}:{connection_params['port']}"
        )

        # Buat database & tabel
        with engine.connect() as conn:
            schema_commands = create_database_schema().split(';')
            for command in schema_commands:
                if command.strip():
                    conn.execute(text(command))

        # Reconnect ke db
        engine = create_engine(
            f"mysql+mysqlconnector://{connection_params['user']}:{connection_params['password']}@{connection_params['host']}:{connection_params['port']}/ecommerce_etl"
        )

        # Load data
        df.to_sql('transactions', engine, if_exists='append', index=False, chunksize=1000)

        print(f"Successfully loaded {len(df)} records")
        return engine

    except Exception as e:
        print(f"Error loading data to MySQL: {e}")
        return None
