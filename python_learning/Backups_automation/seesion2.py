import BackupClase
import dotenv
from os import getenv
dotenv.load_dotenv(dotenv_path=r"C:\Users\didier.acuna\git-repos\python_learning\Backups_automation\.env")

# #Carlos visbal
# backup = BackupClase.Backups_auto(ip_destination="10.0.64.238",
#                       port_destination="5432",
#                       login_user_destination="postgres",
#                       name_db_backup="services_web_api",
#                       password_destination=getenv("car_pwd"),
#                       destination_db_name="services_web_api_15122025",
#                       server=215)

# print(backup.backup_maker())



#Ariel Perez
backup = BackupClase.Backups_auto(ip_destination="10.1.132.74",
                      port_destination="5433",
                      login_user_destination="postgres",
                      name_db_backup="talento_humano",
                      password_destination=getenv("ari_pwd"),
                      destination_db_name="talento_humano_28012026",
                      server=215)

print(backup.backup_maker())


#Manuel Rodriguez
# backup = BackupClase.Backups_auto(ip_destination="110.1.135.153",
#                       port_destination="5432",
#                       login_user_destination="manuel",
#                       name_db_backup="access_control",
#                       password_destination=getenv("man_pwd"),
#                       destination_db_name="access_control_15122025_1",
#                       server=215)

# print(backup.backup_maker())



# #.164
# backup = BackupClase.Backups_auto(ip_destination="10.1.2.164",
#                       port_destination="5432",
#                       login_user_destination="didier.acuna",
#                       name_db_backup="services_web_api",
#                       password_destination=getenv("pwd_164"),
#                       destination_db_name="service_web_api_16_12_2025",
#                       server=215)

# print(backup.backup_maker())


# #.111
# backup = BackupClase.Backups_auto(ip_destination="10.1.2.111",
#                       port_destination="5431",
#                       login_user_destination="didieracuna",
#                       name_db_backup="balanceTecnoIFRS_1",
#                       password_destination=getenv("pwd_111"),
#                       destination_db_name="balanceTecnoIFRS_18122025_1",
#                       server=60)

# print(backup.backup_maker())






