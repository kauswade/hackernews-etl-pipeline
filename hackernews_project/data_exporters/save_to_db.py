import pandas as pd
from sqlalchemy import create_engine

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

@data_exporter
def export_data(df, *args, **kwargs):
    """
    Export data to PostgreSQL
    """
    # Connection to the 'postgres' service defined in Docker
    db_connection_str = 'postgresql://postgres:postgres@postgres:5432/dev'
    db_connection = create_engine(db_connection_str)

    table_name = 'tech_trends_daily'
    
    # Sanity check print
    print(f"Exporting {len(df)} rows to table '{table_name}'...")

    # Write data to SQL
    df.to_sql(table_name, db_connection, if_exists='append', index=False)
    
    return df