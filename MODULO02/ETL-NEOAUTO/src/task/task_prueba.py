from prefect import task

@task(name="tarea de prueba")
def task_prueba():
    print("Hola mundo")