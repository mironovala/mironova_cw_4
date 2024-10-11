import json
from abc import ABC, abstractmethod
from typing import Any

import requests

from vacancy import Vacancy


class AbstractApi(ABC):
    @abstractmethod
    def get_vacancies(self, *args):
        pass

    @abstractmethod
    def rom_vacancy(self, vacancies):
        pass


class HHApi(AbstractApi):
    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}

    def get_vacancies(self, keyword: str, page: int):
        params = {
            "text": keyword,
            "page": page
        }
        return requests.get(self.url, params=params, headers=self.headers)

    def from_vacancy(Self, vacancies: list[dict[str, Any]]):
        vacancies_ok = []
        for vacancy in vacancies:
            vacancies_ok.append((Vacancy(name=vacancy["name"], url=vacancy["url"], salary=vacancy["salary"],
                                         description=vacancy["description"])))
            pass


a = HHApi()
response = a.get_vacancies("водитель", 1)
with open("raw.json", "w", encoding="utf-8") as file:
    json.dump(response.json(), file, ensure_ascii=False, indent=5)
