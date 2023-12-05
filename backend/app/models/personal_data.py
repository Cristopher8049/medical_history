from .setup_models import db

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    ci = db.Column(db.String(20))
    nombres = db.Column(db.String(100))
    apellidos = db.Column(db.String(100))
    tipo_usr = db.Column(db.String(20))
    carrera = db.Column(db.String(100))
    id_huella = db.Column(db.String(50))
    huella = db.Column(db.String(40))
    usr_name = db.Column(db.String(100))
    passwrd = db.Column(db.String(100))
    email = db.Column(db.String(100))
    telefono = db.Column(db.String(100))
    nombre_ref = db.Column(db.String(100))
    telefono_ref = db.Column(db.String(100))
    email_ref = db.Column(db.String(100))




    def __init__(
        self,
        ci,
        nombres,
        apellidos,
        tipo_usr,
        carrera,
        id_huella,
        huella,
        usr_name,
        passwrd,
        email,
        telefono,
        nombre_ref,
        telefono_ref,
        email_ref,
    ):
        self.ci = ci
        self.nombres = nombres
        self.apellidos = apellidos
        self.tipo_usr = tipo_usr
        self.carrera = carrera
        self.id_huella = id_huella
        self.huella = huella
        self.usr_name = usr_name
        self.passwrd = passwrd
        self.email = email
        self.telefono = telefono
        self.nombre_ref = nombre_ref
        self.telefono_ref = telefono_ref
        self.email_ref = email_ref

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete()
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            "CI": self.ci,
            "Nombres": self.nombres,
            "Apellidos": self.apellidos,
            "Tipo de user": self.tipo_usr,
            "Carrera": self.carrera,
            "ID huella": self.id_huella,
            "Huella": self.huella,
            "Username": self.usr_name,
            "Password": self.passwrd,
            "Email": self.email,
            "Telefono": self.telefono,
            "Nombre Referencia": self.nombre_ref,
            "Telefono Referencia": self.telefono_ref,
            "Email Referencia": self.email_ref,
        }


def create_user():
    user_1 = User(
        ci="3434323",
        nombres="Jose Jesus",
        apellidos="Cabrera Pantoja",
        tipo_usr="Student",
        carrera="Software",
        id_huella="123",
        huella="npi",
        usr_name="josejesus",
        passwrd="123",
        email="cp.josejesus@email.com",
        telefono="1231231",
        nombre_ref="jose",
        telefono_ref="12312",
        email_ref="casdas",
    )

    user_2 = User(
        ci="5665233",
        nombres="Jose Jesus",
        apellidos="Cabrera Pantoja",
        tipo_usr="Student",
        carrera="Software",
        id_huella="123",
        huella="npi",
        usr_name="josejesus",
        passwrd="123",
        email="cp.josejesus@email.com",
        telefono="1231231",
        nombre_ref="jose",
        telefono_ref="12312",
        email_ref="casdas",
    )

    user_3 = User(
        ci="9807432",
        nombres="Jose Jesus",
        apellidos="Cabrera Pantoja",
        tipo_usr="Student",
        carrera="Software",
        id_huella="123",
        huella="npi",
        usr_name="josejesus",
        passwrd="123",
        email="cp.josejesus@email.com",
        telefono="1231231",
        nombre_ref="jose",
        telefono_ref="12312",
        email_ref="casdas",
    )

    user_1.insert()
    user_2.insert()
    user_3.insert()
