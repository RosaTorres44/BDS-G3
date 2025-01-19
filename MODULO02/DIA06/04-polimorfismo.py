from tabulate import tabulate

class Persona:
    def __init__(self, dni, nombre, mail):
        self.dni = dni
        self.nombre = nombre
        self.mail = mail

    def mostrar(self):
        data = [["DNI", self.dni], ["Nombre", self.nombre], ["Mail", self.mail]]
        print(tabulate(data, headers=["Campo", "Valor"], tablefmt="pretty", colalign=("center", "center")))
    
class Alumno (Persona):
    def __init__(self, dni, nombre, mail, nota):
        super().__init__(dni, nombre, mail)
        self.nota = nota

    def mostrar(self):
        super().mostrar()
        print(tabulate([["Nota", self.nota]], tablefmt="pretty", colalign=("center", "center")))
        
class Profesor(Persona):
    def __init__(self, dni, nombre, mail,esp):
        super().__init__(dni, nombre, mail)
        self.especialidad = esp
    
    def mostrar(self):
        super().mostrar()
        print(tabulate([["Especialidad", self.especialidad]], tablefmt="pretty"))          
        
class Empleado(Persona): 
    pass
alumno1 = Alumno('100','Rosa','rosa@gmai.com',20)
alumno1.mostrar()   

profesor1 = Profesor('100','Rosa','rosa@gmai.com','Matematica')
profesor1.mostrar()   

empleado = Empleado('200','Hanna','hanna@gmai.com')
empleado.mostrar()   