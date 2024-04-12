class Usuario():
    def __init__(self, id, createdAt, admin, email, nombre, apellido, documento, password) -> None:
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
            "createdAt": self.createdAt,
            "admin": self.admin,
            "email": self.email,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "documento": self.documento,
            "password": self.password
        }