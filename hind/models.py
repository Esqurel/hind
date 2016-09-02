from datetime import datetime
from uuid import uuid4

from hind import db


def association_table_factory(*table_names):
    columns = []
    for table_name in table_names:
        name = table_name + '_id'
        foreign_key = table_name + '.id'
        columns.append(db.Column(name, db.String, db.ForeignKey(foreign_key)))
    table = db.Table('_to_'.join(table_names), *columns)
    return table


users_roles = association_table_factory('user', 'role')
elements_tags = association_table_factory('element', 'tag')


class User(db.Model):
    id = db.Column(db.String, primary_key=True, default=uuid4().hex)
    authenticated = db.Column(db.Boolean, nullable=False, default=False)
    banned = db.Column(db.Boolean, nullable=False, default=False)
    email = db.Column(db.String, unique=True)
    last_login_at = db.Column(db.DateTime, nullable=False, default=datetime.min)
    locale = db.Column(db.String, nullable=False, default='en-US')
    login_count = db.Column(db.Integer, nullable=False, default=0)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    session_token = db.Column(db.String)
    timezone = db.Column(db.String, nullable=False, default='UTC')
    verified = db.Column(db.Boolean, nullable=False, default=False)

    roles = db.relationship('Role', secondary=users_roles, backref='users')

    @property
    def is_active(self):
        return self.verified and not self.banned

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return self.authenticated

    @property
    def password(self):
        return self.password
    @password.setter
    def password(self, password):
        pass

    def get_id(self):
        return self.id

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User {!s}>'.format(self.id)


class Role(db.Model):
    id = db.Column(db.String, primary_key=True, default=uuid4().hex)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String)


class Element(db.Model):
    id = db.Column(db.String, primary_key=True, default=uuid4().hex)
    name = db.Column(db.String, unique=True, nullable=False)
    notes = db.Column(db.String)
    tags = db.relationship('Tag',
                           secondary=elements_tags,
                           backref='elements')
    citations = db.relationship('Citation', backref='element')


class Category(db.Model):
    id = db.Column(db.String, primary_key=True, default=uuid4().hex)
    name = db.Column(db.String, unique=True)
    tags = db.relationship('Tag', backref='category')


class Tag(db.Model):
    id = db.Column(db.String, primary_key=True, default=uuid4().hex)
    name = db.Column(db.String, unique=True)
    category_id = db.Column(db.String, db.ForeignKey('category.id'))


class Citation(db.Model):
    id = db.Column(db.String, primary_key=True, default=uuid4().hex)
    element_id = db.Column(db.String, db.ForeignKey('element.id'))
    source_id = db.Column(db.String, db.ForeignKey('source.id'))
    citation = db.Column(db.String, nullable=False)


class Source(db.Model):
    id = db.Column(db.String, primary_key=True, default=uuid4().hex)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    pub_date = db.Column(db.DateTime)
    link = db.Column(db.String)
    bibliography = db.Column(db.String)
    tag_id = db.Column(db.String, db.ForeignKey('tag.id'))
    citations = db.relationship('Citation', backref='source')

    def __init__(self, title, author=None, pub_date=None, link=None, biblio=None):
        self.title = title
        self.author = author or 'Anonymous'
        self.pub_date = pub_date or datetime.date.min
        self.link = link
        self.bibliography = biblio