# from .setup_models import db
# from .paciente import Paciente
# from .medico import Medico
# from .clinica import Clinica
# from .historia_clinica import HistoriaClinica
# from .historia_laboratorio import HistoriasLaboratorio


# class DetalleHistorias(db.Model):
#     __tablename__ = "DETALLE_HISTORIAS"

#     ID = db.Column(db.Integer, primary_key=True)
#     DIAGNOSTICO = db.Column(db.String(100))
#     FECHA = db.Column(db.Date)
#     ID_PACIENTE = db.Column(db.Integer, db.ForeignKey("PACIENTE.ID"))
#     ID_MEDICO = db.Column(db.Integer, db.ForeignKey("MEDICO.ID"))
#     ID_CLINICA = db.Column(db.Integer, db.ForeignKey("CLINICA.ID"))
#     ID_HISTORIAS_LABORATORIO = db.Column(db.Integer, db.ForeignKey("HISTORIAS_LABORATORIO.ID"))
#     paciente = db.relationship("Paciente", back_populates="detalle_historias")
#     medico = db.relationship("Medico", back_populates="detalle_historias")
#     clinica = db.relationship("Clinica", back_populates="detalle_historias")
#     historia_clinica = db.relationship("HistoriaClinica", back_populates="detalle_historias")
#     historias_laboratorio = db.relationship("HistoriasLaboratorio", back_populates="detalle_historias")
