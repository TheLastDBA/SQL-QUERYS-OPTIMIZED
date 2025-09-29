# # #this is a comment in my python language, so this line would be ignored by the py engine

# # nombre = "Didier"

# # def python_method(nombre):
# #     response = 'Hola mundo, soy '+ '\" ' + nombre + ' \" '+ ' y \n esto es \n \n \n python.'
# #     return response


# # def print_suma(valor1,valor2):
# #     sumar = valor1 + valor2
# #     return sumar

# # def invocar_methods():
# #     print(python_method('DIDIER'), '\n', 'con una suma de', print_suma(20,4), 'años de edad;', "Double quotes here ")
# # #Fin methods

# # invocar_methods() # Ultima linea de codigo comentada que invoca a la funcion

# # print('Your learning path:\n\t-Python Basics \n\t-Data Engineering \n\t-AI')

# # print('Este es un salto de \n linea')
# # print('Este es un backslash \\ para ignorar reserved values')
# # print('Este es un reserved value para printear una felcha \\t')
# # print('Este es un \"""(triple quote) para escribir en bloque:', """ \nasi: \n 
# # '-> para escribir a merced \n
# # '-> y que no haya errores. """)

# # comodin ='datawithdidier.com'
# # print('info@'+comodin)
# # print('support@'+comodin)
# # print('www.'+comodin)


# # def incremento_value(x):
# #     inc = 0.18 
# #     x = x +(x*inc)
# #     return x

# # # #full_name = input('Enter your full name: ')
# # # salary = int(input('Enter your current salary: '))

# # # print("Hello ", full_name, "your current salary is: ", incremento_value(salary))


# # x = "Full_name"
# # length = len(x)
# # nu = 50 
# # print('The length of the string \"', x, '\" is: ', length)


# # booleano = True
# # if (5 > 4) == booleano:
# #     print(type(x.upper()), type(nu.to_bytes(4,'big')), type(''), "Printed because 5 is greater than 4")


# # var1 = input("Valor a comparar 1:")
# # var2 = input("Valor a comparar 2:")

# # if (var1 > var2) and (True == True):
# #     print("El valor 1 es mayor que el valor 2")
# # else:
# #     print("El valor 2 es mayor que el valor 1")



# # age = int(input("Enter your age: "))
# # height = float(input("Enter your height in meters: "))
# # name = str(input("Enter your name: "))
# # booleanos = bool(input("Are you an student? (True/False): "))
# # no_value=''


# # if booleanos == True:
# #     yes = "You are an student."
# # else:
# #     yes = "You are not an student."

# # if len(no_value) == 0:
# #     no_value = "None"
# # else: 
# #     no_value = no_value

# # print("Your age is:", age, "and your height is:", height, "meters.",
# #       "Your name is:", name, yes, "No value here:", no_value)


# # ========================================================
# # 📘 EJERCICIOS DE STRINGS EN PYTHON
# # ========================================================

# # 🔹 1. String Values y Categorías
# # 1. Crea una variable con tu nombre completo y muéstralo en pantalla.
# variable = "Didier Acuña"
# print(variable)
# # 2. Crea tres strings diferentes: uno con comillas simples, otro con comillas dobles y otro con comillas triples.
# string1 = 'Este es el string numero 1 '
# string2 = "Este es el sting numero 2 "
# string3 = """Este es el string que me permite guardar un monton de texto y hacer 
# saltos de lineas sin problemas \n y ademas cambiar los formatos de las comillas ' \" """
# print(string1, string2, string3)



# # 🔹 2. type() y str()

# # 3. Usa type() para verificar el tipo de un número, una cadena y un booleano.
# variable1 = type(10.1)
# variable2 = type("Didier")
# variable3 = type(True)
# print(variable1, variable2, variable3)

# # 4. Convierte un número (12345) en string usando str() y verifica su tipo.
# string_num = str(101010)
# print("numero convertido a string: ",string_num," y su tipo de dato es:",type(string_num))

# # 🔹 3. len()

# # 5. Calcula la longitud de la cadena "Aprendiendo Python es divertido".
# cadena = "Aprendiendo Python es divertido"
# cadena = len(cadena)
# print('La longitud de la cadena es: ',cadena)

# # 6. Verifica cuántos caracteres tiene tu nombre.
# full_name = "Didier Acuña R"
# print('cantidad de caracteres de mi nombre:', len(full_name))


# # 🔹 4. count()
# # 7. Cuenta cuántas veces aparece la letra "a" en la frase "Las manzanas son agradables".
# frase = "Las manzanas son agradables"
# print('Las veces que aparece la palabra \" a \" en la frase, es:', frase.count('a'))
# # 8. Cuenta cuántas veces aparece la palabra "Python" en "Python es genial, Python es poderoso, Python es popular".
# frase2 = "Python es genial, Python es poderoso, Python es popular"
# print("La palabra \"Python\" aparece (",frase2.count("Python"),") veces.")


# # 🔹 5. replace()
# # 9. Reemplaza "perro" por "gato" en la cadena "Tengo un perro muy lindo".
# cadenareplace = "Tengo un perro muy lindo"
# print('El reemplazo es:',cadenareplace.replace('perro','gato'))

# # 10. Reemplaza "2024" por "2025" en la cadena "El año actual es 2024".
# ano = "El año actual es 2024"
# print('El reemplazo es: ',ano.replace('2024','2025'))

# # 🔹 6. Concatenación con + y f-string
# # 11. Crea dos variables (nombre, apellido) y únelo con +.
# nombre = "Didier"
# apellido = "Acuña"
# print("Nombre completo: " + nombre + " " + apellido)


# # 12. Repite el ejercicio usando un f-string.
# print(f"Resultado de conttenacion con f-string: {nombre} {apellido}")


# # 🔹 7. split()
# # 13. Divide la cadena "rojo,verde,azul,amarillo" en una lista de colores.
# colors= "rojo,verde,azul,amarillo"
# print(colors.split(','), str.split(colors,','))
# # 14. Divide la frase "Aprender Python paso a paso" por espacios.
# frase_a_dividir = "Aprender Python paso a paso"
# print(str.split(frase_a_dividir,'   '))

# # 🔹 8. Repetition (*)
# # 15. Imprime el string "Python " 5 veces en una sola línea.
# imprimir = "\"Python\"   " * 5
# print(imprimir)

# # 🔹 9. Indexing & Slicing
# # 16. Toma la palabra "Extracción" y muestra:
# #    - el primer carácter
# #    - los primeros 4 caracteres
# #    - los últimos 3 caracteres
# palabra = "Extracción"
# print('Primer caracter:',palabra[0])
# print('Primeros 4 caracteres:',palabra[0:3])
# print('ultimos 3 caracteres:',palabra[-3:])

# # 🔹 10. lstrip(), rstrip(), strip()
# # 17. Limpia los espacios de "   Hola Mundo   ".
# limpiar = "   Hola Mundo   "
# print('Limpiando los espacions de la frase "   Hola Mundo   "',limpiar.strip(),' ', limpiar.lstrip())
# # 18. Elimina los guiones izquierdos de "----Python" usando lstrip().

# # 🔹 11. upper() y lower()
# # 19. Convierte "python es poderoso" a mayúsculas.
# frase_mayusculas = "python es poderoso".upper()
# print('Frase en mayúsculas:', frase_mayusculas)

# # 20. Convierte "APRENDER PYTHON" a minúsculas.
# frase_minusculas = "APRENDER PYTHON".lower()
# print('Frase en minúsculas:', frase_minusculas)

# # 🔹 12. startswith(), endswith(), in
# # 21. Verifica si "Python es divertido" empieza con "Python".
# frase_starts = "Python es divertido"
# print('La frase empieza con "Python"?', frase_starts.startswith('Python'))

# print('La frase divertido', frase_starts.endswith('divertido'))

# # 22. Verifica si "Hola mundo!" termina con "!".
# frase_ends = "Hola mundo!"
# print('La frase termina con "!"?', frase_ends.endswith('!'))

# # 23. Verifica si "SQL" está dentro de "Python y SQL funcionan bien".

# frase = "Python y SQL funcionan bien"
# print('La frase contiene "SQL"?', 'SQL' in frase)

# # 🔹 13. find()
# # 24. Encuentra la posición de "Python" en "Estoy aprendiendo Python paso a paso".

# position = "Estoy aprendiendo Python paso a paso"

# print('Encontrar:',position.find('Python'))

# # 🔹 14. Validación con isalpha(), isnumeric()
# # 25. Verifica si "Python3" contiene solo letras con isalpha().
# # 26. Verifica si "2025" es numérico con isnumeric().
# print('varificacion si python3 tiene no tiene numeros: ' ,'python3'.isalpha(), '2025 es numerico?', '2025'.isnumeric())



# # ========================================================
# # 🚀 RETOS ADICIONALES
# # ========================================================

# # 🔸 Reto 1:
# # Pide al usuario que escriba una frase y muestra:
# # - El número de caracteres
# # - Cuántas veces aparece la letra "e"
# # - La frase en mayúsculas

# user_frase = str(input("Escribe una frase para aplicar los items: "))
# cant_caracter= len(user_frase)
# veces_e= user_frase.count('e')
# upper = user_frase.upper()
# print('La cantidad de caracteres es:',cant_caracter,'\n La cantidad de veces que aparece la letra e es:',veces_e,'\n La frase en mayusculas es:',upper)



# # 🔸 Reto 2:
# # Dada la frase "Aprender Python es muy divertido":
# # - Reemplaza "divertido" por "fascinante"
# # - Divide la frase en palabras y muestra la lista
# # - Verifica si la palabra "Python" está en la frase
# frase = 'Aprender Python es muy divertido'
# frase = frase.replace('divertido','fascinante')
# frase.split(',,')
# print( "Aplicando items del reto 2: ",frase,' la palabra python existe dentro? ', 'Python' in  frase )



# # 🔸 Reto 3:
# # Escribe un programa que pida al usuario su nombre y edad.
# # Luego muestra un mensaje usando f-string: 
# # "Hola [nombre], en 5 años tendrás [edad+5] años."
# nombre = str(input("Digite nombre"))
# edad = int(input("Digite edad"))

# def mostrar_f_strin(nombre,edad):
#     edad = edad + 5
#     return(f"Hola {nombre}, en 5 años tendras {edad}")


# print(mostrar_f_strin(nombre,edad))



# 🔸 Reto 4:
# Crea una cadena "   ---Python Avanzado---   "
# - Quita los espacios y guiones extras
# - Convierte todo en minúsculas
# - Muestra solo la palabra "Python"
frase = "   ---Python Avanzado---   "
frase = frase.strip()
frase = frase.replace('---','')
frase_array = frase.split()
frase = frase.lower()
inicio= int(frase.find('python'))
fin = int(len('Python'))


print(frase_array[0])
print('Extraer python:',frase[inicio:fin])
print('este print es por mostrar frase: ',frase)



# 🔸 Reto 5 (Nivel Avanzado):
# Escribe un programa que pida una palabra al usuario
# y verifique:
# - Si es alfanumérica
# - Si contiene solo letras
# - Si contiene solo números
# - Si empieza con vocal
# - Si termina con consonante
# - Si tiene más de 5 caracteres
# - Si la segunda letra es una vocal
palabra = str(input("Dame una palabra para aplicar los items"))





# global variables dumder for main method
# if __name__ == "__main__":
#     ...









# print(python_method('DIDIER'),'con una suma de', print_suma(20,4), 'años de edad;', "Double quotes here ")





  