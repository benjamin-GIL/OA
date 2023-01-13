from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

@dataclass
class User(db.Model):
    __tablename__ = 'user'

    __table_args__ = {'schema': 'public'}

    user_id: int = db.Column(db.Integer, primary_key=True)
    email: str = db.Column(db.String())
    phone_number: int = db.Column(db.Integer())
    name: str = db.Column(db.String())
    last_name: str = db.Column(db.String())
    birthday: str = db.Column(db.Date()) 
    gender: str = db.Column(db.String())
    document:int = db.Column(db.Integer())
    document_type: str = db.Column(db.String())
    account_type: str = db.Column(db.String())
    account_number: int = db.Column(db.Integer())

    def __init__(self,user_id, email, phone_number, name, last_name, birthday, gender, document, document_type, account_type, account_number):
        self.user_id = user_id
        self.email = email
        self.phone_number = phone_number
        self.name = name
        self.last_name = last_name
        self.birthday = birthday
        self.gender = gender
        self.document = document
        self.document_type = document_type
        self.account_type = account_type
        self.account_number = account_number    
    def __repr__(self):
        return f"<id {self.user_id}, name {self.email},date {self.phone_number}>"
