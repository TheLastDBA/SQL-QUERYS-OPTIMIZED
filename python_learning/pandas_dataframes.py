import pandas 

try: 
    filter_regions = ['Albany'] #,'WestTexNewMexico','Chicago','Atlanta'
    df_avocado = pandas.read_csv('data_sets/avocado.csv')
    df_avocado.insert(14,'TrustData',True)
    df_avocado = df_avocado.drop('4225',axis=1)
    df_avocado = df_avocado[df_avocado['region'].isin(filter_regions)]
    

    print(df_avocado)

except Exception as error: 
    print(error)