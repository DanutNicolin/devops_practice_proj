from bs4 import BeautifulSoup
import requests


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

    def get_body(self, table):
        table_body_rows = table.find("tbody").find_all("tr")

        data = []
        for row in table_body_rows:
            cols = row.find_all('td')
            cols = [el.text.strip() for el in cols]
            data.append([el for el in cols if el])

        return data
    
    def get_table_data(self):
        soup = self.get_soup()
        table = self.get_table(soup)
        headers = self.get_headers(table)
        body = self.get_body(table)

        table_data = {
            "table_headers": headers,
            "table_body": body
        }



