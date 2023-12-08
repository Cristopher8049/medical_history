from extensions import db

class Paciente(db.Model):
    __tablename__ = "PACIENTE"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ID_DATOS_PERSONALES = db.Column(db.Integer, db.ForeignKey("DATOS_PERSONALES.ID"))
    
    
    datos_personales = db.relationship("DatosPersonales", back_populates="paciente")  
    detalle_historias = db.relationship("DetalleHistorias", back_populates="paciente")
    
    def __init__(self, datos_personales):
        self.datos_personales = datos_personales

    def insert(self):
        db.session.add(self)
        db.session.commit()


