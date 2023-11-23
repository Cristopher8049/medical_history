import oracledb
from flask import current_app

def connect_to_database():
    try:
        connection = oracledb.connect(
            user=current_app.config['ORACLE_USER'],
            password=current_app.config['ORACLE_PASSWORD'],
            dsn=current_app.config['ORACLE_DSN']
        )
        print("Conexión exitosa a la base de datos.")
        return connection
    except Exception as e:
        print(f'Error al conectar a la base de datos: {str(e)}')
        raise
