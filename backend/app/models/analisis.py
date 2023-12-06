# from .setup_models import db
# from .historia_laboratorio import HistoriasLaboratorio

# class Analisis(db.Model):
#     __tablename__ = "ANALISIS"

#     ID = db.Column(db.Integer, primary_key=True)
#     NOMBRE = db.Column(db.String(100))
#     historias_laboratorio = db.relationship("HistoriasLaboratorio", back_populates="analisis")