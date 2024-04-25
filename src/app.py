"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Usuario, Personajes, Planetas, PlanetasFavoritos, PersonajesFavoritos
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

    # Endpoint para obtener todos los personajes
@app.route('/people', methods=['GET'])
def get_people():

    # this is how you can use the Family datastructure by calling its methods
    personajes = Personajes.query.all()
    lista_personajes = list(map(lambda item: item.serialize(), personajes))

    if lista_personajes == []:
        return jsonify({"msg": "No existen personajes"}), 404

    response_body = { 
        "results": lista_personajes
    }

    return jsonify(response_body), 200

    # Endpoint para obtener uno los personajes
@app.route('/people/<int:people_id>', methods=['GET'])
def get_one_people(people_id):

    # this is how you can use the Family datastructure by calling its methods
    one_people = Personajes.query.filter_by(id= people_id).first()
    
    if one_people == None:
        return jsonify({"msg": "No existe el personaje"}), 404

    response_body = {
        "result": one_people.serialize() 
    }

    return jsonify(response_body), 200

# Endpoint para obtener todos los planetas

@app.route('/planets', methods=['GET'])
def get_planets():

    # this is how you can use the Family datastructure by calling its methods
    planetas = Planetas.query.all()
    lista_planetas = list(map(lambda item: item.serialize(), planetas))
    
    if lista_planetas == []:
        return jsonify({"msg": "No existen planetas"}), 404

    response_body = {
        "results": lista_planetas
    }

    return jsonify(response_body), 200

    # Endpoint para obtener un planeta
@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_one_planet(planet_id):

    # this is how you can use the Family datastructure by calling its methods
    one_planet = Planetas.query.filter_by(id= planet_id).first()
    
    if one_planet == None:
        return jsonify({"msg": "No existe el planeta"}), 404

    response_body = {
        "result": one_planet.serialize() 
    }

    return jsonify(response_body), 200

    # Endpoint para obtener todos los usuarios
@app.route('/users', methods=['GET'])
def get_users():

    # this is how you can use the Family datastructure by calling its methods
    usuarios = Usuario.query.all()
    lista_usuarios = list(map(lambda item: item.serialize(), usuarios))

    if lista_usuarios == []:
        return jsonify({"msg": "No existen usuarios"}), 404

    response_body = { 
        "results": lista_usuarios
    }

    return jsonify(response_body), 200

    # Endpoint para obtener todos los favoritos del usuario
@app.route('/users/favorites', methods=['GET'])
def get_favorites_user():

    # this is how you can use the Family datastructure by calling its methods
    favoritos_usuario = PersonajesFavoritos.query.all()
    lista_favoritos_usuarios = list(map(lambda item: item.serialize(), favoritos_usuario))

    if lista_favoritos_usuarios == []:
        return jsonify({"msg": "No existen favoritos"}), 404

    response_body = { 
        "results": lista_favoritos_usuarios
    }

    return jsonify(response_body), 200



# --------------------------------------------------------------

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
