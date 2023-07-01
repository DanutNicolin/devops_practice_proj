from bs4 import BeautifulSoup
import requests
from datetime import datetime
# from time import strptime


class TableScraper:
    def __init__(self, page_link) -> None:
        self.page_link = page_link
        
    def get_soup(self):
        page_text_html = requests.get(self.page_link).text

        soup = BeautifulSoup(page_text_html, "lxml")
        return soup

    def get_table(self, soup):
        return soup.find("table")
        

    def get_headers(self, table):
        table_headers_rows = table.find("thead").find("tr")
        cols = [el.text.strip() for el in table_headers_rows.find_all("th")]
        return cols

    def get_formated_data(self, table, headers):
        table_body_rows = table.find("tbody").find_all("tr")

        date_str = headers[2].replace(".", "-")
        date = datetime.strptime(date_str, '%d-%m-%Y').date()

        data = []
        for row in table_body_rows:
            cols = row.find_all('td')
            cols = [el.text.strip() for i,el in enumerate(cols) if i != 3]
            cols.append(date)

            data.append(tuple(el for el in cols))

        return data
    

    
    def get_table_data(self):
        soup = self.get_soup()
        table = self.get_table(soup)
        headers = self.get_headers(table)
        table_data = self.get_formated_data(table, headers)

        return table_data


