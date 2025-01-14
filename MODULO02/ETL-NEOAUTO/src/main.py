from prefect import task, flow
from task.task_prueba import task_prueba

@flow(name="ETL-PRUEBA")
def main_flow():
    task_prueba()
        
if __name__ == "__main__":
    main_flow()