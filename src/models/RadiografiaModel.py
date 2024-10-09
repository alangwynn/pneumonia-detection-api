from src.database.db import getConnection

class Radiografia():

    def __init__(self, id, createdAt, hasPneumonia, documentoPaciente, usuarioId) -> None:
        self.id = id
        self.createdAt = createdAt
        self.hasPneumonia = hasPneumonia
        self.documentoPaciente = documentoPaciente
        self.usuarioId = usuarioId

    @classmethod
    def loadRadiography(cls, documento, hasPneumonia, userId):
        conn = getConnection()
        print(documento)
        print(hasPneumonia)
        print(userId)
        try:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO public.radiografia (hasneumonia, documentopaciente, userid) VALUES (%s, %s, %s) RETURNING id, createdat",
                            (hasPneumonia, documento, userId))
                conn.commit()
                row = cur.fetchone()
                print(row)
                if row:
                    new_id, created_at = row
                    print(new_id)
                    print(created_at)
                    new_radiography = Radiografia(new_id, created_at, hasPneumonia, documento, userId)
                    return new_radiography
                else:
                    raise Exception("No se pudo obtener el ID y la fecha de creación del nuevo registro.")
        except Exception as ex:
            raise Exception("Error al cargar la radiografía en la base de datos:", ex)
        finally:
            conn.close()

    def toJson(self):
        return {
            "id": self.id,
            "createdAt": self.createdAt,
            "hasPneumonia": self.hasPneumonia,
            "documentoPaciente": self.documentoPaciente,
            "usuarioId": self.usuarioId
        }
