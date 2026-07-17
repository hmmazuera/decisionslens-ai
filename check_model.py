import joblib

from app.constants import VECTORIZER_PATH


vectorizer = joblib.load(VECTORIZER_PATH)

print("File:", VECTORIZER_PATH)
print("Type:", type(vectorizer))
print("Vocabulary:", len(vectorizer.vocabulary_))
print("Has idf:", hasattr(vectorizer, "idf_"))

if hasattr(vectorizer, "idf_"):
    print("IDF shape:", vectorizer.idf_.shape)

test_vector = vectorizer.transform(
    ["the new job offers a higher salary"]
)

print("Transform shape:", test_vector.shape)