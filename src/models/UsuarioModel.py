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

    @classmethod
    def loginUsuario(cls, documento, password):
        conn = getConnection()
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM usuario WHERE documento = %s AND password = %s", (documento, password))
                row = cur.fetchone()
                
                if row is not None:
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
                    return usuario.toJson()
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)
        finally:
            conn.close()

    @classmethod
    def eliminarUsuario(cls, id):
        conn = getConnection()
        try:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM usuario WHERE id = %s", (id,))
                conn.commit()
        except Exception as ex:
            conn.rollback()
            raise ex
        finally:
            conn.close()
    
    @classmethod
    def crearUsuario(cls, admin, email, nombre, apellido, documento, password):
        conn = getConnection()
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM usuario WHERE documento = %s", (documento,))
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
                    if usuario != None:
                        return usuario.toJson()
            
            with conn.cursor() as cur:
                cur.execute("INSERT INTO usuario (admin, email, nombre, apellido, documento, password) VALUES (%s, %s, %s, %s, %s, %s)", (admin, email, nombre, apellido, documento, password))
                conn.commit()
        except Exception as ex:
            conn.rollback()
            raise ex
        finally:
            conn.close()