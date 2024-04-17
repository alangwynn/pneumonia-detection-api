from src.utils.DateFormat import DateFormat

class Usuario():
    
    def __init__(self, id, createdAt=None, admin=None, email=None, nombre=None, apellido=None, documento=None, password=None) -> None:
        self.id = id
        self.createdAt = createdAt
        self.admin = admin
        self.email = email
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.password = password
        
    def toJson(self):
        return {
            "id": self.id,
            "createdAt": DateFormat.convert_date(self.createdAt),
            "admin": self.admin,
            "email": self.email,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "documento": self.documento,
            "password": self.password
        }
    