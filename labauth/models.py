import string
import random
from hashlib import sha256

from labauth import db

class Human(db.Model):
    __tablename__ = 'human'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String())
    token_hash = db.Column(db.String())

    @classmethod
    def create_user(cls, username, email):
        """
        create user, return tuple of User object and token in cleartext
        """
        token = ""
        token_chars = string.ascii_letters + string.digits
        for i in range(64):
            token.append(random.choice(token_chars))

        user_obj = cls(username, email, token)
        
        return user_obj, token
        
class Machine(db.Model):
    __tablename__ = 'machine'
    id = db.Column(db.Integer(), primary_key=True)
    token_hash = db.Column(db.String())
    comment = db.Column(db.String())
    
    @classmethod
    def create_user(cls, username, email):
        """
        create user, return tuple of User object and token in cleartext
        """
        token = ""
        token_chars = string.ascii_letters + string.digits
        for i in range(64):
            token.append(random.choice(token_chars))

        user_obj = cls(comment)
