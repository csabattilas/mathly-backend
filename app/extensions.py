import os
from flask_sqlalchemy import SQLAlchemy
from firebase_admin import credentials, initialize_app
from dotenv import load_dotenv

db = SQLAlchemy()
firebase_app = None

def init_firebase():
    global firebase_app
    if not firebase_app:
        # Load environment variables if not already loaded
        load_dotenv()
        
        # Get the path from environment variable or use a default path
        firebase_creds_path = os.getenv('FIREBASE_SERVICE_ACCOUNT_PATH')
        
        if firebase_creds_path and os.path.exists(firebase_creds_path):
            cred = credentials.Certificate(firebase_creds_path)
            firebase_app = initialize_app(cred)
        else:
            print("Warning: Firebase credentials file not found. Firebase authentication will not work.")
            # Initialize Firebase with None to avoid errors in development
            firebase_app = initialize_app(None)