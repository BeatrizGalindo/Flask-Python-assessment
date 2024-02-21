from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa
import os
import logging
from logging.handlers import RotatingFileHandler
from flask.logging import default_handler

BASEDIR = os.path.abspath(os.path.dirname(__file__))


if os.getenv('DATABASE_URL'):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL').replace("postgres://", "postgresql://", 1)
else:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///market.db'



app = Flask(__name__)


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

app.config['SECRET_KEY'] = '1234'
# Initialise the database
db = SQLAlchemy(app)
migrate = Migrate(app, db)



# Check if the database needs to be initialized
engine = sa.create_engine(app.config['SQLALCHEMY_DATABASE_URI'], pool_pre_ping=True)
inspector = sa.inspect(engine)
if not inspector.has_table("user"):
    # attention
    with app.app_context():
        db.drop_all()
        db.create_all()
        app.logger.info('Initialized the database!')
else:
    app.logger.info('Database already contains the users table.')



# For the passwords not to be stored in the db as password but as hash
bcrypt = Bcrypt(app)

# For login the user
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

# Adding record to database
seeder = FlaskSeeder()
seeder.init_app(app, db)


LOG_WITH_GUNICORN = os.getenv('LOG_WITH_GUNICORN', default=False)


def configure_logging(app):
    # Logging Configuration
    if LOG_WITH_GUNICORN:
        gunicorn_error_logger = logging.getLogger('gunicorn.error')
        app.logger.handlers.extend(gunicorn_error_logger.handlers)
        app.logger.setLevel(logging.DEBUG)
    else:
        file_handler = RotatingFileHandler('instance/flask-user-management.log',
                                           maxBytes=16384,
                                           backupCount=20)
        file_formatter = logging.Formatter('%(asctime)s %(levelname)s %(threadName)s-%(thread)d: %(message)s [in %(filename)s:%(lineno)d]')
        file_handler.setFormatter(file_formatter)
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

    # Remove the default logger configured by Flask
    app.logger.removeHandler(default_handler)

    app.logger.info('Starting the Flask User Management App...')


configure_logging(app)



import market.routes
