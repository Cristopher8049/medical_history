import pyodbc
from flask import current_app

def connect_to_database():
    try:
        connection = pyodbc.connect(
            f'DRIVER={current_app.config["SQL_SERVER_DRIVER"]};'
            f'SERVER={current_app.config["SQL_SERVER_HOST"]};'
            f'DATABASE={current_app.config["SQL_SERVER_DATABASE"]};'
            f'UID={current_app.config["SQL_SERVER_USER"]};'
            f'PWD={current_app.config["SQL_SERVER_PASSWORD"]};'
        )
        print("Conexión exitosa a la base de datos.")
        return connection
    except Exception as e:
        print(f'Error al conectar a la base de datos: {str(e)}')
        raise