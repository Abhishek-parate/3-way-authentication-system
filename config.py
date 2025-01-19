import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "super_secret_key")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///auth.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OTP_EXPIRY_SECONDS = 300  # 5 minutes
