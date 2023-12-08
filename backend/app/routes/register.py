from flask import Flask, jsonify, request, Blueprint
from app.models.direccion import Direccion
from app.models.datos_personales import DatosPersonales
from app.models.paciente import Paciente
from app.models.detalle_historia import DetalleHistorias
from app.models.medico import Medico
from app.models.clinica import Clinica


app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')  

post_bp = Blueprint('post_bp', __name__)

@post_bp.route('/insert_register', methods=['POST'])
def insert_register():
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
    
    paciente_data = data['paciente']
    if paciente_data['paciente']:
        paciente = Paciente(
            datos_personales = datos_personales
        )
        paciente.insert()


    return "Datos insertados correctamente"



@post_bp.route('/insert_triaje', methods=['POST'])
def insert_triaje():
    try:
        data = request.get_json()

        paciente_id = data['datos_personales']['paciente']
        paciente = Paciente.query.get(paciente_id)

        medico_id = data['datos_personales']['medico']
        medico = Medico.query.get(medico_id)

        clinica_id = data['datos_personales']['clinica']
        clinica = Clinica.query.get(clinica_id)

        detalle_historias = DetalleHistorias(
            diagnostico=data['datos_personales']['diagnostico'],
            fecha=data['datos_personales']['fecha'],
            paciente=paciente,
            medico=medico,
            clinica=clinica,
            laboratorio=data['datos_personales']['laboratorio']
        )

        detalle_historias.insert()
        
        return jsonify({"success": True}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
