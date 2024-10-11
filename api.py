import json
from abc import ABC, abstractmethod

import requests


class AbstractApi(ABC):
    @abstractmethod
    def get_vacancies(self, *args):
        pass


class HHApi(AbstractApi):
    def __init__(self):

        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}

    def get_vacancies(self, keyword, page):
        params = {
            "text": keyword,
            "page": page
        }
        return requests.get(self.url, params=params, headers=self.headers)


a = HHApi()
response = a.get_vacancies("водитель", 1)
with open("raw.json", "w", encoding="utf-8") as file:
    json.dump(response.json(), file, ensure_ascii=False, indent=5)
