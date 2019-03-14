import os


basedir = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY=os.environ['SECRET_KEY']
DB_HOST=os.environ['DB_HOST']
DB_URI = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
APP_NAME=os.environ['APP_NAME']


# Settings for MySQL
#DB_USERNAME=os.environ['DB_USERNAME']
#DB_PASSWORD=os.environ['DB_PASSWORD']
#DATABASE_NAME=os.environ['DATABASE_NAME']
#DB_URI = "mysql+pymysql://%s:%s@%s:3306/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, DATABASE_NAME)
#MYSQL_ROOT_PASSWORD=os.environ['MYSQL_ROOT_PASSWORD']