import joblib
import re
import string

# Charger le modèle et le vectorizer
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Fonction de nettoyage des messages
def clean_text(text):
    text = text.lower()
    text = re.sub(f"[{string.punctuation}]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

# Fonction de détection de phishing
def is_phishing(text):
    cleaned_text = clean_text(text)
    vectorized_text = vectorizer.transform([cleaned_text])
    prediction = model.predict(vectorized_text)
    return bool(prediction[0])
