from flask import Flask, jsonify, request, Blueprint
from app.models.direccion import Direccion
from app.models.datos_personales import DatosPersonales

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')  

post_bp = Blueprint('post_bp', __name__)

@post_bp.route('/insert_data', methods=['POST'])
def insert_data():
    data = request.get_json()

    direccion_data = data['direccion']
    direccion = Direccion(
        direccion=direccion_data['direccion'],
        ciudad=direccion_data['ciudad'],
        provincia=direccion_data['provincia'],
        pais=direccion_data['pais']
    )
    direccion.insert()

    datos_personales_data = data['datos_personales']
    datos_personales = DatosPersonales(
        nombres = datos_personales_data['nombres'],
        apellidos = datos_personales_data['apellidos'],
        fecha_nacimiento = datos_personales_data['fecha_nacimiento'],
        ci = datos_personales_data['ci'],
        genero = datos_personales_data['genero'],
        telefono = datos_personales_data['telefono'],
        email = datos_personales_data['email'],
        tipo_sanguineo = datos_personales_data['tipo_sanguineo'],
        direccion = direccion 
    )
    datos_personales.insert()

    return "Datos insertados correctamente"
