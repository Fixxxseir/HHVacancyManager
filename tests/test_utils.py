from src.utils import get_top_n_vacancies, sort_vacancies_by_salary, sort_vacancies_in_range


def test_sort_vacancies_by_salary(vacancies_objects):

    sorted_vacancies = sort_vacancies_by_salary(vacancies_objects)
    assert sorted_vacancies[0].name == "test7"
    assert sorted_vacancies[1].name == "test6"
    assert sorted_vacancies[2].name == "test5"


def test_sort_vacancies_in_range(vacancies_objects):

    filtered_vacancies = sort_vacancies_in_range(vacancies_objects, 6)
    assert 2 == len(filtered_vacancies)
    assert filtered_vacancies[0].name == "test6"
    assert filtered_vacancies[1].name == "test7"


def test_get_top_n_vacancies(vacancies_objects):

    top_vacancies = get_top_n_vacancies(vacancies_objects, 2)
    assert len(top_vacancies) == 2
    assert top_vacancies[0].name == "test7"
    assert top_vacancies[1].name == "test6"


def test_sort_vacancies_in_range_empty(vacancies_objects):
    assert sort_vacancies_in_range([], 1) == []
