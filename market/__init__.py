from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '1234'
# Initialise the database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# For the passwords not to be stored in the db as password but as hash
bcrypt = Bcrypt(app)

# For login the user
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

# Adding record to database
seeder = FlaskSeeder()
seeder.init_app(app, db)


import market.routes
