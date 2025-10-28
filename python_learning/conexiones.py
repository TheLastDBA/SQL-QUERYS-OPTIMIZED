import mysql.connector
from mysql.connector import Error

try:
    conexion_tecnosoft = mysql.connector.connect(user = 'prueba',database='tecnosoft',host='10.1.2.89',port='3306',password='Tecnoglass*2025')

    print('Estado de conexion:' , conexion_tecnosoft)

except Error as e:
    print(e)

cursor_tecnosoft = conexion_tecnosoft.cursor()
cursor_tecnosoft.execute('select * from catalogo.acciones;')
result_tecno_acciones = cursor_tecnosoft.fetchall()

for id,texto,foreigns in result_tecno_acciones:


    print(id,texto,foreigns)




  
    

