import json
import os

from config import DATA_PATH
from src.base_vacancy_data_manager import VacancySaver
from src.vacancy import Vacancy


class JSONSaver(VacancySaver):

    def __init__(self, filename: str = "vacancies.json") -> None:
        self.filename = filename
        self.__file_path = os.path.join(DATA_PATH, filename)  # путь до файла

    #     self.__examination_file()
    #
    # def __examination_file(self):
    #     """ Проверка есть ди файл, если нет то мы создаем его пустым """
    #     if not os.path.exists(self.__file_path):
    #         with open(self.__file_path, 'w', encoding='utf-8') as f:
    #             json.dump([], f, ensure_ascii=False)
    #
    #     print("файл есть")

    def __read_file(self):
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []
        return data

    def __write_to_file(self, vacancies):
        """Метод сохранения объекта Python в ф формате json в файл"""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Добавляет объект Vacancy если такого объекта в файле нет"""
        list_for_one = self.__read_file()

        if vacancy.url not in [vac["url"] for vac in list_for_one]:
            list_for_one.append(vacancy.to_json())
            self.__write_to_file(list_for_one)

    def add_vacancies(self, vacancies: list[Vacancy]) -> None:
        """Добавляет объекты Vacancy В файл, если добавляемые объекты уже есть в файле то не добавляет"""
        list_old = self.__read_file()
        for vac in vacancies:
            if vac.url not in [vac_["url"] for vac_ in list_old]:
                list_old.append(vac.to_json())
                self.__write_to_file(list_old)

    def get_vacancy_by_vacancy_name(self, word: str) -> list[Vacancy]:
        """Возвращает список вакансий по ключевому слову в названии вакансии"""
        found_vacancies = []

        for vac in self.__read_file():
            if word in vac.get("name").lower():
                found_vacancies.append(vac)

        return Vacancy.converting_dict_to_class(found_vacancies)

    def delete_vacancy(self, word: str) -> None:
        """Удаляет вакансию из файла"""
        vacancies_list = self.__read_file()

        for index, vacancy in enumerate(vacancies_list):
            if vacancy["name"] == word:
                vacancies_list.pop(index)

        self.__write_to_file(vacancies_list)
