import sqlite3

class ConexionDB:
    def __init__(self):
        self.base_datos = "database/peliculas.db"
        self.conexion = sqlite3.connect(self.base_datos)
        self.cursor = self.conexion.cursor()
        
    def cerrar(self):
        self.conexion.commit()#realizar cambios, confirmar cambios
        self.conexion.close()#cerrar la conexion
        
        