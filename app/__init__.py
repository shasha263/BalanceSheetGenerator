from flask import Flask
from config import Config
from .auth.routes import auth
from .financialstmt.routes import financialstmt

from .models import db,login
from flask_migrate import Migrate, migrate

app=Flask(__name__)
app.register_blueprint(auth)
app.register_blueprint(financialstmt)

app.config.from_object(Config)

db.init_app(app)
migrate=Migrate(app,db)

login.init_app(app)
login.login_view='auth.signin'
login.login_message='Please sign in to see this page'
login.login_message_category='danger'


from . import routes

from . import models

