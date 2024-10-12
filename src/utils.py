from src.vacancy import Vacancy


def sort_vacancies_by_salary(vacancies: list[Vacancy]) -> list[Vacancy]:
    """
    Функция для сортировки вакансий по зарплате
    """
    by_salary = sorted(vacancies, key=lambda x: x.salary_from, reverse=True)
    return by_salary


def sort_vacancies_in_range(vacancies: list[Vacancy], salary: int) -> list[Vacancy]:
    """
    Функция для сортировки в заданном диапазоне
    """
    by_range = [vac for vac in vacancies if vac.salary_from >= salary]

    return by_range


def get_top_n_vacancies(vacansies: list[Vacancy], top_n: int) -> list[Vacancy]:
    """
    Функция возвращает топ N вакансий по зарплате
    """
    by_top_n = sort_vacancies_by_salary(vacansies)

    return by_top_n[:top_n]
