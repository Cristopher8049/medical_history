import os

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'tu_clave_secreta_predeterminada')

    # Configuración de la base de datos Oracle
    ORACLE_USER = os.environ.get('ORACLE_USER', 'admin')
    ORACLE_PASSWORD = os.environ.get('ORACLE_PASSWORD', 'Admin1234!')
    ORACLE_DSN = os.environ.get('ORACLE_DSN', 'final.cyuc5g3vj9ns.us-east-1.rds.amazonaws.com/orcl')


class DevelopmentConfig(Config):
    DEBUG = False

class TestingConfig(Config):
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig,
}
