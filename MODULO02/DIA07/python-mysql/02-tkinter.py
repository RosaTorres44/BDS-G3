from tkinter import *
from tkinter import messagebox

def saludar():
    nombre = txt_nombre.get()
    messagebox.showinfo('Saludo', f'Hola {nombre}')

app = Tk()
app.title("Mi App")
app.geometry("400x600")

#frame
frame = LabelFrame(app, text= 'Nueva Ventana', padx=50, pady=50)
frame.grid(row=0, column=0, padx=10, pady=10)

#label  
lb_nombre = Label(frame, text='Nombre:')
lb_nombre.grid(row=1,column=0)

#texto
txt_nombre = Entry(frame)
txt_nombre.grid(row=1,column=1)

#button
btn_saludo = Button(frame, text='Saludar', command=saludar)
btn_saludo.grid(row=2,column=1)

app.mainloop()