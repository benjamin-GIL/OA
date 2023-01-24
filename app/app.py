from flask import Flask, jsonify, request
from models import db, User, BankInfo, Bank  

import config


app = Flask(__name__)
env_config = config.Config
app.config.from_object(env_config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
app.config['JSON_AS_ASCII'] = False


@app.route("/")
def hi():
    return "hola gualter blanco"


@app.route("/users", methods=['GET'])
def user():
    users = User.query.all()
    return jsonify(users)


@app.route("/users/<int:document_number>")
def user_document(document_number):
    user = User.query.filter_by(document_number=document_number).first()
    return jsonify(user)


@app.route("/users/<int:document_number>/banking-info")
def bankinfo(document_number):
    bank_info = User.query.filter_by(document_number=document_number).first().banking_info
    return jsonify(bank_info)


@app.route("/users", methods=['POST'])
def create_user():
    response = +1
    return jsonify(response)


@app.route("/users", methods=['DELETE'])
def delete_user():
    response = {'message: success'}
    return jsonify(response)


@app.route("/banks", methods=['GET'])
def get_banks():
    banks = Bank.query.all()
    return jsonify(banks)


@app.route("/banks/<string:name>", methods=['GET'])
def get_bank_by_name(name):
    # pdb.set_trace()
    clean_name = name.replace("-", " ")
    banks = Bank.query.filter_by(name=clean_name).first()
    return jsonify(banks)


@app.route("/banks/", methods=['POST'])
def post_bank():
    #primero: recibo el request y extraigo la informacion que necesito de ahi
    req = request.json
    #segundo: inicializo un objeto de la clase Bank con la informacion que extraje anteriormente 
    new_bank = Bank(name=req.get("name"))
    #tercero: le paso el objeto Bank a la sesion para que lo agrege y haga el commit 
    db.session.add(new_bank)
    db.session.commit()
    #cuarto: devuelvo como json el objeto creado 
    return jsonify(new_bank)

@app.route("/banks", methods=['DELETE'])
def delete_bank():
    banks = Bank.query.all()
    return jsonify(banks)


@app.route("/banks", methods=['PUT'])
def edit_bank():
    banks = Bank.query.all()
    return jsonify(banks)


if __name__ == '__main__':
    app.run(debug=True)
