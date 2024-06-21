from app.routes import setup_routes
import logging
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

app = Flask(__name__)
CORS(app)

api = Api(app)
setup_routes(api)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info("Starting Flask application")
    app.run(debug=True)
