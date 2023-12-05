import os

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'tu_clave_secreta_predeterminada')

    # Configuración de la base de datos SQL Server
    SQL_SERVER_DRIVER = os.environ.get('SQL_SERVER_DRIVER', 'ODBC Driver 17 for SQL Server')
    SQL_SERVER_HOST = os.environ.get('SQL_SERVER_HOST', '104.197.209.110')
    SQL_SERVER_DATABASE = os.environ.get('SQL_SERVER_DATABASE', 'FINALDATABASE')
    SQL_SERVER_USER = os.environ.get('SQL_SERVER_USER', 'sqlserver')
    SQL_SERVER_PASSWORD = os.environ.get('SQL_SERVER_PASSWORD', 'sqlserver')
    
    SQLALCHEMY_DATABASE_URI = (
    f'mssql+pyodbc://{SQL_SERVER_USER}:{SQL_SERVER_PASSWORD}@'
    f'{SQL_SERVER_HOST}/{SQL_SERVER_DATABASE}?'
    f'driver={SQL_SERVER_DRIVER}'
    )
    QLALCHEMY_TRACK_MODIFICATIONS = False 

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig,
}
