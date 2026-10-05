from pathlib import Path
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "ml_training_data.csv"

FEATURES = [
    "study_hours",
    "attendance",
    "assignment_completion",
    "quiz_score",
    "previous_marks",
    "consistency"
]

def train_model():
    df = pd.read_csv(DATA_FILE)

    X = df[FEATURES]
    y = df["performance"]

    model = RandomForestClassifier(
        n_estimators=150,
        random_state=42
    )
    model.fit(X, y)
    return model

def predict_performance(model, study_hours, attendance, assignment, quiz, previous, consistency):
    sample = pd.DataFrame([{
        "study_hours": study_hours,
        "attendance": attendance,
        "assignment_completion": assignment,
        "quiz_score": quiz,
        "previous_marks": previous,
        "consistency": consistency
    }])
    return model.predict(sample)[0]
