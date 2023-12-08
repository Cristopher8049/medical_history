from extensions import db

class DetalleHistorias(db.Model):
    __tablename__ = "DETALLE_HISTORIAS"

    ID = db.Column(db.Integer, primary_key=True)
    DIAGNOSTICO = db.Column(db.String(100))
    FECHA = db.Column(db.Date)
    LABORATORIO = db.Column(db.String(100)) 
    ID_PACIENTE = db.Column(db.Integer, db.ForeignKey("PACIENTE.ID"))
    ID_MEDICO = db.Column(db.Integer, db.ForeignKey("MEDICO.ID"))
    ID_CLINICA = db.Column(db.Integer, db.ForeignKey("CLINICA.ID"))
    
    
    medico = db.relationship("Medico", back_populates="detalle_historias")
    clinica = db.relationship("Clinica", back_populates="detalle_historias")
    paciente = db.relationship("Paciente", back_populates="detalle_historias")

    def __init__(self, diagnostico, fecha, paciente, medico, clinica, laboratorio):
        self.DIAGNOSTICO = diagnostico
        self.FECHA = fecha
        self.paciente = paciente
        self.medico = medico
        self.clinica = clinica
        self.LABORATORIO= laboratorio
        
    def insert(self):
        db.session.add(self)
        db.session.commit()
        
        