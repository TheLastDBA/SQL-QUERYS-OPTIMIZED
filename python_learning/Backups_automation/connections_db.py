import psycopg2
from os import getenv
from dotenv import load_dotenv
from pydantic import BaseModel


try:
    load_dotenv(
        dotenv_path=r"C:\Users\didier.acuna\git-repos\python_learning\Backups_automation\.env")

    postgres_connection_215 = psycopg2.connect(dbname="postgres",
                                               user=getenv("prd_user"),
                                               password=getenv("prd_password"),
                                               host=getenv("synergy_ip"),
                                               port=getenv("prd_port_synergy"))

    postgres_connection_60 = psycopg2.connect(dbname="postgres",
                                              user=getenv("prd_user"),
                                              password=getenv("prd_password"),
                                              host=getenv("ifrs_ip"),
                                              port=getenv("prd_port_synergy"))

    # Validating 215 databases
    psql = postgres_connection_215.cursor()

    psql_60 = postgres_connection_60.cursor()

    def exists_bd(db_name: str, server: int):

        if server == 215:

            psql.execute(
                query=f"SELECT True FROM pg_database as db where db.datistemplate = False and db.datname = '{db_name}' limit 1;")
            exists = psql.fetchone()
            exists = exists[0]

            if exists == (True):

                pass
            else:
                exists = False

        else:

            psql_60.execute(
                query=f"SELECT True FROM pg_database as db where db.datistemplate = False and db.datname = '{db_name}' limit 1;")
            exists = psql_60.fetchone()
            exists = exists[0]
            if exists == (True):

                pass
            else:
                exists = False

        return exists
except Exception as error:
    print(error)



print(exists_bd('aulaVirtual',60))

