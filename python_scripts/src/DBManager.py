import psycopg2
import os


DB_CONN_STR = os.getenv('DB_CONN_STR')

class DBManager:
    def __init__(self) -> None:

        try:
            self.__conn = psycopg2.connect(DB_CONN_STR)
        except:
            print("Could not connect to the database")
            
        self.__cur = self.__conn.cursor()

    
    def fetch_data(self, table:str):
        sql = f"""SELECT * FROM {table}"""
        self.__cur.execute(sql)

        records = self.__cur.fetchall()
        return records

    def write_data(self, data:list, table:str) -> None:
        sql = f"""INSERT INTO {table} (simbol, denumire, rate, date) VALUES (%s, %s, %s, %s)"""
        self.__cur.executemany(sql, data)
        self.__conn.commit()

    def close_connection(self):
        self.__cur.close()
        self.__conn.close()