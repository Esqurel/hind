import json
from os import path


basedir = path.join(path.abspath(path.dirname(__file__)), '..')
db_path = path.join(basedir, 'data', 'hind.db')
database_uri = 'sqlite:////' + db_path

with open(path.join(basedir, 'config.json'), 'r') as config_file:
    config = json.load(config_file)

config['SQLALCHEMY_DATABASE_URI'] = database_uri