import pandas
import numpy
from matplotlib import pyplot
import kagglehub
import time

try:
    timer = time.process_time()

    print('all working')


    df = pandas.read_csv(r'C:\Users\didier.acuna\git-repos\python_learning\data_sets\avocado.csv',index_col=1)

#Select all about Chicago Region
    chicago_df = df[df['region'] == 'Chicago']
#Order by Date
    chicago_df = chicago_df.sort_values(by='Date',ascending=True)
    #print(chicago_df.head(10))
#Visualiza en un grafico todos los precios medio de cada dia
    # df_precios = chicago_df['AveragePrice'][:20]
    # pyplot.plot(df_precios)
    # pyplot.title('Precios Aguacates')
    # pyplot.xlabel('Fecha')
    # pyplot.xticks(rotation=90)
    # pyplot.ylabel('USD')
    # pyplot.show()

    df = pandas.read_csv(r'C:\Users\didier.acuna\git-repos\python_learning\data_sets\avocado.csv',index_col=0)
    df = df[(df['region'] == 'Albany') & (df['Total Volume'] > 50000)][30:47]
    df = df.sort_values(by='Total Volume', ascending=False)

    df_atlanta = pandas.read_csv(r'data_sets/avocado.csv')
    df_atlanta = df_atlanta.sort_values(by='AveragePrice',ascending=False)
    df_atlanta = df_atlanta[df_atlanta['region'] == 'Atlanta'][0:10]
    df_atlanta = df_atlanta[['Date','AveragePrice','Total Volume','region']]
    df_atlanta.insert(3,'Nuevo',1)
    df_atlanta['Nueva_col2'] = 1
    df_atlanta = df_atlanta.assign(nuevacol3 = 1)
    df_atlanta['Precio X VolumenTotal'] = (df_atlanta['AveragePrice'] * df_atlanta['Total Volume'])
    #df_atlanta = df_atlanta[(df_atlanta['Precio X VolumenTotal'] == 37283.3450)]
    df_atlanta= df_atlanta.drop('nuevacol3',axis=1)
    df_atlanta = df_atlanta[df_atlanta['AveragePrice'].isin([2.59,2.23,2.56])]
    #df_atlanta = df_atlanta[['AveragePrice']]

    
    print(df_atlanta)
    print(f'\n {timer}')



except Exception as error:
    print(error)
    








