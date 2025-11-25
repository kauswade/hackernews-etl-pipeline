from sqlalchemy import create_engine
import pandas as pd

# Connect to the DB
db_connection_str = 'postgresql://postgres:postgres@postgres:5432/dev'
db_connection = create_engine(db_connection_str)

# Read the table we just filled
print(pd.read_sql("SELECT * FROM tech_trends_daily ORDER BY count DESC LIMIT 10;", db_connection))