from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

def load_academic_data():
    return pd.read_csv(DATA_DIR / "academic_records.csv")

def load_productivity_data():
    return pd.read_csv(DATA_DIR / "productivity_records.csv")

def calculate_performance(df):
    df = df.copy()
    df["performance_score"] = (
        df["marks"] * 0.30
        + df["attendance"] * 0.20
        + df["assignment_score"] * 0.20
        + df["quiz_score"] * 0.15
        + (df["study_hours"].clip(0, 8) / 8 * 100) * 0.15
    )
    return df
