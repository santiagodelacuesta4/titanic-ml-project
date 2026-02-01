import pandas as pd
from pathlib import Path
    
class TitanicDataset:
    def __init__(self, data_path: str):
        self.data_path = Path(data_path)
    
    def load(self) -> pd.DataFrame:
        return pd.read_csv(self.data_path)
       
    def basic_cleaning(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        df["Age"] = df["Age"].fillna(df["Age"].median())
        df["Embarked"] = df["Embarked"].fillna("Unknown")
        return df