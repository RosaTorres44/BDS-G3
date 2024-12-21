dias = ("lunes", "martes", "miércoles", "jueves")
"""
la tupla es una estructura de datos inmutable, es decir, no se puede modificar una vez creada.

Tuple:
    dias (tuple): A tuple containing the following days of the week:
        - "lunes"
        - "martes"
        - "miércoles"
        - "jueves"
"""


#convertir la tupla en lista
dias = list(dias) 
print(type(dias))
dias.append("viernes")
dias = tuple(dias)  
print(type(dias))

#recorrer la lista
for dia in dias:
    print(dia)