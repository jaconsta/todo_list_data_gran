from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class User(db.Document):
    """
    Manages user and their authentication credentials.
    """
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)

    def hash_password(self):
        self.password = generate_password_hash(self.password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
#https://runningcodes.net/flask-login-and-mongodb/
