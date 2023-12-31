from extensions import db

class Clinica(db.Model):
    __tablename__ = "CLINICA"

    ID = db.Column(db.Integer, primary_key=True)
    NOMBRE = db.Column(db.String(100))
    TELEFONO = db.Column(db.String(100))
    ID_DIRECCION = db.Column(db.Integer, db.ForeignKey("DIRECCION.ID"))
    
    direccion = db.relationship("Direccion", back_populates="clinica")
    detalle_historias = db.relationship("DetalleHistorias", back_populates="clinica")
