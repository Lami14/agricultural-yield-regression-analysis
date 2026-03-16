import pandas as pd

def test_dataset_not_empty():
    df = pd.read_csv("sampled_field_df.csv")
    assert len(df) > 0


def test_target_variable_exists():
    df = pd.read_csv("sampled_field_df.csv")
    assert "Standard_yield" in df.columns


def test_no_missing_values():
    df = pd.read_csv("sampled_field_df.csv")
    assert df.isnull().sum().sum() == 0
