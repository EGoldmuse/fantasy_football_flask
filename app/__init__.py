from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_user import login_required, UserManager, UserMixin, SQLAlchemyAdapter
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment
from flask_mail import Mail
from config import Config
import os


from app.blueprints.api.routes import api
# from app.blueprints.site.routes import site

app = Flask(__name__)

db = SQLAlchemy(app)
db.init_app(app)


migrate = Migrate()
migrate.init_app(app)

login_manager = LoginManager()
moment = Moment()
mail = Mail()


app.config['SECRET_KEY'] = 'thisisascret'
# This is where I put my DB connection
app.config['SQLALCHEMY_DATABASE_URI']
app.config['CSRF_ENABLED'] = True
app.config['USER_ENABLE_EMAIL'] = False

app.register_blueprint(api)

from app.blueprints.authentication import bp as authentication
app.register_blueprint(authentication)

from .import routes

if __name__ == '__main__':
    app.run(debug=True)