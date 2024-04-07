from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
csrf = CSRFProtect(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
# print(app.config)
migrate = Migrate(app, db)

from app import views