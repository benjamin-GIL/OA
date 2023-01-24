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
    gender_id: str = db.Column(db.String())
    document_number: int = db.Column(db.Integer())
    document_type_id: str = db.Column(db.String())


    def __init__(self, user_id, email, phone_number, name, last_name, birthday, gender_id, document_number, document_type_id, account_type, account_number):
        self.user_id = user_id
        self.email = email
        self.phone_number = phone_number
        self.name = name
        self.last_name = last_name
        self.birthday = birthday
        self.gender_id = gender_id
        self.document_number = document_number
        self.document_type_id = document_type_id

    def __repr__(self):
        return f"<id {self.user_id}, name {self.name},date {self.last_name}>"


@dataclass
class Gender(db.Model):
    __tablename__ = 'gender'
    
    id: int = db.Column(db.Integer, primary_key=True)
    identity: str = db.Column(db.String())

    def __init__(self, id, identity):
        self.id = id
        self.identity = identity
    
    def __repr__(self):
        return f"<id{self.id}, identity{self.identity}>"


@dataclass
class DocumentType(db.Model):
    __tablename__ = 'document_type'
    
    id: int = db.Column(db.Integer, primary_key=True)
    short_name: str = db.Column(db.String())
    name: str = db.Column(db.String())

    def __init__(self, id, short_name, name):
        self.id = id
        self.short_name = short_name
        self.name = name 
    
    def __repr__(self):
        return f"<id{self.id}, identity{self.identity}>"

@dataclass
class ContactInfo(db.Model):
    __tablename__ = 'contact_info'

    id: int = db.Column(db.Integer, primary_key=True)
    user_id: int = db.Column(db.ForeignKey("user.user_id"))
    email: str = db.Column(db.String)
    phone_number: int = db.Column(db.Integer())

    def __init__(self, id, user_id, email, phone_number):
        
        self.id = id
        self.user_id = user_id
        self.email = email
        self.phone_number = phone_number
    
    def __repr__(self):
        return f"<id{self.id}, user_id{self.user_id}, email{self.email}, phone_number{self.phone_number}>"


@dataclass
class BankInfo(db.Model):

    __tablename__ = 'banking_info'

    id: int = db.Column(db.Integer, primary_key=True)
    bank_id: int = db.Column(db.ForeignKey("bank_id.id"))
    account_type_id: int = db.Column(db.ForeignKey("account_type.id"))
    account_number: int = db.Column(db.Integer())
    user_id: int = db.Column(db.Integer, db.ForeignKey("user.user_id"))

    def __init__(self, id, bank_id, account_type_id, account_number, user_id):
        self.id = id
        self.user_id = user_id
        self.bank_id = bank_id
        self.account_type_id = account_type_id
        self.account_number = account_number

    def __repr__(self):
        return f"<id {self.id}, user_id{self.user_id}, bank_id{self.bank_id}>"



@dataclass 
class Bank(db.Model):

    __tablename__ = "bank_id"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String())
    
    def __init__(self, name):
        self.name = name 

    def __repr__(self):
        return f"<id{self.id}, name{self.name}>"


@dataclass 
class AccountType(db.Model):
    __tablename__ = "account_type"

    id: int = db.Column(db.Integer, primary_key=True)
    type: str = db.Column(db.String())

    def __init__(self, id, type):
        self.id = id
        self.type = type

    def __repr__(self):
        return f"<id {self.user_id}, name {self.email},date {self.phone_number}>"
