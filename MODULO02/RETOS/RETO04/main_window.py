from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
from empresa_tk import EmpresaTk 

class MainWindow:
    def __init__(self, app):
        self.app = app
        self.app.title("Gestión de Empresas")
        self.app.geometry('640x480')

        self.empresa_tk = EmpresaTk()
        
        frame = LabelFrame(self.app, text='Registrar nueva empresa')
        frame.grid(row=0, column=0, columnspan=2, pady=10,padx=50)
        
        #Ingresar RUC 
        lb_ruc = Label(frame, text='RUC')
        lb_ruc.grid(row=1, column=0)
        self.txt_ruc = Entry(frame)
        self.txt_ruc.grid(row=1, column=1)
        
        #Ingresar Razon Social
        lb_razsocial = Label(frame, text='Razon Social')
        lb_razsocial.grid(row=2, column=0)
        self.txt_nrazsocial = Entry(frame)
        self.txt_nrazsocial.grid(row=2, column=1)
        
        btn_insertar = Button(frame, text='Insertar', command=self.insertar_empresa)
        btn_insertar.grid(row=3, columnspan=2, sticky=W+E)
        
        #grilla de empresas
        self.tree = Treeview(self.app, columns=('RUC','RAZON SOCIAL'))
        self.tree.grid(row=4, column=0, columnspan=2,padx=10,pady=10)
        self.tree.heading('#0', text='id')
        self.tree.heading('RUC', text='RUC')
        self.tree.heading('RAZON SOCIAL', text='RAZON SOCIAL')
        
        
         # Cargar empresas al inicio
        self.empresa_tk.cargar_empresas(self.tree)
        
    def insertar_empresa(self):
    # Obtener datos de los campos de entrada
        ruc = self.txt_ruc.get()
        razon_social = self.txt_nrazsocial.get()

        if ruc and razon_social:
            # Insertar nueva empresa y actualizar la grilla
            self.empresa_tk.insertar_empresa(ruc, razon_social, self.tree)

            # Limpiar los campos de entrada
            self.txt_ruc.delete(0, END)
            self.txt_nrazsocial.delete(0, END)

            messagebox.showinfo("Éxito", "Empresa registrada correctamente")
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos")

 