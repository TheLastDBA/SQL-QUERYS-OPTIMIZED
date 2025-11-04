import pandas 

productos_columns = ['nombre','precio','tamaño','cantidad']
producto1 = ['Shampoo elizabeth',16000,'1000ml','100']
producto2 = ['Acondicionador Aurora', 18500, '900ml', '80']
producto3 = ['Crema Corporal Zen', 22000, '500ml', '120']
producto4 = ['Jabón Natural Lavanda', 9500, '250g', '200']
producto5 = ['Aceite Capilar Brillo', 27000, '150ml', '60']
producto6 = ['Gel Facial Purificante', 19500, '200ml', '90']
producto7 = ['Loción Refrescante Citrus', 17500, '400ml', '70']
producto8 = ['Mascarilla Hidratante', 24500, '300ml', '110']
producto9 = ['Perfume Aurora Boreal', 56000, '100ml', '50']
producto10 =['Tónico Capilar Vital', 21000, '250ml', '85']



products_list = [producto1,producto2,producto3,producto4,producto5,producto6,producto7,producto8,producto9,producto10]





df = pandas.DataFrame(products_list,columns=productos_columns)

#print('Resultdo 1: \n',df)




nombres = [
    'Shampoo elizabeth',
    'Acondicionador suave',
    'Crema capilar',
    'Gel fijador',
    'Aceite nutritivo'
]

precios = [16000, 18000, 25000, 15000, 22000]

tamaños = ['1000ml', '900ml', '500ml', '300ml', '150ml']

cantidades = [100, 80, 50, 60, 40]

listas_productos = zip(nombres,precios,tamaños,cantidades)

df = pandas.DataFrame(list(listas_productos),columns=['nombre','precio','tamaño','cantidad'])
print(df)

data_diccionario = {'nombre': nombres,'precio':precios, 'tamaño': tamaños , 'cantidad':cantidades}


df = pandas.DataFrame(data_diccionario)
df = df.assign(precio_duplicado = precios)
df['cantidad_duplicada'] = cantidades

df.insert(5,'columna_name',tamaños)
print('\n', df)


# df = pandas.read_csv(r"C:\Users\didier.acuna\Downloads\hts_2025_revision_25_csv.csv")

# print('\n',df.head(10))
