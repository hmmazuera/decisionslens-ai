import joblib
from constants import MODEL_PATH, VECTORIZER_PATH, OPENROUTER_MODEL
import os
from dotenv import load_dotenv
from openai import OpenAI
from prompts import DECISION_ANALYSIS_PROMPT
import streamlit as st

load_dotenv()

def create_openrouter_client():
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        api_key = st.secrets["OPENROUTER_API_KEY"]
    return OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )

def load_model():
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)

    vectorizer.transform(["test sentence"])

    return model, vectorizer

def preprocess_text(text):
    text = text.lower()
    text = ' '.join(text.split())
    return text

def predict_argument(text, model, vectorizer):
    clean_text = preprocess_text(text)
    text_vector = vectorizer.transform([clean_text])
    prediction = model.predict(text_vector)[0]
    probability = model.predict_proba(text_vector).max()
    return prediction, probability

def analyze_decision(decision, stance, confidence):
    client = create_openrouter_client()
    prompt = DECISION_ANALYSIS_PROMPT.format(
        decision=decision,
        stance=stance,
        confidence=confidence
    )
    response = client.chat.completions.create(
        model=OPENROUTER_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content