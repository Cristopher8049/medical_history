# from .setup_models import db
# from .analisis import Analisis
# from .laboratorio import Laboratorios
# from .detalle_historia import DetalleHistorias

# class HistoriasLaboratorio(db.Model):
#     __tablename__ = "HISTORIAS_LABORATORIO"

#     ID = db.Column(db.Integer, primary_key=True)
#     ID_ANALISIS = db.Column(db.Integer, db.ForeignKey("ANALISIS.ID"))
#     ID_LABORATORIO = db.Column(db.Integer, db.ForeignKey("LABORATORIOS.ID"))
#     analisis = db.relationship("Analisis", back_populates="historias_laboratorio")
#     laboratorio = db.relationship("Laboratorios", back_populates="historias_laboratorio")