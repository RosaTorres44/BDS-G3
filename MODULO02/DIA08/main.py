from tkinter import *
from lib_empresas import Empresa

app = Tk()  

if __name__ == '__main__':
    empresa = Empresa(app)
    app.mainloop()