from src.TableScraper import TableScraper
from src.DBManager import DBManager


target_page = "https://www.cursbnr.ro/curs-bnr-azi"
table_data = TableScraper(target_page).get_table_data()

