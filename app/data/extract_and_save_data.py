from bs4 import BeautifulSoup
from app.database.mongo import db
from app.config import settings
import requests
import re


class ExtractData:
    def __init__(self, end) -> None:
        self.uri = settings.URI_TCM
        self.uris = self.get_uris(end)

    def get_uris(self, end):
        uris = []
        for i in range(2, end):
            if len(str(i)) < 3:
                if len(str(i)) == 2:
                    c = "0" + str(i)
                else:
                    c = "00" + str(i)
            else:
                c = str(i)
            uri = self.uri.format(c)

            uris.append(uri)
        return uris

    def get_tables(self, uri):
        site = requests.get(uri)

        soup = BeautifulSoup(site.content, 'html.parser')

        tables = soup.find("table").find("tbody")

        city = (soup.find('title').text).replace(
            "Portal da Transparência -", "")

        return tables, city

    def get_data(self, tables):
        data = []
        for tr in tables.find_all("tr"):
            c = {}
            n = 0
            for td in tr.find_all("td"):
                n += 1
                if n != 2:
                    c[str(n)] = td.text.replace("/xa0", "").strip()
                else:
                    text = td.text.replace("/xa0", "").strip()
                    match = re.finditer("Cód", text)
                    for i in match:
                        c[str(n)] = (text[0: i.start()]).strip()
            data.append(c)
        return data

    def save_data(self, data, city):
        for i in range(len(data)):
            db.insert(city, {
                '_id': str(i),
                'city': city,
                "data": data[i]
            })

    def start(self):
        for uri in self.uris:
            table, city = self.get_tables(uri)

            data = self.get_data(table)

            self.save_data(data, "test")
