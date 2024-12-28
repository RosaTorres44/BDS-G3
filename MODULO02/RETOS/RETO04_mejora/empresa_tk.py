from tkinter import *
from conexion_bd import conectar_bd

class EmpresaTk:
    
    def __init__(self):
        self.db = conectar_bd()
        self.cursor = self.db.cursor()


    def cargar_empresas(self, tree):
        # Limpiar los datos existentes en el Treeview
        for item in tree.get_children():
            tree.delete(item)

        # Cargar datos desde la base de datos
        self.cursor.execute("SELECT id_empresa, nro_ruc, nombre FROM empresa ORDER BY id_empresa")
        for row in self.cursor.fetchall():
            tree.insert('', 0, text=row[0], values=(row[1], row[2]))
            
    def insertar_empresa(self,ruc, razon_social, tree):
        nueva_empresa = (ruc, razon_social)
        query = "INSERT INTO empresa(nro_ruc, nombre) VALUES (%s, %s)"
        self.cursor.execute(query, nueva_empresa)
        self.db.commit()
        print("Empresa insertada")
        
         # Recargar datos en el Treeview
        self.cargar_empresas(tree)
        
    def eliminar(self, ruc, tree):
        query = "DELETE FROM empresa WHERE nro_ruc = %s"
        self.cursor.execute(query, (ruc,))
        self.db.commit()
        print("Empresa eliminada")
        
        # Recargar datos en el Treeview
        self.cargar_empresas(tree)

    def actualizar(self, nueva_razon_social, nuevo_ruc, tree):

        query = "UPDATE empresa SET nombre = %s WHERE nro_ruc = %s"
        self.cursor.execute(query, (nueva_razon_social, nuevo_ruc,))
        self.db.commit()
         # Recargar datos en el Treeview
        self.cargar_empresas(tree)
        print("Empresa actualizada")