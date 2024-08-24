from src.vacancies_class import Vacancy


def create_list_obj(list_obj):
    """
    Создание списка из класса Vacancy
    """
    list_vacancies = []
    for item in list_obj:
        list_vacancies.append(
            Vacancy(item.get('name'),
                    item.get('area', {}).get('name'),
                    item.get('salary').get('from') if item["salary"] is not None else 0,
                    item.get('salary').get('to') if item["salary"] is not None else 0,
                    item.get('snippet', {}).get('requirement'),
                    item.get('apply_alternate_url'),
                    )
                            )
    return list_vacancies


def sort_salary_from(vacs_list, user_sorting_number):
    """
    Функция которая сортирует список вакансий по зарплате.
    """

    if user_sorting_number == 1:
        vacs_list.sort()
        print('Выбрано: Сортировка по возрастанию зарплаты')
    if user_sorting_number == 2:
        vacs_list.sort(reverse=True)
        print('Выбрано: Сортировка по убыванию зарплаты')
    if user_sorting_number == 3:
        print('Выбрано: Без сортировки списка вакансий')
    return vacs_list
