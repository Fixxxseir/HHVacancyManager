from abc import ABC, abstractmethod

from src.vacancy import Vacancy


class VacancySaver(ABC):

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Добавляет вакансию объекта Vacancy"""
        pass

    @abstractmethod
    def add_vacancies(self, vacancies: list[Vacancy]) -> None:
        """Добавляет список объектов Vacancy"""

    @abstractmethod
    def get_vacancy_by_vacancy_name(self, word: str) -> list[Vacancy]:
        """Возвращает список вакансий"""
        pass

    @abstractmethod
    def delete_vacancy(self, name: str) -> None:
        """Удаление вакансии из файла"""
        pass
