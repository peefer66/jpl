import os

basedir = os.path.abspath(os.path.dirname(__file__))
#app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///'+os.path.join(basedir,'data.sqlite')

SECRET_KEY=os.environ['SECRET_KEY']
#DB_USERNAME=os.environ['DB_USERNAME']
#DB_PASSWORD=os.environ['DB_PASSWORD']
DB_HOST=os.environ['DB_HOST']
#DATABASE_NAME=os.environ['DATABASE_NAME']
DB_URI = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
#DB_URI = "mysql+pymysql://%s:%s@%s:3306/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
#MYSQL_ROOT_PASSWORD=os.environ['MYSQL_ROOT_PASSWORD']
APP_NAME=os.environ['APP_NAME']
