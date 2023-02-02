from flask import Flask, jsonify, request, abort
from models import db, User, BankingInfo, Bank, ContactInfo 

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


@app.route("/users/<int:document_number>", methods=['GET'])
def user_document(document_number):
    user = User.query.filter_by(document_number=document_number).first()
    return jsonify(user)


@app.route("/users", methods=['POST'])
def create_user():

    data = request.json
    data_doc = data.get("document_number")
    filter_user = User.query.filter_by(document_number=data_doc).first()

    if filter_user is None:
        new_user = User(
            name=data.get("name"), last_name=data.get("last_name"),
            birthday=data.get("birthday"), gender_id=data.get("gender_id"),
            document_number=data.get("document_number"),
            document_type_id=data.get("document_type_id")
        )
        db.session.add(new_user)
        db.session.commit()
    else:
        return abort(500, description="error trying to create user")
    return jsonify(new_user)


@app.route("/users/<int:document_number>", methods=['DELETE'])
def delete_user(document_number):
    delete_user = User.query.filter_by(document_number=document_number).first()
    db.session.delete(delete_user)
    db.session.commit()
    return "", 204

@app.route("/users/<int:document_number>", methods=['PUT'])
def edit_user(document_number):

    edited_user = User.query.filter_by(document_number=document_number).first()

    data = request.json
    data_keys = data.keys()
    for x in data_keys:
        if x == "document_number":
            continue
        if hasattr(edited_user, x):
            setattr(edited_user, x, data.get(x))
    db.session.commit()
    return jsonify(edited_user)

# ___________________________________________________________________________ 


@app.route("/banks", methods=['GET'])
def get_banks():
    banks = Bank.query.all()
    return jsonify(banks)


@app.route("/banks/<string:name>", methods=['GET'])
def get_bank_by_name(name):
    clean_name = name.replace("-", " ")
    banks = Bank.query.filter_by(name=clean_name).first()
    return jsonify(banks)


@app.route("/banks", methods=['POST'])
def post_bank():
    # primero: recibo el request y extraigo la informacion que necesito de ahi
    req = request.json
    # segundo: inicializo un objeto de la clase Bank con la informacion que extraje anteriormente 
    new_bank = Bank(name=req.get("name"))
    # tercero: le paso el objeto Bank a la sesion para que lo agrege y haga el commit 
    db.session.add(new_bank)
    db.session.commit()
    # cuarto: devuelvo como json el objeto creado 
    return jsonify(new_bank)


@app.route("/banks", methods=['DELETE'])
def delete_bank():
    # 1: se recibe el request y se extrae la informacion 
    rqst = request.json
    # 2: se inicializa el objeto contactcon un query Bank  y se filtra con la informacion anterior 
    delete_banks = Bank.query.filter(Bank.name == rqst.get("name")).first()
    # 3: se pasa el objeto bank, se añade a la sesion y se hace el commit  
    db.session.delete(delete_banks)
    db.session.commit()
    # 4: devuelvo objeto creado como json
    return jsonify(delete_banks)


@app.route("/banks", methods=['PUT'])
def edit_bank():
    # se recibe un request y extraigo el ID
    id = request.json.get("id")  
    # segundo se hace un query a la base de datos filtrando por el el anterior id y se obtiene la instancia de Bank 
    bank = Bank.query.filter_by(id=id).first()
    # tercero extraigo el resto de informacion que viene en el request
    data = request.json
    data_keys = data.keys()
    for x in data_keys:
        if x == "id":
            continue
        if hasattr(bank, x):
            setattr(bank, x, data.get(x))
    # cuarto tomo la informacion que extraje en el anterior paso y actualizo los valores correspondientes en la instancia de Bank
    # quinto hago el commit
    db.session.commit()
    # sexto devuelto el json del objeto Bank
    return jsonify({"messenge":"success"})

# ___________________________________________________________________________ 

@app.route("/users/<int:document_number>/contact-info", methods=['GET'])
def contact_info(document_number):
    user_contact_info = User.query.filter_by(document_number=document_number).first().contact_info
    return jsonify(user_contact_info)


@app.route("/users/<int:document_number>/contact-info", methods=['POST'])
def create_contact_info(document_number):
    data = request.json
    get_user = User.query.filter_by(document_number=document_number).first()
    id = get_user.user_id
    user_contact_info = ContactInfo.query.filter_by(user_id=id).first()

    if user_contact_info is None:
        new_contact_info = ContactInfo(
            user_id=data.get("user_id"), email=data.get("email"),
            phone_number=data.get("phone_number")
        )
        db.session.add(new_contact_info)
        db.session.commit()
    else:
        return abort(501, description="error trying to create User contact info")
    return jsonify(new_contact_info)


@app.route("/users/<int:document_number>/contact-info", methods=['DELETE'])
def delete_contact_info(document_number):
    get_user = User.query.filter_by(document_number=document_number).first()
    id = get_user.user_id
    delete_user_contact_info = ContactInfo.query.filter_by(user_id=id).first()
    db.session.delete(delete_user_contact_info)
    db.session.commit()
    return "", 204


@app.route("/users/<int:document_number>/contact-info", methods=['PUT'])
def edit_contact_info(document_number):
    get_user = User.query.filter_by(document_number=document_number).first()
    id = get_user.user_id
    edited_contact_info = ContactInfo.query.filter_by(user_id=id).first()

    data = request.json
    data_keys = data.keys()
    for x in data_keys:
        if x == "user_id":
            continue
        if hasattr(edited_contact_info, x):
            setattr(edited_contact_info, x, data.get(x))
    db.session.commit()
    return jsonify(edited_contact_info)

# ____________________________________________________________________________


@app.route("/users/<int:document_number>/banking-info", methods=['GET'])
def bank_info(document_number):
    bank_info = User.query.filter_by(document_number=document_number).first().banking_info
    return jsonify(bank_info)



if __name__ == '__main__':
    app.run(debug=True)
