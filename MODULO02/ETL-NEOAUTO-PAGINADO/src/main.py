from prefect import flow 
from task.task_prueba import task_prueba
from task.task_extract_neoauto import task_extract_neoauto
from task.task_transfrom_neoauto import task_transfrom_neoauto
from task.task_load_neoautos import task_load_neoauto
from task.task_extra_total_pages import task_extra_total_pages
import time

@flow(name="ETL-PRUEBA")
def main_flow():
    print("Inicio del flujo...")
    total_pages = task_extra_total_pages()
    print("Total de paginas: ", total_pages)
    
    for page in range(1,total_pages + 1,1):
        print(f'extract page {page}...')
        autos = task_extract_neoauto(page)
        #PASO 2 - TRANSFORMAR DATA
        autos_transform = task_transfrom_neoauto(autos)
        #PASO 3 - CARGAR DATA
        task_load_neoauto(autos_transform)
        time.sleep(1)

        
if __name__ == "__main__":
    main_flow()