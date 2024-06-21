from app import app
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info("Starting Flask application")
    app.run(debug=True)
