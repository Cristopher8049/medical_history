# from .setup_models import db
# from .paciente import Paciente
# from .detalle_historia import DetalleHistorias

# class HistoriaClinica(db.Model):
#     __tablename__ = "HISTORIA_CLINICA"

#     ID = db.Column(db.Integer, primary_key=True)
#     ID_PACIENTE = db.Column(db.Integer, db.ForeignKey("PACIENTE.ID"))
#     ID_DETALLE_HISTORIAS = db.Column(db.Integer, db.ForeignKey("DETALLE_HISTORIAS.ID"))
#     paciente = db.relationship("Paciente", back_populates="historias_clinicas")
#     detalle_historias = db.relationship("DetalleHistorias", back_populates="historia_clinica")