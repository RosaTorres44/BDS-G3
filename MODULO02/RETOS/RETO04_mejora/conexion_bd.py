import mysql.connector 

def conectar_bd():
    try:
        connection = mysql.connector.connect(
            host="rtgmysql.mysql.database.azure.com",
            user="rtg_admin",
            password="mukkam-cyzVi4-vixdij",
            database="datag3"
        )
        print(f'Estas conectado a la base de datos: {connection.database}')
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    return connection
#conectar_bd()