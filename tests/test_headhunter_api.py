from src.headhunter_api import HeadHunterAPI


def test_load_vacancies():
    api = HeadHunterAPI()
    api.load_vacancies("Python developer")
    assert len(api.get_info) > 0
    assert all("name" in vacancy for vacancy in api.get_info)


def test_get_info():
    api = HeadHunterAPI()
    api.load_vacancies("Python developer")
    info = api.get_info
    assert isinstance(info, list)
    assert all(isinstance(vacancy, dict) for vacancy in info)


# def test_load_vacancies_invalid_keyword():
#     api = HeadHunterAPI()
#     with pytest.raises(Exception):
#         api.load_vacancies("ыыыы")
