from flask import Flask, jsonify, request, Blueprint
from app.database.database import connect_to_database

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')  

main_bp = Blueprint('main', __name__)

@main_bp.route('/get_patient', methods=['GET'])
def obtener_paciente():
    paciente_id = request.args.get('card_id')
    
    try:
        with connect_to_database().cursor() as cursor:
            cursor.execute("""SELECT PD.NAME AS DOCTOR_NAME, PD.LAST_NAME AS DOCTOR_LAST_NAME, D.SPECIALITY, D.REGISTER
FROM DOCTORS D
JOIN PERSONS P ON D.PERSON_ID = P.ID
JOIN PERSONAL_DATA PD ON P.PERSONAL_DATA_ID = PD.ID
WHERE PD.CARD_ID = :id """, id=paciente_id)
            data = cursor.fetchone()

            if data:
                column_names = [desc[0] for desc in cursor.description]
                paciente_dict = dict(zip(column_names, data))
                return jsonify(paciente_dict)
            else:
                return jsonify({'error': 'Paciente no encontrado'})
    except Exception as e:
        return jsonify({'error': f'Error: {str(e)}'})
