from dotenv import load_dotenv
import os

load_dotenv()

DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_PORT = os.environ.get('DB_PORT')
DB_HOST = os.environ.get('DB_HOST')

JWT_SECRET = os.environ.get('JWT_SECRET')
SECRET_VERIF_RESET = os.environ.get('SECRET_VERIF_RESET')
