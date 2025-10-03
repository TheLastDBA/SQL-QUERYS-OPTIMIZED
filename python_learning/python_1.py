import random as ran
import math as ma

# #this is a comment in my python language, so this line would be ignored by the py engine

# nombre = "Didier"

# def python_method(nombre):
#     response = 'Hola mundo, soy '+ '\" ' + nombre + ' \" '+ ' y \n esto es \n \n \n python.'
#     return response


# def print_suma(valor1,valor2):
#     sumar = valor1 + valor2
#     return sumar

# def invocar_methods():
#     print(python_method('DIDIER'), '\n', 'con una suma de', print_suma(20,4), 'años de edad;', "Double quotes here ")
# #Fin methods

# invocar_methods() # Ultima linea de codigo comentada que invoca a la funcion

# print('Your learning path:\n\t-Python Basics \n\t-Data Engineering \n\t-AI')

# print('Este es un salto de \n linea')
# print('Este es un backslash \\ para ignorar reserved values')
# print('Este es un reserved value para printear una felcha \\t')
# print('Este es un \"""(triple quote) para escribir en bloque:', """ \nasi: \n 
# '-> para escribir a merced \n
# '-> y que no haya errores. """)

# comodin ='datawithdidier.com'
# print('info@'+comodin)
# print('support@'+comodin)
# print('www.'+comodin)


# def incremento_value(x):
#     inc = 0.18 
#     x = x +(x*inc)
#     return x

# # #full_name = input('Enter your full name: ')
# # salary = int(input('Enter your current salary: '))

# # print("Hello ", full_name, "your current salary is: ", incremento_value(salary))


# x = "Full_name"
# length = len(x)
# nu = 50 
# print('The length of the string \"', x, '\" is: ', length)


# booleano = True
# if (5 > 4) == booleano:
#     print(type(x.upper()), type(nu.to_bytes(4,'big')), type(''), "Printed because 5 is greater than 4")


# var1 = input("Valor a comparar 1:")
# var2 = input("Valor a comparar 2:")

# if (var1 > var2) and (True == True):
#     print("El valor 1 es mayor que el valor 2")
# else:
#     print("El valor 2 es mayor que el valor 1")



# age = int(input("Enter your age: "))
# height = float(input("Enter your height in meters: "))
# name = str(input("Enter your name: "))
# booleanos = bool(input("Are you an student? (True/False): "))
# no_value=''


# if booleanos == True:
#     yes = "You are an student."
# else:
#     yes = "You are not an student."

# if len(no_value) == 0:
#     no_value = "None"
# else: 
#     no_value = no_value

# print("Your age is:", age, "and your height is:", height, "meters.",
#       "Your name is:", name, yes, "No value here:", no_value)


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



# # 🔸 Reto 4:
# # Crea una cadena "   ---Python Avanzado---   "
# # - Quita los espacios y guiones extras
# # - Convierte todo en minúsculas
# # - Muestra solo la palabra "Python"
# frase = "   ---Python Avanzado---   "
# frase = frase.strip()
# frase = frase.replace('---','')
# frase_array = frase.split()
# frase = frase.lower()
# inicio= int(frase.find('python'))
# fin = int(len('Python'))


# print(frase_array[0])
# print('Extraer python:',frase[inicio:fin])
# print('este print es por mostrar frase: ',frase)



# # 🔸 Reto 5 (Nivel Avanzado):
# # Escribe un programa que pida una palabra al usuario
# # y verifique:
# # - Si es alfanumérica
# # - Si contiene solo letras
# # - Si contiene solo números
# # - Si empieza con vocal
# # - Si termina con consonante
# # - Si tiene más de 5 caracteres
# # - Si el segundo de una cadena es vocal

# palabra = str(input("Dame una palabra para aplicar los items: "))


# def validador_str(palabras):
#     alfanumerica = palabras.isalnum() #Saber si es alfanumerica
#     letras = palabras.isalpha() #Saber si es solo letras
#     numeros = palabras.isnumeric() #Saber si es numerico
#     if palabras[0]  in 'aeiouAEIOU': #Validacion si el principio de una cadena es vocal
#         vocal = True
#     else:
#         vocal = False 
    
#     if palabras[-1] not in 'aeiouAEIOU':
#         consonante = True 
#     else:
#         consonante = False

#     if len(palabras) > 5:
#         length = True
#     else:
#         length = False

#     if palabras[1]  in 'aeiouAEIOU': #Validacion si el segundo de una cadena es vocal
#         segund_vocal = True
#     else:
#         segund_vocal = False 
    
#     resultado = f"""¿alfanumerico? {alfanumerica}, ¿contiene solo letras? {letras}, ¿contiene solo numeros? {numeros}, ¿Empieza con vocal? {vocal}, 
#     ¿Termina en consonante? {consonante}, ¿Tiene mas de 5 caracteres? {length}, ¿la segunda letra es una vocal? {segund_vocal}"""
#     return print(resultado)

# print(validador_str(palabra))



# ########################################################################################################################################################################
# #NUMBERS

# # 🔢 Ejercicios de Números en Python
# # 1. Tipos de Números

# # Crea tres variables: un entero, un flotante y un complejo.
# # Imprime cada uno junto con su tipo.
# a = 1
# b = 1.1
# c = 1j
# print(type(a),type(b),type(c))


# # 2. Conversión de Tipos

# # Convierte el número decimal 7.9 a entero y a complejo.

# # Convierte el número 12 en flotante y en complejo.

# a,b=7.9,12
# def convert_to(enterComplex,floatComplex):
#     entero = int(enterComplex)
#     complejo = complex(enterComplex)
#     floatnum = float(floatComplex)
#     seComplex = complex(floatComplex)
#     return f"{entero}, {complejo}, {floatnum}, {seComplex}"


# print(convert_to(a,b))


# # 3. Operadores Matemáticos

# # Escribe un programa que reciba dos números e imprima:

# # La suma

# # La resta

# # La multiplicación

# # La división entera

# # El módulo (residuo)

# # La potencia

# def arimetic_aplicator(a,b):
#     suma = a+b
#     resta = a-b
#     multiplicacion = a*b
#     division_entera = a//b
#     mod = a%2
#     potecni = a**b
#     print(suma,resta,multiplicacion,division_entera,mod,potecni)

# print(arimetic_aplicator(a,b))


# # 4. Redondeo

# # Toma el número 23.6789 y:

# # Redondea a 2 decimales.

# # Redondea al entero más cercano.

# # Usa math.floor() y math.ceil().

# num = 23.6789

# print(round(num,2), round(num),ma.floor(num),ma.ceil(num))



# # 5. Números Aleatorios

# # Genera un número aleatorio entre 1 y 50.

# # Simula lanzar un dado 10 veces y guarda los resultados en una lista.

# # Selecciona aleatoriamente un nombre de la lista ["Ana", "Luis", "Pedro", "Sofía"] 10 veces y guaradalos en una lista .


# random=ran.randint(1,50)
# lista = []
# nombres = ["Ana", "Luis", "Pedro", "Sofía"]
# resultado_nombres = []
# def exercise_5():
#     for i in range(10):
#         value = ran.randint(50,1000)
#         lista.append(value)
#         result= ran.choice(nombres)
#         resultado_nombres.append(result)
#         print('usuario escogido en el ciclo #',i,'es: ',result)
#     print('Lista resultante de guardar numeros aleatorios 10 veces: ',lista,'\nLista resultante de escoger nombres aleatorios: ', resultado_nombres)

# print(exercise_5())




# # 6. Validación

# # Escribe una función es_numero(cadena) que retorne True si la cadena es un número válido, y False en caso contrario.

# # Ejemplo: "123" → True

# # "12.5" → True

# # "hola" → False

# cadena = input("Ingrese una cadena: ")
# def es_numero(cadena): 
#     if cadena.isnumeric() == True:
#         return True
#     else:
#         return False

# print('Result: ',es_numero(cadena))






# # 7. Reto Final 🚀

# # Haz un juego de adivinanza de números:

# # Genera un número secreto entre 1 y 100.

# # El usuario debe adivinarlo.

# # Si el número es menor, muestra “El número es mayor”.

# # Si es mayor, muestra “El número es menor”.

# # Cuando acierte, muestra el número de intentos que tomó.





# def guess_secret_number():
#     secret_number = ran.randint(1,100)
#     a = True
#     intentos = 0
#     print('Adivina el numero que pense')
#     user_number = input("¿Que numero pense?")

#     if user_number.isnumeric() == True:
#         user_number = int(user_number)
#         while a == True:
#             intentos +=1
#             if user_number == secret_number:
#                 print('Adivinaste el numero, con una cantidad de intentos de: ',intentos)
#                 a = False
#             elif user_number > secret_number:
#                 user_number = input("Mi numero es menor, ¿Intenta de nuevo -_-?")
#                 if user_number.isnumeric() == True:
#                     user_number = int(user_number)
#                 else:
#                     print("Regla infringida: INGRESAR UN VALOR NO NUMERICO | Castigo: pierdes.")
#                     break    
#             elif user_number < secret_number:
#                 user_number = input("Mi numero es mayor, ¿Intenta de nuevo -_-?")
#                 if user_number.isnumeric() == True:
#                     user_number = int(user_number)
#                 else:
#                     print("Regla infringida: INGRESAR UN VALOR NO NUMERICO | Castigo: pierdes.")
#                     break                  
#     else:
#         return 'No digitaste un numero valido, debe ser un entero o sera redondeado al mas cercano'
    
#     return "Exitos :')"

# print(guess_secret_number())



#SOME CONTROL FLOW 
print(bool(None))
print(bool(''))
print(bool('true'))

lista_vacia = [False,False]
lista_llena = ["llena",'1','2']
lista_incompleta = ["1",'uncommitted',False]

print(all(lista_vacia))
print(all(lista_llena))
print(all(lista_incompleta))


print(any(lista_vacia))
print(any(lista_llena))
print(any(lista_incompleta))

a = 10
b = 10.1
c = 'gaga'
print(c.count('a'))

print(isinstance(a,(str,int,float)), isinstance(c,(str)),isinstance(b,int))















# global variables dumder for main method
# if __name__ == "__main__":
#     ...

# print(python_method('DIDIER'),'con una suma de', print_suma(20,4), 'años de edad;', "Double quotes here ")





  