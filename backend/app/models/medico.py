from extensions import db
from .datos_personales import DatosPersonales

class Medico(db.Model):
    __tablename__ = "MEDICO"

    ID = db.Column(db.Integer, primary_key=True)
    ID_DATOS_PERSONALES = db.Column(db.Integer, db.ForeignKey("DATOS_PERSONALES.ID"))
    ESPECIALIDAD = db.Column(db.String(100))
    MARICULA = db.Column(db.String(100))
    datos_personales = db.relationship("DatosPersonales", back_populates="medico")

    def __init__(self, datos_personales, especialidad, maricula):
        self.datos_personales = datos_personales
        self.ESPECIALIDAD = especialidad
        self.MARICULA = maricula

    def insert(self):
        db.session.add(self)
        db.session.commit()