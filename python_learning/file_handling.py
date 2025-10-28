# # Manejar archivos en Python, para manejar archivos en python es necesario tener lo siguiente: abrimos un archivo manual: file = open(path/tuarchivo.txt)  --> file.read() --> file.close()
# # o podemos hacer lo siguiente: with open() as file: file.read()
# # AHORA BIEN, TU PUEDES SETEAR MODOS, PARA SETEARLOS DEBES RESPETAR EL ORDEN DE LOS FLAGS, POR EJEMPLO with open('PATH/read.txt', 'r') as file: file.read()
# # DONDE ESTA LA LETRA 'r' como parametro podemos enviar lo siguiente: 'r' , 'w'  , 'a' , ''


import csv
from os import path
import os


# try:
           
#     with open(r"C:\yUsers\didier.acuna\git-repos\readmes.txt",'w+') as readme:
#         print( readme.write("""\n Este repo es el resultado de practicas en python, esta linea fue creada desde python de esta forma: \n \n with open(r"C:\\Users\\didier.acuna\\git-repos\\readme.txt",'w+') as readme:
#         print( readme.write(Este repo es el resultado de practicas en python, esta linea fue creada desde python de esta forma: )) """), print(readme.read()))

#     with open(r"C:\yUsers\didier.acuna\git-repos\readmes.txt",'a+') as readme:
#         for line in readme:
#             line = line + 'Añadiendo esto'
#             readme.write(line)
#         else:
#             print('fin')
# except:
#     print('you have an error in your code')
# finally:
#    with open(r"C:\Users\didier.acuna\git-repos\readmes.txt",'r') as readme:
#        print(readme.read())


try: 
    with open(r'C:\Users\didier.acuna\git-repos\modified_file.txt','a+') as file_new_txt:
        existencia = file_new_txt
        if path.getsize(r'C:\Users\didier.acuna\git-repos\modified_file.txt') == 0:
            print('vacio')
        else:
            print('No vacio \n')

        for i in ['DIDIER','SHARO','MELISSA','ARIANA','JESSICA',1,]:
            file_new_txt.write(f'\n {i}')
        else:
            file_new_txt.seek(0)
            print(file_new_txt.read())
            print(os.path.exists(r'C:\Users\didier.acuna\git-repos\modified_file.txt'))
            
except Exception as e:
    raise Exception(f'Ha sucedido un error en tu codigo; {e}')
finally:
    print('The program is close.')
    os.remove(r'C:\Users\didier.acuna\git-repos\modified_file.txt')







 





# with open("C:\\Users\\didier.acuna\\Downloads\\Sample.Data.v3\\Sample Data v3\\Catalog_v2.csv",'r') as csv_catalog_file:
#     print(csv_catalog_file.read())

