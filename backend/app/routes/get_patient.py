from flask import Flask, jsonify, request, Blueprint
from app.utils.database import connect_to_database

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')  

get_bp = Blueprint('get_bp', __name__)

@get_bp.route('/get_patient_info', methods=['GET'])
def get_patient_info():
    paciente_id = request.args.get('card_id')
    
    try:
        
        connection = connect_to_database()
        cursor = connection.cursor()
        query = f"SELECT * FROM DATOS_PERSONALES WHERE CI = '{paciente_id}'"
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

@get_bp.route('/get_patient_histo', methods=['GET'])
def get_patient_histo():
    ci = request.args.get('card_id') 

    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        query =  f"""
        SELECT DH.DIAGNOSTICO, DH.FECHA, DH.ID_MEDICO, DH.ID_CLINICA, DH.LABORATORIO,
        DP_MEDICO.NOMBRES AS NOMBRE_MEDICO, DP_MEDICO.APELLIDOS AS APELLIDO_MEDICO
        FROM DETALLE_HISTORIAS DH
        LEFT JOIN PACIENTE P ON DH.ID_PACIENTE = P.ID
        LEFT JOIN DATOS_PERSONALES DP_PACIENTE ON P.ID_DATOS_PERSONALES = DP_PACIENTE.ID
        LEFT JOIN MEDICO M ON DH.ID_MEDICO = M.ID
        LEFT JOIN DATOS_PERSONALES DP_MEDICO ON M.ID_DATOS_PERSONALES = DP_MEDICO.ID
        WHERE DP_PACIENTE.CI = '{ci}';"""
        
        cursor.execute(query)
        data = cursor.fetchall()

        if data:
            result = []
            for row in data:
                column_names = [desc[0] for desc in cursor.description]
                paciente_dict = dict(zip(column_names, row))
                result.append(paciente_dict)
            
            return jsonify(result)
        else:
            return jsonify({'error': 'Paciente no encontrado'})
    except Exception as e:
        return jsonify({'error': f'Error: {str(e)}'})
