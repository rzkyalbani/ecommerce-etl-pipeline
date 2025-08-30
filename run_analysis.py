from config import mysql_params
from analysis.queries import run_analysis_queries
from sqlalchemy import create_engine

engine = create_engine(
    f"mysql+mysqlconnector://{mysql_params['user']}:{mysql_params['password']}@{mysql_params['host']}:{mysql_params['port']}/ecommerce_etl"
)

run_analysis_queries(engine)
