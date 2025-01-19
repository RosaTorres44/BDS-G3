from prefect import task

@task(name="Transformar Data Neoauto")
def task_transform_neoauto(autos):
    autos_transform = []
    for auto in autos:
        nombre = auto['nombre'] 
        url = auto['url']
        precio = auto['precio']
        precio_num = float(precio.replace('US$','').replace(',',''))
        autos_transform.append({'nombre': nombre, 'url': url, 'precio': precio_num})
    return autos_transform