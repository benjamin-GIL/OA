from flask import Flask ,jsonify
from models import db ,User
import config

app = Flask(__name__)
env_config = config.Config
app.config.from_object(env_config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route("/users")
def user():
    users = User.query.all()
    return jsonify(users)

@app.route("/")
def hi():
    return "hola gualter blanco"

if __name__ == '__main__':
    app.run()
