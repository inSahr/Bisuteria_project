import pymysql

class Conexion:
    @staticmethod
    def obtener_conexion():
        return pymysql.connect(host="localhost", 
                               user="root",
                               password="",
                               db="bisuteria")

