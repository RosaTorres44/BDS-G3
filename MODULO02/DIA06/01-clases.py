class Automovil:
    def __init__(self, aa, pl, col, mar):
        self.año = aa
        self.placa = pl
        self.color = col
        self.marca = mar
        print(f"Se ha creado un auto de marca {self.marca} del año {self.año} con placa {self.placa} y color {self.color}")

    def encender(self):
        print(f"El auto de marca {self.marca} se ha encendido")
    
    def avanzar(self):
        print(f"El auto de marca {self.marca} ha avanzado")
    
    def frenar (self):
        print(f"El auto de marca {self.marca} ha frenado")

    def apagar(self):
        print(f"El auto de marca {self.marca} se ha apagado")

#creamos objetos
print("Objetos creados")
vw = Automovil(2020, "PQW-123", "Rojo", "Volkswagen")
vw.encender()
vw.avanzar()
vw.frenar()
vw.apagar()


tico = Automovil(2010, "ABC-123", "Azul", "DAEWOO")
tico.encender()
tico.avanzar()
tico.frenar()
tico.apagar()

