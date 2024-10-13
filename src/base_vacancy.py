from abc import ABC, abstractmethod


class BaseVacancy(ABC):
    """Базовый класс для вакансий с обязательными методами"""

    @abstractmethod
    def __eq__(self, other) -> bool:
        """Магический метод проверки равенства =="""
        pass

    @abstractmethod
    def __lt__(self, other) -> bool:
        """Магический метод оператора меньше <"""
        pass

    @abstractmethod
    def __le__(self, other) -> bool:
        """Магический метод оператора меньше или равно <="""
        pass

    @abstractmethod
    def __gt__(self, other) -> bool:
        """Магический метод оператора больше >"""
        pass

    @abstractmethod
    def __ge__(self, other) -> bool:
        """Магический метод оператора больше или равно >="""
        pass

    @staticmethod
    def __validation_num_data(num_data: int | float | None) -> int | float | None:
        """Статический метод валидации данных, проверка на наличие чисел"""
        pass

    @staticmethod
    def __validation_string_data(string_data):
        """Статистический метод валидации данных, проверка на наличие строки"""
        pass

    @classmethod
    def converting_dict_to_class(cls, vacancies: list[dict]) -> list:
        pass

    @abstractmethod
    def to_json(self) -> dict:
        pass
