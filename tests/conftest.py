import pytest

from src.vacancy import Vacancy


@pytest.fixture
def vacancies_dict():
    vacs = [
        {
            "name": "Python Backend Developer",
            "url": "https://api.hh.ru/test",
            "snippet": {"requirement": "write code", "responsibility": "understand everything"},
            "salary": {
                "from": 200000,
                "to": 250000,
            },
        },
        {
            "name": "Python Backend Developer 2",
            "url": "https://api.hh.ru/test2",
            "snippet": {"requirement": "write code2", "responsibility": "understand everything2"},
            "salary": {
                "from": "zero",
                "to": "zero",
            },
        },
    ]
    return vacs


@pytest.fixture
def vacancy_1():
    return Vacancy("test1", 1, 11, "test_url", "test_r", "test_r")


@pytest.fixture
def vacancy_2():
    return Vacancy("test2", 2, 12, "test_url2", "test_r2", "test_r2")


@pytest.fixture
def vacancy_3():
    return Vacancy("test3", 3, 13, "test_url3", "test_r3", "test_r3")


@pytest.fixture
def vacancies_objects():
    vacs = [
        Vacancy("test4", 4, 14, "test_url4", "test_r4", "test_r4"),
        Vacancy("test5", 5, 15, "test_url5", "test_r5", "test_r5"),
        Vacancy("test6", 6, 16, "test_url6", "test_r6", "test_r6"),
        Vacancy("test7", 7, 17, "test_url7", "test_r7", "test_r7"),
    ]

    return vacs
