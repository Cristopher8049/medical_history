from flask import Flask, jsonify, request, Blueprint
from app.utils.database import connect_to_database

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')  

post_bp = Blueprint('post_bp', __name__)

@post_bp.route('/insert_data', methods=['POST'])
def insert_data():
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        sql_insert = "INSERT INTO PACIENTE (ID, ID_DATOS_PERSONALES) VALUES (?, ?)"
        data_to_insert = (request.json.get('valor1'), request.json.get('valor2'))
        cursor.execute(sql_insert, data_to_insert)
        connection.commit()
        connection.close()
        return jsonify({'message': 'Inserción exitosa'}), 201
    except Exception as e:
        return jsonify({'error': f'Error al realizar la inserción: {str(e)}'}), 500 

