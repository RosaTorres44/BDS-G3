class Persona:
    def __init__(self, dni, nombre, mail):
        self.dni = dni
        self.nombre = nombre
        self.mail = mail

    def mostrar(self):
        print(f"Persona: {self.nombre} ({self.dni})")

class Alumno (Persona):
    pass
        
class Profesor(Persona):
    def __init__(self, dni, nombre, mail,esp):
        super().__init__(dni, nombre, mail)
        self.especialidad = esp
    
    def mostrar(self):
        print(f"Profesor: {self.nombre} ({self.dni}) - {self.especialidad}")
          
alumno1 = Alumno('100','Rosa','rosa@gmai.com')
alumno1.mostrar()   

profesor1 = Profesor('100','Rosa','rosa@gmai.com','Matematica')
profesor1.mostrar()   