from extensions import db

class DatosPersonales(db.Model):
    __tablename__ = "DATOS_PERSONALES"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    NOMBRES = db.Column(db.String(100))
    APELLIDOS = db.Column(db.String(100))
    FECHA_NACIMIENTO = db.Column(db.Date)
    CI = db.Column(db.Integer) 
    GENERO = db.Column(db.String(20))
    TELEFONO = db.Column(db.Integer) 
    EMAIL = db.Column(db.String(100))
    TIPO_SANGUINEO = db.Column(db.String(5))
    ID_DIRECCION = db.Column(db.Integer, db.ForeignKey('DIRECCION.ID'))

    
    direccion = db.relationship('Direccion', back_populates='datos_personales')
    paciente = db.relationship('Paciente', back_populates='datos_personales')   
    medico = db.relationship("Medico", back_populates="datos_personales")

    def __init__(self, nombres, apellidos, fecha_nacimiento, ci, genero, telefono, email, tipo_sanguineo, direccion):
        self.NOMBRES = nombres
        self.APELLIDOS = apellidos
        self.FECHA_NACIMIENTO = fecha_nacimiento
        self.CI = ci
        self.GENERO = genero
        self.TELEFONO = telefono
        self.EMAIL = email
        self.TIPO_SANGUINEO = tipo_sanguineo
        self.direccion = direccion

    def insert(self):
        db.session.add(self)
        db.session.commit()
        
    def find_by_ci(ci):
        return DatosPersonales.query.filter_by(CI=ci).first()
    
    def as_dict(self):
        return {
            'ID': self.ID,
            'NOMBRES': self.NOMBRES,
            'APELLIDOS': self.APELLIDOS,
            'FECHA_NACIMIENTO': str(self.FECHA_NACIMIENTO),
            'CI': self.CI,
            'GENERO': self.GENERO,
            'TELEFONO': self.TELEFONO,
            'EMAIL': self.EMAIL,
            'TIPO_SANGUINEO': self.TIPO_SANGUINEO,
            'ID_DIRECCION': self.ID_DIRECCION,
        }
        
