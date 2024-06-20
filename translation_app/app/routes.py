# translation_app/app/routes.py
from flask import request, jsonify
from flask_restful import Resource
from app.translation import detect_and_translate

class Translate(Resource):
    def post(self):
        data = request.json
        if not data:
            return jsonify({"error": "No input data provided"}), 400
        
        text = data.get('text')
        target_lang = data.get('target_lang')
        api_key = data.get('api_key')
        
        if not text or not target_lang or not api_key:
            return jsonify({"error": "Missing required parameters"}), 400
        
        try:
            translated_text = detect_and_translate(text, target_lang, api_key)
            return jsonify({'translated_text': translated_text})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

def setup_routes(api):
    api.add_resource(Translate, '/translate')
