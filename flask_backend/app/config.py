import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'mysql+pymysql://tishere_dev:tishere_pwd@localhost/tishere'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY') or 'jwt-secret-string'
