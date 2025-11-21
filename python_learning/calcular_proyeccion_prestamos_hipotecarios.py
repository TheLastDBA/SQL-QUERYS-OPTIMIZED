# Con este script de python podemos calcular la proyeccion de cuotas dado un prestamo, tasa y cantidad de meses



#: (C=P\frac{r(1+r)^{n}}{(1+r)^{n}-1}) formula del calculo de cuota mensual Inicial

import math
from pyspark.sql import SparkSession
#import conexiones


# cnx_prestamo = conexiones.conexion_tecnosoft.cursor()
# cnx_prestamo.execute('select * from catalogo.acciones;')

# resultado = cnx_prestamo.fetchall()
# resultado_lista_padre = []
# resultado_lista_hijo = []


# print(resultado)


# for i in range(len(resultado)):
#     print(i)
#     for x in resultado[i]:
#         resultado_lista_hijo.append(x)
#     resultado_lista_padre.append(resultado_lista_hijo)
#     print(resultado_lista_padre)
        



# for fila in resultado:
#     resultado_lista_hijo = []
#     for valor in fila:
#         resultado_lista_hijo.append(valor)
#     resultado_lista_padre.append(resultado_lista_hijo)

# print(resultado_lista_padre)

   
    


def calcular_proyeccion_prestamo(monto_x,tasa_x,numero_años_x,ver_proyeccion):
    
    monto = monto_x #int(input('Digite el monto a financiar: ')) #Monto principal del prestamo (P)
    tasa =  tasa_x #int(input('Digite la tasa de su credito: ')) #Tasa de interes periodica mensual (r)
    tasa_year = tasa
    numero_meses = numero_años_x  #int(input('Digite a cuantos años esta su credito: ')) #numero total de años (n)

    tasa = round(((tasa / 12) /100),4) #Calculamos la tasa mensual
    numero_meses = (numero_meses * 12)

    cuota =  round( (monto * (tasa * ((1+tasa)**numero_meses) / (((1+tasa)**numero_meses) -1)) ) , 2 ) #Calculo de cuota fija

    print(f' Credito: ${monto} Millones \n Tasa anualizada: {tasa_year}% (mes:{tasa}% ) \n Numero_meses: {numero_meses} \n Cuota: ${cuota}')
    intereses_pagados_x_anos = 0
    if ver_proyeccion == True:
        
        #Calculo de proyeccion de pagos del credito dado cantidad de meses
        interes_a_pagar = (monto * tasa)
        Amortizacion = cuota - interes_a_pagar
        saldo_final = monto - Amortizacion

        for i  in range(numero_meses):
            interes_a_pagar = (saldo_final * tasa)
            Amortizacion = cuota - interes_a_pagar
            saldo_final = saldo_final - Amortizacion
            intereses_pagados_x_anos = interes_a_pagar + intereses_pagados_x_anos
            print(f'Mes {i} | Cuota: {round(cuota,2)} | Abono a interes: {round(interes_a_pagar,2)} | Abono a capital: {round(Amortizacion,2)} | Saldo final: {round(saldo_final,2)} ')
        else:
            return f'interes pagados totales: {round(intereses_pagados_x_anos,2)}'
    else:
        return f'Fin'    


#print(calcular_proyeccion_prestamo(33000000,16.33,6,True))


print(calcular_proyeccion_prestamo(100000000,10,20,True))








