from src.database.db import getConnection
from .entities.Usuario import Usuario

class UsuarioModel():
    
    @classmethod
    def getUsuarios(self):
        conn = getConnection()
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM usuario ORDER BY id ASC")
                rows = cur.fetchall()
                usuarios = []
                for row in rows:
                    usuario = Usuario(
                        id=row[0],
                        createdAt=row[1],
                        admin=row[2],
                        email=row[3],
                        nombre=row[4],
                        apellido=row[5],
                        documento=row[6],
                        password=row[7]
                    )
                    usuarios.append(usuario.toJson())
                return usuarios
        except Exception as ex:
            raise Exception(ex)
        finally:
            conn.close()
            
    @classmethod
    def getUsuario(self, id):
        conn = getConnection()
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM usuario WHERE id = %s", (id,))
                row = cur.fetchone()
                
                usuario = None
                if row != None:
                    usuario = Usuario(
                        id=row[0],
                        createdAt=row[1],
                        admin=row[2],
                        email=row[3],
                        nombre=row[4],
                        apellido=row[5],
                        documento=row[6],
                        password=row[7]
                    )
                    usuario = usuario.toJson()
                return usuario
        except Exception as ex:
            raise Exception(ex)
        finally:
            conn.close()
