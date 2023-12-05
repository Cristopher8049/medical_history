from flask import Flask, jsonify, request, Blueprint
from app.utils.database import connect_to_database

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')  

get_bp = Blueprint('get_bp', __name__)

@get_bp.route('/get_patient', methods=['GET'])
def get_patient():
    paciente_id = request.args.get('card_id')
    
    try:
        
        connection = connect_to_database()
        cursor = connection.cursor()
        query = f"SELECT * FROM DATOS_PERSONALES WHERE ID = '{paciente_id}'"
        cursor.execute(query)
        data = cursor.fetchone()
        if data:
            column_names = [desc[0] for desc in cursor.description]
            paciente_dict = dict(zip(column_names, data))
            return jsonify(paciente_dict)
        else:
            return jsonify({'error': 'Paciente no encontrado'})
    except Exception as e:
        return jsonify({'error': f'Error: {str(e)}'})

