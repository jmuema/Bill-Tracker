import os

class Config:
  QUOTES_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
  SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://joseph:25MuemA25@localhost/bills'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SECRET_KEY = 'joseph'
  UPLOADED_PHOTOS_DEST ='app/static/photos'

  #  email configurations
  MAIL_SERVER = 'smtp.gmail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = "pitchymojo@gmail.com"
  MAIL_PASSWORD = "25MuemA25"

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://joseph:25MUemA25@localhost/bills'

class TestConfig(Config):
  pass

class DevConfig(Config):
  DEBUG = True

config_options = {
  'development': DevConfig,
  'production': ProdConfig,
  'test': TestConfig
}