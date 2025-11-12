from db_config import db

class Mascota(db.Model):  # Usa mayúscula para clase (buenas prácticas)
    __tablename__ = "mascota"
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    raza = db.Column(db.String(70))
    edad = db.Column(db.String(15))

    def __init__(self, nombre, raza, edad ):
        self.nombre = nombre
        self.raza = raza 
        self.edad = edad 
