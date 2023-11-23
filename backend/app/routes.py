from flask import current_app as app
import oracledb
from config import Config

@app.route("/")
def home():
    connection = oracledb.connect(user=app.config['ORACLE_USER'], password=app.config['ORACLE_PASSWORD'], dsn=app.config['ORACLE_DSN'])
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM PACIENTES")

    data = []

    for row in cursor:
        data.append(row)

    cursor.close()
    connection.close()

    return f'Data from Oracle: {data}'
