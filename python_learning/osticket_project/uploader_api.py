import pandas
import gspread
import osticket_connection




try: 

    
    gc = gspread.service_account(filename=r'C:\Users\didier.acuna\google_api_tecno\google_api_tecno_uploader_ky.json')

    sh = gc.open(title="Osticket central view by day")
    worksheet = sh.worksheet(title="Osticket_report_1")
    #print(sh.sheet1.cell(5,2,value_render_option='FORMULA'))
    osticket_connection.ost_to_csv_generator(path=r'C:\Users\didier.acuna\git-repos\python_learning\osticket_project\result.csv')

    df_csv = pandas.read_csv(r'C:\Users\didier.acuna\git-repos\python_learning\osticket_project\result.csv',index_col=0)
    df_csv= df_csv.convert_dtypes()
    df_csv['Ticket'] =  df_csv['Ticket'].astype('string')
    df_csv=df_csv[['Ticket','Last Updated','Subject','From','Priority','Assigned To']]
    #print(df_csv.head(3))
    #print(df_csv.info())


    df_csv = df_csv.astype(str)

    df_csv = df_csv.replace(['None', 'nan', '<NA>'], '')
    df_csv= df_csv.fillna('')
     

    
    df_csv= [df_csv.columns.values.tolist()] + df_csv.values.tolist()
    #df_csv= df_csv.fillna('')


    worksheet.clear()
    worksheet.update( range_name='A1', 
        values=df_csv, 
        value_input_option='USER_ENTERED')
    





except BaseException as e: 
    print(e)