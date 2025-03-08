import os
from flask import Flask
from models import db  # Removed Teacher import since it's no longer needed
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

app = Flask(__name__)

# Load environment variables
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', 'False') == 'True'

# Initialize database and bcrypt
db.init_app(app)
bcrypt = Bcrypt(app)

from routes import *  # Ensure this is correct and routes are properly defined

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
