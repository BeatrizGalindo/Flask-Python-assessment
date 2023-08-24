from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '1234'
# Initialise the database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# For the passwords not to be stored in the db as password but as hash
bcrypt = Bcrypt(app)

from market import routes