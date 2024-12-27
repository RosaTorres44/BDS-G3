def cargar_empresas(nombre_archivo):
    archivo = open(nombre_archivo, 'r')
    str_empresas = archivo.read()
    archivo.close()
    
    empresas = {}
    for linea in str_empresas.splitlines():
        ruc, razon_social, direccion = linea.split(',')
        empresas[ruc] = {'razon_social': razon_social, 'direccion': direccion}
    
    return empresas


empresas = cargar_empresas('archivo_empresas.txt')
print(empresas)


