# translation_app/app/routes.py
from flask import request, jsonify
from flask_restful import Resource
from app.translation import detect_and_translate
import logging

logger = logging.getLogger(__name__)

class Translate(Resource):
    def post(self):
        data = request.json
        logger.info("Received translation request")
        
        # Validate input data
        if not data:
            logger.warning("No input data provided")
            return jsonify({"error": "No input data provided"}), 400
        
        text = data.get('text')
        target_lang = data.get('target_lang')
        api_key = data.get('api_key')
        
        if not text or not target_lang or not api_key:
            logger.warning("Missing required parameters")
            return jsonify({"error": "Missing required parameters"}), 400
        
        try:
            translated_text = detect_and_translate(text, target_lang, api_key)
            logger.info("Translation successful")
            return jsonify({'translated_text': translated_text})
        except ValueError as ve:
            # Handle specific known errors
            logger.error(f"ValueError: {str(ve)}")
            return jsonify({"error": str(ve)}), 400
        except Exception as e:
            # Handle general errors
            logger.error(f"Exception: {str(e)}")
            return jsonify({"error": "An error occurred during translation"}), 500

def setup_routes(api):
    api.add_resource(Translate, '/translate')

