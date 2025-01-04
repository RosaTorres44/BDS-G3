from tabulate import tabulate

import mysql.connector 

connection = mysql.connector.connect(
    host="rtgmysql.mysql.database.azure.com",
    user="rtg_admin",
    password="",
    database="datag3"
)

print(f'Estas conecatado a la base de datos: {connection.database}')    

alumno_cursor = connection.cursor()
#alumno_cursor.execute("insert into alumno (nro_doc,nombre) values ('123', 'Juan')")
#connection.commit()
#print(f'Alumno insertado con exito')

alumno_cursor_select = connection.cursor()
alumno_cursor_select.execute("select * from alumno")
resultado = alumno_cursor_select.fetchall()
print(alumno_cursor_select.description)
print(resultado)

headers = [i[0] for i in alumno_cursor_select.description]
print(tabulate(resultado, headers=headers, tablefmt='psql'))

connection.close()
