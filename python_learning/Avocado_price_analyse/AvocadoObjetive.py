import pandas
import matplotlib.pyplot as plotlib

# Objetivo general: Analizar cómo ha variado el precio promedio del aguacate en distintas regiones y 
# tipos (“conventional” vs “organic”), encontrar tendencias y
#  preparar los datos para análisis futuros en PySpark.

try:

    #Cargue y exploracion de datos
    avoacado_df = pandas.read_csv(r'C:\Users\didier.acuna\git-repos\python_learning\data_sets\avocado.csv')
    avoacado_df = avoacado_df#.head(10)
    

   

    #Droping unused columns modifying the original df
    avoacado_df.drop('Unnamed: 0',axis=1,inplace=True)

    #Changing data type for column date, to be more specific
    avoacado_df['Date'] = pandas.to_datetime(avoacado_df['Date'],errors='coerce')
    
    #Change data types for columns 4046,4225,4770 to int
    #First cleaning the data
    avoacado_df['4046'] = pandas.to_numeric(avoacado_df['4046'],errors='coerce')
    avoacado_df['4225'] = pandas.to_numeric(avoacado_df['4225'], errors='coerce')
    avoacado_df['4770'] = pandas.to_numeric(avoacado_df['4770'], errors='coerce')
    #Modifying to Columns to int
    avoacado_df['4046'] = avoacado_df['4046'].astype(int)
    avoacado_df['4225'] = avoacado_df['4225'].astype(int)
    avoacado_df['4770'] = avoacado_df['4770'].astype(int)
    avoacado_df['Total Bags'] = avoacado_df['Total Bags'].round().astype(int)
    avoacado_df[['Large Bags','Total Volume','Small Bags','XLarge Bags']]=avoacado_df[['Large Bags','Total Volume','Small Bags','XLarge Bags']].round().astype(int)
    avoacado_df = avoacado_df.sort_values(by='Date',ascending=True)
    #Adding new column PricePerBags
    avoacado_df.insert(loc=13,column='PricePerBags', value=(avoacado_df['AveragePrice'] / avoacado_df['Total Volume']))
    #Mean price
    mean_result_df = avoacado_df['AveragePrice'].mean()
    #filtering by Albany and organic and retriving proces over the mean
    albany_filter_df = avoacado_df[(avoacado_df['region'] == 'Albany') & (avoacado_df['type'] == 'organic') & (avoacado_df['AveragePrice'] > mean_result_df)]
    #Calcula el precio promedio por año y tipo.
    albany_filter_df_groupby_yeartype=albany_filter_df.groupby(by=['year','type'],as_index=False)['AveragePrice'].mean()
    #Calcula el volumen total por región y año.
    total_volumne_per_regionadnyear = avoacado_df.groupby(by=['region','year'],as_index=False)['Total Volume'].sum().sort_values(by='Total Volume',ascending=False)
    #Comparin in matplotlib
    total_volumne_per_regionadnyear.plot()
    plotlib.show()

    

    
    
    

    
    #Visualize data frame information, for exploring data
    #typeofdata = avoacado_df.dtypes
    #avoacado_df_info = avoacado_df.info()
    #print(avoacado_df.dtypes, '|', avoacado_df_info)

    

    print(total_volumne_per_regionadnyear)
    

    
except Exception as error: 
    print(error)