from src.base_vacancy import BaseVacancy

# from src.print_mixin import PrintMixin


class Vacancy(BaseVacancy):
    """Класс представления информации о вакансии"""

    __slots__ = ("name", "salary_from", "salary_to", "url", "requirements", "responsibility")

    def __init__(
        self,
        name: str,
        salary_from: int | float | None,
        salary_to: int | float | None,
        url: str,
        requirement: str,
        responsibility: str,
    ):
        self.name = name
        self.salary_from = self.__validation_num_data(salary_from)
        self.salary_to = self.__validation_num_data(salary_to)
        # self.salary_avg = self.avg_salary()
        self.url = self.__validation_string_data(url)
        self.requirement = self.__validation_string_data(requirement)
        self.responsibility = self.__validation_string_data(responsibility)
        # super().__init__()

    def __eq__(self, other) -> bool:
        if not isinstance(other, Vacancy):
            raise TypeError("Операнд справа должен иметь тип Vacancy")
        else:
            return self.salary_from == other.salary_from

    def __lt__(self, other) -> bool:
        if not isinstance(other, Vacancy):
            raise TypeError("Операнд справа должен иметь тип Vacancy")
        else:
            return self.salary_to < other.salary_to

    def __le__(self, other) -> bool:
        if not isinstance(other, Vacancy):
            raise TypeError("Операнд справа должен иметь тип Vacancy")
        else:
            return self.salary_to <= other.salary_to

    def __gt__(self, other) -> bool:
        if not isinstance(other, Vacancy):
            raise TypeError("Операнд справа должен иметь тип Vacancy")
        else:
            return self.salary_to > other.salary_to

    def __ge__(self, other) -> bool:
        if not isinstance(other, Vacancy):
            raise TypeError("Операнд справа должен иметь тип Vacancy")
        else:

            return self.salary_to >= other.salary_to

    @staticmethod
    def __validation_num_data(num_data: int | float | None) -> int | float | None:
        """Валидация числовых данных"""
        if isinstance(num_data, (int, float)) and num_data:
            return num_data
        else:
            return 0

    @staticmethod
    def __validation_string_data(string_data: str | None) -> str:
        """Валидация строковых данных"""
        if isinstance(string_data, str) and string_data:
            return string_data
        else:
            return "Строка пустая"

    def __str__(self) -> str:
        """Метод отдает строки с информацией о вакансии"""
        name = f"Вакансия: {self.name}"
        salary = f"Зарплата: от {self.salary_from} и до {self.salary_to}"
        url = f"Ссылка: {self.url}"
        requirement = f"Требования: {self.requirement}"
        responsibility = f"Обязанности: {self.responsibility}"
        return f"{name}, {salary}, \n{requirement}, \n{responsibility}, \n{url}\n"

    @classmethod
    def converting_dict_to_class(cls, vacancies: list[dict]) -> list:
        """Класс метод возвращает список объектов класса Vacancy из списка словарей"""
        vacancies_list = []
        for vacancy in vacancies:
            name = vacancy.get("name")
            if vacancy.get("salary"):
                salary_from = vacancy.get("salary")["from"]
                salary_to = vacancy.get("salary")["to"]
            else:
                salary_from = vacancy.get("salary")
                salary_to = vacancy.get("salary")
            url = vacancy.get("url")
            requirements = vacancy.get("snippet")["requirement"]
            responsibility = vacancy.get("snippet")["responsibility"]
            obj = cls(name, salary_from, salary_to, url, requirements, responsibility)
            vacancies_list.append(obj)
        return vacancies_list

    def to_json(self) -> dict:
        """Возвращаем словарь с вакансиями для записи"""
        return {
            "name": self.name,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "url": self.url,
            "requirement": self.requirement,
            "responsibility": self.responsibility,
        }

    @classmethod
    def create_from_file_info(cls, vacancies: list[dict]) -> list:
        """Класс метод забирающий экземпляры Vacancy из списка словарей
         который подходит по структуре класса Vacancy"""

        return [cls(**vac) for vac in vacancies]

    # def avg_salary(self):
    # 	self.__salary_validation()
    # 	if self.salary_from and self.salary_to:
    # 		return round((int(self.salary_to) + int(self.salary_from)) /2)
    # 	return self.__salary_validation()


# if __name__ == "__main__":
#     vacancies_data = [
#         {
#             "name": "Software Developer",
#             "snippet": {"requirement": "asdasd", "responsibility": "фывфыв"},
#             "url": "https://example.com/job/1",
#             "salary": {"from": "", "to": 10000, "currency": "USD"},
#         },
#         {
#             "name": "Data Scientist",
#             "snippet": {"requirement": "asdasd", "responsibility": "фывфыв"},
#             "url": "https://example.com/job/2",
#             "salary": {"from": 6000, "to": 12000, "currency": "USD"},
#         },
#     ]
#
#     qq = Vacancy.converting_dict_to_class(vacancies_data)
#     print(qq)
#     print(qq[1].salary_to)
