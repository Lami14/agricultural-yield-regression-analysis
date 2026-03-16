import pandas as pd

def create_temperature_range(df):
    """
    Create new feature Temperature_Range
    """
    df["Temperature_Range"] = df["Max_temperature_C"] - df["Min_temperature_C"]
    return df


def encode_categorical(df):
    """
    Convert categorical variables using dummy encoding
    """
    categorical_cols = ["Location", "Soil_type", "Crop_type"]
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    return df
