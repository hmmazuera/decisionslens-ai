from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "logistic_regression_model.pkl"

VECTORIZER_PATH = BASE_DIR / 'models' / 'tfidf_vectorizer_2.pkl'

APP_TITLE = 'DecisionLens AI'
APP_SUBTITLE = 'Structure your decisions with AI'

OPENROUTER_MODEL = "openrouter/free"

LABELS = {
    1: 'Supporting argument',
    -1: 'Opposing argument',
}