from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
from empresa_tk import EmpresaTk

class MainWindow:
    def __init__(self, app):
        self.app = app
        self.app.title("Gestión de Empresas")
        self.app.geometry('800x600')

        # Crear la barra de menú
        self.menu_bar = Menu(self.app)
        self.app.config(menu=self.menu_bar)

    # Menú "Opciones"
        self.opciones_menu = Menu(self.menu_bar, tearoff=0)
        self.opciones_menu.add_command(label="Mostrar", command=self.mostrar_empresas)
        self.opciones_menu.add_command(label="Insertar", command=self.insertar_empresa)
        self.opciones_menu.add_command(label="Eliminar", command=self.eliminar_empresa)
        self.opciones_menu.add_command(label="Actualizar", command=self.actualizar_empresa)
        self.opciones_menu.add_separator()
        self.opciones_menu.add_command(label="Salir", command=self.salir_sistema)
        self.menu_bar.add_cascade(label="Opciones", menu=self.opciones_menu)

        
        # Mostrar el menú "Opciones" al iniciar
        self.opciones_menu.post(0, 0)   

    def mostrar_empresas(self):
        self.empresa_tk = EmpresaTk()
        
        # Grilla de empresas
        self.tree = Treeview(self.app, columns=('RUC', 'RAZÓN SOCIAL'))
        self.tree.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        self.tree.heading('#0', text='ID')
        self.tree.heading('RUC', text='RUC')
        self.tree.heading('RAZÓN SOCIAL', text='RAZÓN SOCIAL')
        
        self.empresa_tk.cargar_empresas(self.tree)
        

    def insertar_empresa(self):
        
        # Frame para insertar nueva empresa
        frame = LabelFrame(self.app, text='Registrar nueva empresa')
        frame.grid(row=0, column=0, columnspan=2, pady=10, padx=50)
        # Ingresar RUC
        lb_ruc = Label(frame, text='RUC')
        lb_ruc.grid(row=1, column=0)
        self.txt_ruc = Entry(frame)
        self.txt_ruc.grid(row=1, column=1)

        # Ingresar Razón Social
        lb_razsocial = Label(frame, text='Razón Social')
        lb_razsocial.grid(row=2, column=0)
        self.txt_nrazsocial = Entry(frame)
        self.txt_nrazsocial.grid(row=2, column=1)

        
        btn_insertar = Button(frame, text='Insertar', command=self.insertar_empresa_bd)
        btn_insertar.grid(row=3, columnspan=2, sticky=W+E)
        
            
    def insertar_empresa_bd(self):
        ruc = self.txt_ruc.get()
        razon_social = self.txt_nrazsocial.get()

        if ruc and razon_social:
            self.empresa_tk.insertar_empresa(ruc, razon_social, self.tree)
            self.txt_ruc.delete(0, END)
            self.txt_nrazsocial.delete(0, END)
            messagebox.showinfo("Éxito", "Empresa registrada correctamente")
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos")

    def eliminar_empresa(self):
        
        self.empresa_tk = EmpresaTk()
        # Frame para eliminar  empresa
        frame = LabelFrame(self.app, text='Eliminar  empresa')
        frame.grid(row=0, column=0, columnspan=2, pady=10, padx=50)
        # Ingresar RUC
        lb_ruc = Label(frame, text='RUC')
        lb_ruc.grid(row=1, column=0)
        self.txt_ruc = Entry(frame)
        self.txt_ruc.grid(row=1, column=1)
        
        btn_eliminar = Button(frame, text='Eliminar', command=self.eliminar_empresa_bd)
        btn_eliminar.grid(row=3, columnspan=2, sticky=W+E)
        
    
        
    def eliminar_empresa_bd(self): 
        ruc = self.txt_ruc.get()
        
        if ruc :
            self.empresa_tk.eliminar(ruc, self.tree)
            self.txt_ruc.delete(0, END) 
            messagebox.showinfo("Éxito", "Empresa eliminada correctamente")
        else:
            messagebox.showwarning("Advertencia", "Por favor, confirme el ruc")

    def actualizar_empresa(self):
        self.empresa_tk = EmpresaTk()
        # Frame para actualizar  empresa
        frame = LabelFrame(self.app, text='Actualizar empresa')
        frame.grid(row=0, column=0, columnspan=2, pady=10, padx=50)
        # Ingresar RUC
        lb_ruc = Label(frame, text='RUC')
        lb_ruc.grid(row=1, column=0)
        self.txt_ruc = Entry(frame)
        self.txt_ruc.grid(row=1, column=1)
        
        # Ingresar Razón Social
        lb_razsocial = Label(frame, text='Razón Social')
        lb_razsocial.grid(row=2, column=0)
        self.txt_nrazsocial = Entry(frame)
        self.txt_nrazsocial.grid(row=2, column=1)

        btn_actualizar = Button(frame, text='Actualizar', command=self.actualizar_empresa_bd)
        btn_actualizar.grid(row=3, columnspan=2, sticky=W+E)
        
    def actualizar_empresa_bd(self): 
        ruc = self.txt_ruc.get()
        razon_social = self.txt_nrazsocial.get()
        
        if ruc and razon_social:
            self.empresa_tk.actualizar(razon_social,ruc,self.tree)
            self.txt_ruc.delete(0, END) 
            messagebox.showinfo("Éxito", "Empresa actualizada correctamente")
        else:
            messagebox.showwarning("Advertencia", "Por favor, confirme el ruc")
        

    def salir_sistema(self):
        if messagebox.askyesno("Confirmar", "¿Deseas salir del sistema?"):
            self.app.quit()
