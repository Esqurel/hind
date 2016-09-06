from flask_principal import Permission, RoleNeed
from passlib.context import CryptContext

from hind import app, db
from hind.models import User


pwd_context = CryptContext(**app.config['PASSLIB'])

admin_permission = Permission(RoleNeed('admin'))
edit_permission = Permission(RoleNeed('edit'))


def attempt_login(name, pwd):
    pass