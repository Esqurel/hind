from flask import request
from flask_login import current_user

from hind import app, babel


@babel.localeselector
def get_locale():
    locale = current_user.locale
    if not locale:
        languages = app.config['LANGUAGES'].keys()
        locale = request.accept_languages.best_match(languages)
    return locale

@babel.timezoneselector
def get_timezone():
    return current_user.timezone