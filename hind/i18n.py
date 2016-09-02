from flask_login import current_user

from hind import babel


@babel.localeselector
def test():
    return current_user.get('locale', None)

@babel.timezoneselector
def test1():pass