from tkinter import Tk
from main_window import MainWindow

if __name__ == "__main__":
    app = Tk()
    app_empresa = MainWindow(app)
    app.mainloop()