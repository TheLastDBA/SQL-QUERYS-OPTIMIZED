# import mysql.connector
# from mysql.connector import Error
import requests
import json
import clases_1

url_api = r='https://api.chucknorris.io/jokes/random'
get = requests.get(url=url_api)
response_check_api = get.json()
response_check_api.items()



print(response_check_api.items())


contar = clases_1.Counter(nombre="Didier va por", cantidad_numero=10000000)

print(contar.contar())

# try:
#     conexion_tecnosoft = mysql.connector.connect(user = 'prueba',database='',host='',port='3306',password='')

#     print('Estado de conexion:' , conexion_tecnosoft)

# except Error as e:
#     print(e)

# cursor_tecnosoft = conexion_tecnosoft.cursor()
# cursor_tecnosoft.execute('select * from catalogo.acciones;')
# result_tecno_acciones = cursor_tecnosoft.fetchall()

# for id,texto,foreigns in result_tecno_acciones:


#     print(id,texto,foreigns)




  
    

