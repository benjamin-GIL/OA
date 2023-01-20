from flask import Flask ,jsonify
from models import db ,User, BankInfo  
import config

app = Flask(__name__)
env_config = config.Config
app.config.from_object(env_config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route("/")
def hi():
    return "hola gualter blanco"


@app.route("/users", methods = ['GET'])
def user():
    users = User.query.all()
    return jsonify(users)


@app.route("/users", methods = ['POST'])
def create_user():
    response = {'message: success'}
    return jsonify(response)


@app.route("/users/<int:document_number>")
def user_document(document_number):
    user = User.query.filter_by(document_number=document_number).first()
    return jsonify(user)


@app.route("/users/<int:document_number>/banking-info")
def bankinfo(document_number):
    #import pdb; pdb.set_trace()
    bank_info = User.query.filter_by(document_number=document_number).first().banking_info
    return jsonify(bank_info)


if __name__ == '__main__':
    app.run()
