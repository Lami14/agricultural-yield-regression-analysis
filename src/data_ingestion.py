import pandas as pd
from sqlalchemy import create_engine

def load_data(db_path, sql_query):
    """
    Load data from SQLite database using SQL query
    """
    engine = create_engine(db_path)
    df = pd.read_sql(sql_query, engine)
    return df


def save_to_csv(df, filename):
    """
    Save dataframe to CSV
    """
    df.to_csv(filename, index=False)
