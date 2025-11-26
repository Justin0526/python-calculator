import os

API_KEY = os.getenv('API_KEY', 'default-key-for-local-testing')
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///local.db')
DEBUG_MODE = os.getenv('DEBUG_MODE', 'true').lower() == 'true'