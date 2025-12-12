from pyspark.sql import SparkSession
from datetime import datetime, date
import pandas as pd
from pyspark.sql import Row






try: 
    spark = SparkSession.builder.getOrCreate()

    df = spark.createDataFrame([
    Row(a=1, b=2., c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
    Row(a=2, b=3., c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
    Row(a=4, b=5., c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))
    ])
    df.show()

    
        
    # # Ruta al archivo de configuración
    # path_config = r'C:\Users\didier.acuna\git-repos\python_learning\Spark\spark.configs.json'

    # # Cargar configuraciones desde JSON
    # with open(path_config, 'r', encoding='utf-8') as jsonfile:
    #     json_path_config = json.load(jsonfile)
    #     print('Parámetros de configuración Spark cargados:', json_path_config)

    # # Crear configuración
    # config = SparkConf().setAll(json_path_config.items())

    # # Crear SparkSession
    # session = (SparkSession.builder
    #         .config(conf=config)
    #         .appName('SparkSataSession')
    #         .master("local[*]")
    #         .getOrCreate())

    # #  Crear DataFrame correcto desde tu dict
    # diccionario_names = ['Didier','Roberto', 'Acuña']

    # df = session.createDataFrame([
    #     (1, 2., 'string1', date(2000, 1, 1), datetime(2000, 1, 1, 12, 0)),
    #     (2, 3., 'string2', date(2000, 2, 1), datetime(2000, 1, 2, 12, 0)),
    #     (3, 4., 'string3', date(2000, 3, 1), datetime(2000, 1, 3, 12, 0))
    # ], schema='a long, b double, c string, d date, e timestamp')
    # df.show()   

    # session.stop()


except BaseException as e: 
    print(e)
