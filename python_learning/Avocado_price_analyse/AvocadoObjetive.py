import pandas
import matplotlib.pyplot as plotlib
import os 
import kagglehub


#path_to_trmfile = kagglehub.dataset_download("alonsocopete/trm-dolar-cop-colombia")

#print("Path to dataset files:", path_to_trmfile)
# Objetivo general: Analizar cómo ha variado el precio promedio del aguacate en distintas regiones y 
# tipos (“conventional” vs “organic”), encontrar tendencias y
#  preparar los datos para análisis futuros en PySpark.

try:

    #Cargue y exploracion de datos
    avoacado_df = pandas.read_csv(r'C:\Users\didier.acuna\git-repos\python_learning\data_sets\avocado.csv')
    avoacado_df = avoacado_df#.head(10)
    #Cargue de precios usd / cop por dia
    trm_df = pandas.read_csv(r'C:\Users\didier.acuna\git-repos\python_learning\data_sets\TRM.csv',index_col=False)
    trm_df=trm_df.rename(columns={'VALOR':'Precio', 'VIGENCIADESDE':'Date', 'VIGENCIAHASTA':'Dia cierre'})
    trm_df['Date'] = pandas.to_datetime(trm_df['Date'],format='mixed')
    trm_df['Dia cierre'] = pandas.to_datetime(trm_df['Dia cierre'],format='mixed')
    

    

   

    #Droping unused columns modifying the original df
    avoacado_df.drop('Unnamed: 0',axis=1,inplace=True)

    #Changing data type for column date, to be more specific
    avoacado_df['Date'] = pandas.to_datetime(avoacado_df['Date'],errors='coerce')
    #Avocado analyze and trm $COP prices per day, merging dfs to get prices per date
    avoacado_df = pandas.merge(avoacado_df,trm_df,how='inner',on='Date')
    
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
    avoacado_df.insert(loc=13,column='PricePerBags', value=(  avoacado_df['Total Volume'] / avoacado_df['AveragePrice'] ).round())
    
    
    df_prices_trm_avocado = avoacado_df[['Date','AveragePrice','Total Volume','4046','4225','4770','type','region','Precio']]
    df_prices_trm_avocado.reset_index()
    #avoacado_df['PricePerBags'] = avoacado_df['PricePerBags'].round()
    #Mean price
    mean_result_df = avoacado_df['AveragePrice'].mean()
    #filtering by Albany and organic and retriving proces over the mean
    albany_filter_df = avoacado_df[(avoacado_df['region'] == 'Albany') & (avoacado_df['type'] == 'organic') & (avoacado_df['AveragePrice'] > mean_result_df)]
    #Calcula el precio promedio por año y tipo.
    albany_filter_df_groupby_yeartype=albany_filter_df.groupby(by=['year','type'],as_index=False)['AveragePrice'].mean()
    #Calcula el volumen total por región y año.
    total_volumne_per_regionadnyear = avoacado_df.groupby(by=['region','year'],as_index=False)['Total Volume'].sum().sort_values(by='Total Volume',ascending=False)
    total_volume = pandas.DataFrame(total_volumne_per_regionadnyear)
    # Creating personalized dataframe for calculate average price , grouping per each yearand region
    df_average_price_per_region = avoacado_df[['AveragePrice','region','year']].sort_values(by=['year','region']).groupby(by=['region','year'])['AveragePrice'].mean()
    


    #Comparin in matplotlib
   # total_volumne_per_regionadnyear.plot()
    #plotlib.show()

    #Albany result CSV
    albany_filter_df.to_csv(r'C:\Users\didier.acuna\git-repos\python_learning\Avocado_price_analyse\Avocado Reports Result\Albany_result.csv',index='yes')
    total_volume.to_excel(r'C:\Users\didier.acuna\git-repos\python_learning\Avocado_price_analyse\Avocado Reports Result\total_volume.xlsx',sheet_name='Volumen total por region X ano')
    df_prices_trm_avocado.to_excel(r'C:\Users\didier.acuna\git-repos\python_learning\Avocado_price_analyse\Avocado Reports Result\Avocado_Cop_Prices.xlsx',sheet_name='Full reports per cops')
    df_full_report = pandas.merge(avoacado_df,total_volume,how='inner',on='year')
    df_full_report.merge(albany_filter_df_groupby_yeartype,how='inner',on='year')

    with pandas.ExcelWriter(r"C:\Users\didier.acuna\git-repos\python_learning\Avocado_price_analyse\Avocado Reports Result\total_volume.xlsx",     mode="a",engine="openpyxl", if_sheet_exists="overlay") as writer:
        total_volumne_per_regionadnyear_df_excel = pandas.DataFrame(total_volumne_per_regionadnyear)
        total_volumne_per_regionadnyear_df_excel.to_excel(writer,sheet_name='Volumen total por año')
    
    

    

    

    
    
    

    
    #Visualize data frame information, for exploring data
    #typeofdata = avoacado_df.dtypes
    #avoacado_df_info = avoacado_df.info()
    #print(avoacado_df.dtypes, '|', avoacado_df_info)
    #trm_df[trm_df['Date'] == '2015-01-04']

    

    print(df_prices_trm_avocado)
    

    
except Exception as error: 
    print(error)