from extensions import db

class Direccion(db.Model):
    __tablename__ = "DIRECCION"

    ID = db.Column(db.Integer, primary_key=True)
    DIRECCION = db.Column(db.String(100))
    CIUDAD = db.Column(db.String(100))
    PROVINCIA = db.Column(db.String(100))
    PAIS = db.Column(db.String(100))


    datos_personales = db.relationship('DatosPersonales', back_populates='direccion', uselist=False)
    clinica = db.relationship("Clinica", back_populates="direccion")

    def __init__(self, direccion, ciudad, provincia, pais):
        self.DIRECCION = direccion
        self.CIUDAD = ciudad
        self.PROVINCIA = provincia
        self.PAIS = pais

    def insert(self):
        db.session.add(self)
        db.session.commit()

