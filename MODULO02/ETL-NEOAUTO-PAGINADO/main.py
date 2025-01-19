from prefect import flow 
from task.task_prueba import task_prueba
from task.task_extract_neoauto import task_extract_neoauto
from task.task_transfrom_neoauto import task_transform_neoauto
from task.task_load_neoautos import task_load_neoauto

@flow(name="ETL-PRUEBA")
def main_flow():
    print("Inicio del flujo...")
    task_prueba()
    print("Extraer Datos")
    autos = task_extract_neoauto()
    print("Transformar Datos")
    autos_transform = task_transform_neoauto(autos)
    print("Cargar Datos")
    task_load_neoauto(autos_transform)
    print(autos_transform)

        
if __name__ == "__main__":
    main_flow()