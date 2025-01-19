from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
import mysql.connector

class Empresa: 
    def __init__(self, app):
        self.app = app
        self.app.title('Gestion de Empresas')
        self.app.geometry('640x500')
        
        self.db = mysql.connector.connect(
            host='bi8vuvzuxbrzrznzlmiw-mysql.services.clever-cloud.com',
            user='u40zscggfnpilt7x',
            password='mlQhsUK4olxrQAT6lwvA',
            database='bi8vuvzuxbrzrznzlmiw')
        
        self.cursor = self.db.cursor()
        
        self.empresa_id = 0
        self.opcion=0
        
        frame = LabelFrame(self.app, text='Registro de Empresas')
        frame.grid(row=0, column=0, columnspan=2, pady=10, padx=10)
        
        lb_ruc = Label(frame, text='RUC')
        lb_ruc.grid(row=0, column=0)

        self.txt_ruc = Entry(frame)
        self.txt_ruc.grid(row=0, column=1)
        
        lb_razon_social = Label(frame, text='Razon Social')
        lb_razon_social.grid(row=1, column=0)
        
        self.txt_razon_social = Entry(frame)
        self.txt_razon_social.grid(row=1, column=1)
        
        self.btn_insert = Button(frame, text='Registrar Empresa', command=self.insertar_empresa)
        self.btn_insert.grid(row=2, column=0)
        
        self.btn_eliminar = Button(self.app, text='Eliminar Empresas', command=self.eliminar)
        self.btn_eliminar.grid(row=2, column=1)
        
        self.btn_editar = Button(self.app, text='Editar Empresas', command=self.editar)
        self.btn_editar.grid(row=2, column=0)
        
        
        self.tree = Treeview(self.app, columns=('RUC', 'Razon Social'))
        self.tree.grid(row=1, column=0, columnspan=2)
        self.tree.heading('#0', text='ID')
        self.tree.heading('#1', text='RUC')
        self.tree.heading('#2', text='Razon Social')

        self.tree.grid(row=1, column=0, padx=20, pady=10, columnspan=2)
        
        self.cargar_empresas()
        
    def cargar_empresas(self):
        
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        self.cursor.execute("SELECT id_empresa, nro_ruc, nombre FROM empresa;")
        for row in self.cursor.fetchall():
            self.tree.insert('', 0, text=row[0], values=(row[1], row[2]))
    
    def insertar_empresa(self):
        
        if not self.txt_ruc.get() or not self.txt_razon_social.get():
            messagebox.showwarning('Mensaje', 'Complete todos los campos!!')
            return
        
        if self.empresa_id > 0 and self.opcion==1:
            self.actualizar_empresa()
            return
        elif self.empresa_id > 0 and self.opcion == 2:
                self.eliminar_empresa()
                return
               

        nueva_empresa = (self.txt_ruc.get(), self.txt_razon_social.get())
        
        query = "INSERT INTO empresa (nro_ruc, nombre) VALUES (%s, %s)"
        self.cursor.execute(query, nueva_empresa)
        self.db.commit()
        
        messagebox.showinfo('Mensaje', 'Empresa registrada correctamente')
        
        self.cargar_empresas()
        
    def editar(self):
        selected_row = self.tree.selection()
        if not selected_row:
            messagebox.showwarning('Mensaje', 'Seleccione una empresa')
            return
        
        self.empresa_id = self.tree.item(selected_row)['text']
        self.opcion=1
        print("opcion : ", self.opcion)
        print("empresa a editar : ", self.empresa_id)
        self.txt_ruc.delete(0, END) 
        self.txt_ruc.insert(0, self.tree.item(selected_row)['values'][0])
        self.txt_razon_social.delete(0, END)
        self.txt_razon_social.insert(0, self.tree.item(selected_row)['values'][1])
        self.btn_insert.config(text='Actualizar Empresa')
    
    def eliminar(self):
        selected_row_eliminar = self.tree.selection()
        if not selected_row_eliminar:
            messagebox.showwarning('Mensaje', 'Seleccione una empresa a eliminar')
            return
        
        self.opcion=2
        self.empresa_id = self.tree.item(selected_row_eliminar)['text']
        print("opcion : ", self.opcion)
        print("empresa a eliminar : ", self.empresa_id)
        self.txt_ruc.delete(0, END)
        self.txt_ruc.insert(0, self.tree.item(selected_row_eliminar)['values'][0])
        self.txt_razon_social.delete(0, END)
        self.txt_razon_social.insert(0, self.tree.item(selected_row_eliminar)['values'][1])
        self.btn_insert.config(text='Eliminar Empresa')
    
    def actualizar_empresa(self):
        nuevo_ruc = self.txt_ruc.get()
        nueva_razon_social = self.txt_razon_social.get()
        
        empresa_actualizar = (nuevo_ruc, nueva_razon_social, self.empresa_id)
        
        if not nuevo_ruc or not nueva_razon_social:
            messagebox.showwarning('Mensaje', 'Complete todos los campos')
            return
        
        query = "UPDATE empresa SET nro_ruc=%s, nombre=%s WHERE id_empresa=%s"
        self.cursor.execute(query, empresa_actualizar)
        self.db.commit()
        self.cargar_empresas()
        self.limpiar_datos()

    def eliminar_empresa(self):
        nuevo_ruc = self.txt_ruc.get()
        nueva_razon_social = self.txt_razon_social.get()
        
        if not nuevo_ruc or not nueva_razon_social:
            messagebox.showwarning('Mensaje', 'Complete todos los campos')
            return
        
        respuesta = messagebox.askyesno('Mensaje', '¿Desea eliminar la empresa?')
        
        if respuesta:
            empresa_eliminar = (self.empresa_id,) 
            query = "DELETE FROM empresa WHERE id_empresa=%s"
            self.cursor.execute(query, empresa_eliminar)  # Pasa empresa_eliminar como tuple
            self.db.commit()
            self.cargar_empresas()
            self.limpiar_datos()

    
    
    def limpiar_datos(self):
        self.txt_ruc.delete(0, END)
        self.txt_razon_social.delete(0, END)
        self.empresa_id = 0
        self.btn_insert
        self.btn_insert.config(text='Insertar Empresa')