from src.TableScraper import TableScraper
from src.DBManager import DBManager





if __name__ == "__main__":
    target_page = "https://www.cursbnr.ro/curs-bnr-azi"
    table_data = TableScraper(target_page).get_table_data()

    db_manager = DBManager()
    
    db_entryes = db_manager.fetch_data("exchange_rates")
    print(f"DB entryes: {len(db_entryes)}")

    db_manager.write_data(table_data, "exchange_rates")
    db_entryes = db_manager.fetch_data("exchange_rates")
    print(f"DB entryes after update: {len(db_entryes)}")

    db_manager.close_connection()
