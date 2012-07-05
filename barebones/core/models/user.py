from sqlalchemy import Integer, String, Boolean
from barebones.database import db
import hashlib


class User(db.Model):
    __tablename__ = 'users'
    userid = db.Column('userid', Integer, primary_key=True)
    username = db.Column('username', String(50), unique=True)
    _password = db.Column('password', String(50), nullable=False)
    admin = db.Column('admin', Boolean)

    def __init__(self, username, password, admin=False):
        self.username = username
        # this salting routine is terrible. find a better one
        salt = self.username + '$4lt'
        self.password = password + salt
        self.admin = admin

    def __repr__(self):
        return self.username

    def _get_password(self):
        return self._password

    def _set_password(self, password):
        self._password = hashlib.sha256(password).hexdigest()

    password = db.synonym("_password", descriptor=property(_get_password, _set_password))

    def hashpassword(self, password, salt):
        return hashlib.sha256(password + salt).hexdigest()

    def checkpassword(self, password):
        salt = self.username + '$4lt'
        return self.hashpassword(password, salt) == self.password
