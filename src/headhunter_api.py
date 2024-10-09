from abc import ABC, abstractmethod
import requests


class Parser(ABC):

	@abstractmethod
	def load_vacancies(self, keyword):
		pass

	@abstractmethod
	def get_vacancies(self):
		pass


class HeadHunterAPI(Parser):

	def __init__(self):
		self.__url = 'https://api.hh.ru/vacancies'
		self.__headers = {'User-Agent': 'HH-User-Agent'}
		self.__params = {'text': '', 'page': 0, 'per_page': 1}
		self.__vacancies = []

	def __connect_to_api(self):
		response = requests.get(self.__url)
		if response.status_code != 200:
			raise Exception(f'Не удается подключится к API, код: {response.status_code}')

	def load_vacancies(self, keyword):
		self.__connect_to_api()
		self.__params['text'] = keyword
		while self.__params.get('page') != 1:
			response = requests.get(self.__url, headers=self.__headers, params=self.__params)
			vacancies = response.json()["items"]
			self.__vacancies.extend(vacancies)
			self.__params["page"] += 1

	@property
	def get_vacancies(self):
		""" Список вакансий """
		return self.__vacancies


if __name__ == "__main__":
	sub = HeadHunterAPI()
	sub.load_vacancies('Python')
	vacancies_sub = sub.get_vacancies
	print(vacancies_sub)
