

class Vacancy:
	__slots__ = ('name', 'alternate_url', 'requirements', 'responsibility', 'salary')

	def __init__(self, name, alternate_url, requirements, responsibility, salary):
		self.name = name
		self.alternate_url = alternate_url
		self.requirements = requirements
		self.responsibility = responsibility
		self.salary = salary


