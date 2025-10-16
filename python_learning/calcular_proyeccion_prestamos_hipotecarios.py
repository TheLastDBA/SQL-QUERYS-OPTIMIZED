# Con este script de python podemos calcular la proyeccion de cuotas dado un prestamo, tasa y cantidad de meses



#: (C=P\frac{r(1+r)^{n}}{(1+r)^{n}-1}) formula del calculo de cuota mensual Inicial
import math 

monto = int(input('Digite el monto a financiar: ')) #Monto principal del prestamo (P)
tasa = int(input('Digite la tasa de su credito: ')) #Tasa de interes periodica mensual (r)
tasa_year = tasa
numero_meses = int(input('Digite a cuantos años esta su credito: ')) #numero total de años (n)

tasa = round(((tasa / 12) /100),4) #Calculamos la tasa mensual
numero_meses = (numero_meses * 12)


cuota =  round( (monto * (tasa * ((1+tasa)**numero_meses) / (((1+tasa)**numero_meses) -1)) ) , 2 )
print(f' Credito: ${monto} Millones \n tasa anualizada: {tasa_year}% (mes:{tasa}% ) \n numero_meses: {numero_meses} \n cuota: ${cuota}')


