from src.framework.Settings import Settings
import sqlite3
import cx_Oracle
import traceback

from src.framework.LogHandler import LogHandler
logger = LogHandler.getLogger()

class DatabaseConnectionFactory:

    connection = None
    cursor = None

    @staticmethod
    def get_connection(database_type):
        try:
            properties = Settings.getProperty()
            if DatabaseConnectionFactory.connection is None:
                if database_type.upper() == "SQLITE":
                    DatabaseConnectionFactory.connection = sqlite3.connect(properties.get("DATABASE","SQLITE_PATH"))
                elif(database_type.upper() == "ORACLE"):
                    # dsn_tns = cx_Oracle.makedsn(properties.get("DATABASE","HOSTNAME"), properties.get("DATABASE","PORT"),
                    #                             service_name=properties.get("DATABASE","SERVICE"))
                    # conn = cx_Oracle.connect(user=properties.get("DATABASE","HOSTNAME"), password=properties.get("DATABASE","HOSTNAME"),
                    #                          dsn=dsn_tns)
                    # DatabaseConnectionFactory.connection = conn
                    # DatabaseConnectionFactory.cursor = conn.cursor()
                    DatabaseConnectionFactory.connection = ""
                    logger.info("Establishing Oracle database connection.....")
                else:
                    raise Exception("Incorrect Database type - "+str(database_type))
                logger.info("Database Connection created successfully")
            return DatabaseConnectionFactory.connection
        except Exception as e:
            traceback.print_exc()
            print(str(e))


    @staticmethod
    def getResultset(connection,query):
        pass