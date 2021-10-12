from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(84), nullable=True)
    email = db.Column(db.String(84), nullable=True, unique=True)
    password = db.Column(db.String(300), nullable=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        print(self.password)
        print(password)
        check = check_password_hash(self.password, password)
        print(check)
        return check

    def __repr__(self):
        return f"<User : {self.username} >"
