import mysql.connector as cnx_osticket
from mysql.connector import errors
import dotenv
from os import getenv
import pandas
import gspread

# gs_cnx =gspread.service_account(filename=r'C:\Users\didier.acuna\google_api_tecno\google_api_tecno_uploader_ky.json')
# sh = gs_cnx.open(title="Osticket central view by day")
# worksheet = sh.worksheet(title="Osticket_report_1")

def ost_to_csv_generator(path:str):
    
    try:
        #path = ''
        dotenv.load_dotenv(dotenv_path=r'C:\Users\didier.acuna\git-repos\python_learning\osticket_project\osticket.env')
        

        connection_osticket =  cnx_osticket.connect(user=getenv('ost_user'),
                                                    port=getenv("ost_port"), 
                                                    password=getenv("ost_password"), 
                                                    host = getenv("ost_host"),
                                                    database=getenv('ost_database'))  

        query_my = connection_osticket.cursor(dictionary=True,buffered=True) 
        query_text = " SELECT ost_ticket.`Ticket`, ost_ticket.`Last Updated`, ost_ticket.`Subject`, ost_ticket.`From`, ost_ticket.`Priority`, CASE WHEN ost_ticket.staff_id = 0 THEN ost_team.name ELSE CONCAT(ost_staff.username, ' ', ost_staff.firstname, ' ', ost_staff.lastname) END AS `Assigned To` FROM (SELECT ost_ticket.number AS `Ticket`, ost_ticket.lastupdate AS `Last Updated`, ost_ticket__cdata.subject AS `Subject`, ost_user.name AS `From`, osticket_db.ost_ticket_priority.priority AS `Priority`, ost_ticket.staff_id, ost_ticket.team_id FROM ost_thread INNER JOIN ost_ticket ON ost_thread.object_id = ost_ticket.ticket_id INNER JOIN ost_user ON ost_user.id = ost_ticket.user_id INNER JOIN ost_ticket__cdata ON ost_ticket.ticket_id = ost_ticket__cdata.ticket_id INNER JOIN osticket_db.ost_ticket_priority ON osticket_db.ost_ticket_priority.priority_id = ost_ticket__cdata.priority INNER JOIN ost_thread_entry ON ost_thread_entry.thread_id = ost_thread.id WHERE ost_thread_entry.user_id != 0 and ost_ticket.created > date_sub(now() , interval 1 day)  ) AS ost_ticket LEFT JOIN ost_staff ON ost_staff.staff_id = ost_ticket.staff_id LEFT JOIN ost_team ON ost_team.team_id = ost_ticket.team_id order by ost_ticket.`Last Updated` desc "
        query_my.execute(query_text)
        query_result=query_my.fetchall()
        # list_new_sheet = []
        # for  i in query_result:
        #     list_new_sheet.append(list(i))

        # worksheet.update(list_new_sheet)

        
            

        
            
        #print(query_result)

        df_ost = pandas.DataFrame(query_result)
        df_ost = df_ost.astype(str)

        df_ost = df_ost.replace(['None', 'nan', '<NA>'], '')
        df_ost.to_csv(header=True,path_or_buf=path)
        return "Finish"
        

    except BaseException as e:
        print(e)

path = r'C:\Users\didier.acuna\git-repos\python_learning\osticket_project\result_1.csv'
print(ost_to_csv_generator(path=path))








