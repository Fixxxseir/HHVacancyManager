from src.vacancy import Vacancy


def test_vacancy_init(vacancy_1):
    assert vacancy_1.name == "test1"
    assert vacancy_1.salary_from == 1
    assert vacancy_1.salary_to == 11
    assert vacancy_1.url == "test_url"
    assert vacancy_1.requirement == "test_r"
    assert vacancy_1.responsibility == "test_r"


def test_vacancy_to_json(vacancies_objects):
    vac = vacancies_objects[0]
    assert vac.to_json() == {
        "name": "test4",
        "salary_from": 4,
        "salary_to": 14,
        "url": "test_url4",
        "requirement": "test_r4",
        "responsibility": "test_r4",
    }

    vac = Vacancy("test5", 2, "qwewq", "test_url4", "rek", "")
    assert vac.to_json() == {
        "name": "test5",
        "salary_from": 2,
        "salary_to": 0,
        "url": "test_url4",
        "requirement": "rek",
        "responsibility": "Строка пустая",
    }


def test_converting_dict_to_class(vacancies_dict):
    vacs = Vacancy.converting_dict_to_class(vacancies_dict)
    assert len(vacs) == 2
    assert vacs[0].name == "Python Backend Developer"
    assert vacs[1].salary_from == 0


def test_vacancy_str(vacancy_1):
    assert str(vacancy_1) == (
        "Вакансия: test1, Зарплата: от 1 и до 11, \nТребования: test_r, \nОбязанности: test_r, \nСсылка: test_url\n"
    )


def test_converting_dict_to_class_empty():
    vacs = Vacancy.converting_dict_to_class([])
    assert vacs == []


def test_vacancy_eq(vacancies_objects):
    vac = Vacancy("test5", 5, 15, "test_url5", "test_r5", "test_r5")
    assert vacancies_objects[0] != vacancies_objects[1]
    assert vacancies_objects[1] == vac


def test_vacancy_le(vacancies_objects):
    assert vacancies_objects[3] >= vacancies_objects[2]
    assert vacancies_objects[1] <= vacancies_objects[2]
