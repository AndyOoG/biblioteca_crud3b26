import psycopg2
class Conexion:

    @staticmethod
    def obtener_conexion():
        return psycopg2.connect(
        host="localhost", database = "biblioteca_3b26",
        user = "postgres", password = "Enchiladasverdes2.", port =5432)