class Radiografia():

    def __init__(self, id, createdAt, hasPneumonia, documentoPaciente, usuarioId) -> None:
        self.id = id
        self.createdAt = createdAt
        self.hasPneumonia = hasPneumonia
        self.documentoPaciente = documentoPaciente
        self.usuarioId = usuarioId

    def toJson(self):
        return {
            "id": self.id,
            "createdAt": self.createdAt,
            "hasPneumonia": self.hasPneumonia,
            "documentoPaciente": self.documentoPaciente,
            "usuarioId": self.usuarioId
        }
