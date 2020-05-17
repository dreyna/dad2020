import pymysql
from conexion import Conexion
from sqlalchemy import create_engine
from json import dumps
cx = Conexion()

class Usuario:
    idusuario = 0
    nomuser = ""
    clave = ""
    estado = ""
    def readAll(self):
        try:
            sql = "select * from USUARIO"
            conexion=cx.conecta()
            cursor = conexion.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print(e)
        finally:
            conexion.close()
    def delete(self):
        try:
            sql = ""
            conexion = cx.conecta();
            cursor = conexion.cursor()
            cursor.execute("")