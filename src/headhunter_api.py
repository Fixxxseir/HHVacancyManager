import requests

from src.base_headhunter_api import Parser


class HeadHunterAPI(Parser):
    URL = "https://api.hh.ru/vacancies"

    def __init__(self):
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 50}
        self.__vacancies = []

    def __connect_to_api(self) -> None:
        response = requests.get(self.URL)
        if response.status_code != 200:
            raise Exception(f"Не удается подключится к API, код: {response.status_code}")

    def load_vacancies(self, keyword: str):
        self.__connect_to_api()
        self.__params["text"] = keyword
        while self.__params.get("page") != 10:
            response = requests.get(self.URL, headers=self.__headers, params=self.__params)
            vacancies = response.json()["items"]
            self.__vacancies.extend(vacancies)
            self.__params["page"] += 1

    @property
    def get_info(self):
        """Список вакансий"""
        return self.__vacancies


# if __name__ == "__main__":
#     sub = HeadHunterAPI()
#     sub.load_vacancies("Python")
#     vacancies_sub = sub.get_info
#
#     print(vacancies_sub)
