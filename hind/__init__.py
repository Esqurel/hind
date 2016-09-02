from flask import Flask
from flask_babel import Babel
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from hind.config import config


app = Flask(__name__)
app.config.update(config)

babel = Babel(app)
db = SQLAlchemy(app)
lm = LoginManager(app)


import hind.models as models
import hind.views as views