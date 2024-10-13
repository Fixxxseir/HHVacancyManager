import json
import os

from config import DATA_PATH
from src.vacancy import Vacancy
from src.vacancy_data_manager import JSONSaver


def test_saver():
    saver = JSONSaver("test.json")
    vac = Vacancy("test2", 2, 2, "test_url2", "test_r2", "test_r2")

    saver.add_vacancy(vac)
    file = os.path.join(DATA_PATH, "test.json")

    with open(file, encoding="utf-8") as f:
        data = json.load(f)

    assert data == [
        {
            "name": "test2",
            "salary_from": 2,
            "salary_to": 2,
            "url": "test_url2",
            "requirement": "test_r2",
            "responsibility": "test_r2",
        }
    ]
