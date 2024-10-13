# from src.print_mixin import PrintMixin
from src.headhunter_api import HeadHunterAPI
from src.utils import get_top_n_vacancies, sort_vacancies_in_range
from src.vacancy import Vacancy
from src.vacancy_data_manager import JSONSaver


# функция взаимодействия с пользователем
def main():
    """Функция взаимодействия с пользователем"""
    print("Программа для поиска работы по вакансиям \n")
    word = input("Введи название своей вакансии для поиска сюда: ")

    # поиск по запросу
    hh_start = HeadHunterAPI()
    hh_start.load_vacancies(word)
    hh = hh_start.get_info

    # сохранение вакансий в файл
    qq = Vacancy.converting_dict_to_class(hh)
    save_json = JSONSaver()
    save_json.add_vacancies(qq)
    print(f"По вашему запросу загрузить удалось {len(hh)} вакансий")

    # выбор сортировки
    print("Если желаете можно отсортировать по критериям")
    while True:
        filter_word = input(
            "Варианты сортировки:\n"
            "1. Вакансии от указанной зарплаты\n"
            "2. Топ N вакансий по зарплате\n"
            "3. Найти вакансию по названию\n"
            "4. Может вы хотите добавить на будущее вакансию в список\n"
            "5. Или удалить любую вакансию из списка по url\n"
            "6. Показать все вакансии\n"
            "Введите номер варианта или 'stop' что бы выйти:  "
        )

        if filter_word.lower() == "stop":
            break
            # Код для обработки первого варианта
        elif filter_word == "1":
            try:
                salary_from = int(input("Укажите нижний порог зарплаты (целое число от 0): "))
            except ValueError:
                print("Некорректный ввод. Нижний порог не указан")
                salary_from = 0
            vacs_objects = Vacancy.converting_dict_to_class(hh)
            for vac in sort_vacancies_in_range(vacs_objects, salary_from):
                print(vac)
                print()

        elif filter_word == "2":
            # Код для обработки 2 варианта
            try:
                top_n = int(input("Введите количество вакансий для вывода в топ N: "))
            except ValueError:
                print("Количество вакансий должно быть целым числом")
                print("По умолчанию будет выведено 10 вакансий\n")
                top_n = 10

            if top_n > len(hh):
                top_n = len(hh) - 1

            vacs_objects = Vacancy.converting_dict_to_class(hh)
            for vac in get_top_n_vacancies(vacs_objects, top_n):
                print(vac)
                print()
        elif filter_word == "3":
            # Код для обработки четвертого варианта
            vacancy_name = input("Введите слово для поиска: ").lower()
            for vac in save_json.get_vacancy_by_vacancy_name(vacancy_name):
                print(vac)
                print()
        elif filter_word == "4":
            # Код для обработки пятого варианта
            vacancy = Vacancy(
                input("Введите название: "),
                int(input("Введите зарплату от: ")),
                int(input("Введите зарплату до: ")),
                input("Введите ссылку: "),
                input("Введите требования: "),
                input("Введите обязанности: "),
            )
            save_json.add_vacancy(vacancy)
        elif filter_word == "5":
            # Код для обработки шестого варианта
            url = input("Введите ссылку на вакансию: ")
            save_json.delete_vacancy(url)
        elif filter_word == "6":
            for vac in Vacancy.converting_dict_to_class(hh):
                print(vac)
                print()
        else:
            print("Неверный ввод. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()
