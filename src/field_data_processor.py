import pandas as pd
import re

class FieldDataProcessor:

    def __init__(self, config):
        self.config = config
        self.df = None

    def process(self):
        """
        Load and clean dataset
        """
        import pandas as pd
        from sqlalchemy import create_engine

        engine = create_engine(self.config["db_path"])
        self.df = pd.read_sql(self.config["sql_query"], engine)

        # Rename columns
        self.df = self.df.rename(columns=self.config["columns_to_rename"])

        # Fix incorrect values
        for wrong, correct in self.config["values_to_rename"].items():
            self.df = self.df.replace(wrong, correct)

        return self.df
