# this is a comment in my python language, so this line would be ignored by the py engine

nombre = "Didier"

def python_method(nombre):
    response = 'Hola mundo, soy '+ '\" ' + nombre + ' \" '+ ' y \n esto es \n \n \n python.'
    return response


def print_suma(valor1,valor2):
    sumar = valor1 + valor2
    return sumar

def invocar_methods():
    print(python_method('DIDIER'), '\n', 'con una suma de', print_suma(20,4), 'años de edad;', "Double quotes here ")
#Fin methods

invocar_methods() # Ultima linea de codigo comentada que invoca a la funcion

print('Your learning path:\n\t-Python Basics \n\t-Data Engineering \n\t-AI')

print('Este es un salto de \n linea')
print('Este es un backslash \\ para ignorar reserved values')
print('Este es un reserved value para printear una felcha \\t')
print('Este es un \"""(triple quote) para escribir en bloque:', """ \nasi: \n 
'-> para escribir a merced \n
'-> y que no haya errores. """)

comodin ='datawithdidier.com'
print('info@'+comodin)
print('support@'+comodin)
print('www.'+comodin)






# print(python_method('DIDIER'),'con una suma de', print_suma(20,4), 'años de edad;', "Double quotes here ")



  