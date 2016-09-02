from passlib.context import CryptContext

from hind import app


pwd_context = CryptContext(**app.config['PASSLIB'])