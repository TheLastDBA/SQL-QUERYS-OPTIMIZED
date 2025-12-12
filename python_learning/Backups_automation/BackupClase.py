import os
from dotenv import load_dotenv
import subprocess
import connections_db as db
#comment
load_dotenv(
    dotenv_path=r"C:\Users\didier.acuna\git-repos\python_learning\Backups_automation\.env")


class Backups_auto:
    def __init__(self, ip_destination: str,
                 port_destination: str,
                 login_user_destination: str,
                 name_db_backup: str,
                 password_destination: str,
                 destination_db_name: str,
                 server: str
                 ):
        self.ip_origin_synergy = os.getenv("synergy_ip")
        self.ip_origin_balancetecno = os.getenv("ifrs_ip")
        self.prd_password = os.getenv("prd_password")
        self.prd_user = os.getenv("prd_user")
        self.global_port = os.getenv("prd_port_synergy")
        self.name_db_backup = name_db_backup
        self.ip_destination = ip_destination
        self.port_destination = port_destination
        self.login_user_destination = login_user_destination
        self.password_destination = password_destination
        self.destination_db_name = destination_db_name
        self.server = server

    def backup_maker(self):
        try:
            exists_db = db.exists_bd(self.name_db_backup, self.server)
            if exists_db == True:
                pgpassconf = self.ip_destination+':' + self.port_destination+':' + \
                    '*'+':'+self.login_user_destination+':' + self.password_destination
                self.destination_db_name = self.destination_db_name.lower()
                # Define Dir to allocate  backups
                dir_backup = r'D:/Backups_devs/'+self.destination_db_name+'.dump'

                # Validate server source (Company validation), if you want, ignore it and comment.
                if (self.server == 60):
                    self.ip_origin_synergy = self.ip_origin_balancetecno

                with open(r"C:\Users\didier.acuna\AppData\Roaming\postgresql\pgpass.conf", '+a') as pgpass_file:
                    pgpass_file.write('\n'+pgpassconf)

                psql_command = ["psql", f"-h{self.ip_destination}", f"-U{self.login_user_destination}",
                                f"-p{self.port_destination}", f"--command=  create database {self.destination_db_name} ;"]
                pgdump_command_synergy = ["pg_dump", f"--host={self.ip_origin_synergy}", f"--port={self.global_port}",
                                          f"--username={self.prd_user}",  f"--dbname={self.name_db_backup}", "-O", "-x", "--verbose", "--format=c", f"--file={dir_backup}"]
                pg_restore_command = ["pg_restore", f"--host={self.ip_destination}", f"--username={self.login_user_destination}",
                                      f"--port={self.port_destination}",  f"--dbname={self.destination_db_name}", "--verbose", f"{dir_backup}"]

                subprocess.run(pgdump_command_synergy, check=True)
                subprocess.run(psql_command, check=True)
                subprocess.run(pg_restore_command, check=True)
                return f"Production source DB: {self.name_db_backup} | From host:{self.ip_origin_synergy} \nFinal destination name: {self.destination_db_name} | To host: {self.ip_destination}"
            else:

                print( f"La base de datos no existe en el server designado, por favor validar origen de la base de datos.")

            
        except Exception as error:
            print(error)


backup = Backups_auto(ip_destination="10.1.132.74",
                      port_destination="5433",
                      login_user_destination="postgres",
                      name_db_backup="aulaVirtual",
                      password_destination="123456",
                      destination_db_name="aulaVirtual_backup_2",
                      server=60)

print(backup.backup_maker())
