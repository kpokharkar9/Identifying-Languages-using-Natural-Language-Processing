import joblib
import os
import re
import string
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to preprocess text data
def preprocess_text(line):
    if len(line) != 0:
        line = line.lower()
        line = re.sub(r"\d+", "", line)
        line = line.translate(str.maketrans('', '', string.punctuation))
    return line

# Load the detection model once
detection_model_path = 'translation_app/models/detection_model/mnb_model_compressed.joblib'
pipe_mnb = joblib.load(detection_model_path)

# Dictionary to map language names to language codes
language_mapping = {
    "English": "en",
    "Bulgarian": "bg",
    "Czech": "cs",
    "Danish": "da",
    "German": "de",
    "Spanish": "es",
    "Finnish": "fi",
    "French": "fr",
    "Hungarian": "hu",
    "Italian": "it",
    "Dutch": "nl",
    "Romanian": "ro",
    "Slovenian": "sl",
    "Swedish": "sv",
    "Portuguese": "pt",
    "Swedish": "sv" 
}

# Set of unsupported languages for local models
unsupported_languages = {"lv", "sl", "ro", "pt"}

# Function to detect language
def detect_language(text):
    preprocessed_text = preprocess_text(text)
    detected_language_name = pipe_mnb.predict([preprocessed_text])[0]
    return language_mapping.get(detected_language_name)

# Function to load a translation model
def load_model(src_lang, tgt_lang):
    if src_lang == "en":
        model_dir = f"translation_app/models/translation_model/{tgt_lang}/{src_lang}-{tgt_lang}"
    else:
        model_dir = f"translation_app/models/translation_model/{src_lang}/{src_lang}-{tgt_lang}"
    tokenizer_path = os.path.join(model_dir, 'tokenizer.joblib')
    model_path = os.path.join(model_dir, 'model.joblib')
    tokenizer = joblib.load(tokenizer_path)
    model = joblib.load(model_path)
    return tokenizer, model

# Function to perform translation
def translate_text_local(text, src_lang, tgt_lang):
    tokenizer, model = load_model(src_lang, tgt_lang)
    tokenized_text = tokenizer([text], return_tensors="pt", padding=True)
    translated_tokens = model.generate(**tokenized_text)
    translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
    return translated_text

# Function to perform translation using Google Translate API
def translate_text_api(text, target_lang, api_key):
    url = "https://translation.googleapis.com/language/translate/v2"
    params = {
        "q": text,
        "target": target_lang,
        "key": api_key
    }
    response = requests.get(url, params=params)
    return response.json()["data"]["translations"][0]["translatedText"]

# Function to detect source language and translate
def detect_and_translate(text, tgt_lang, api_key):
    src_lang = detect_language(text)
    if src_lang == "en":
        # Directly translate from English to target language
        if tgt_lang in unsupported_languages:
            return translate_text_api(text, tgt_lang, api_key)
        else:
            return translate_text_local(text, src_lang, tgt_lang)
    elif src_lang in unsupported_languages:
        # Use API for unsupported languages
        return translate_text_api(text, tgt_lang, api_key) + " -> " + translate_text_api(text, tgt_lang, api_key)
    else:
        # Translate from source language to English
        text_in_english = translate_text_local(text, src_lang, 'en')
        # Translate from English to target language
        if tgt_lang in unsupported_languages:
            return translate_text_api(text_in_english, tgt_lang, api_key)
        else:
            return translate_text_local(text_in_english, 'en', tgt_lang)