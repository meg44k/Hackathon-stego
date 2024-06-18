import os
from dotenv import load_dotenv

load_dotenv()

class SystemConfig:

  DEBUG = True

  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
      'user': os.getenv('DB_USER'),
      'password': os.getenv('DB_PASSWORD'),
      'host': 'localhost',
      'db_name': 'flaschcard_db'
  })

Config = SystemConfig