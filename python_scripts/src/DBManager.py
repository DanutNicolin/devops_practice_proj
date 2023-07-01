import psycopg2




class DBManager:
    def __init__(self) -> None:
        db_name = "test_db_name"
        db_user = "test_user"
        self.__conn = psycopg2.connect("dbname=test user=postgres")
        self.__cur = self.__conn.cursor()
    
    def fetch_data(self):
        # Execute a query
        self.__cur.execute("SELECT * FROM my_data")

        # Retrieve query results
        records = self.__cur.fetchall()
        pass

