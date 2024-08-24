from src.hh_class import HeadHunter
from src.json_class import JSONSafe
from src.functions import create_list_obj, sort_salary_from


def user_interaction():
    """
    Функция для работы с пользователем
    """

    print("Приветствуем вас! Наше приложение поможет вам найти подходящую вакансию.")
    user_vacancy = input("Введите наименование интересующей вас вакансии: ").lower().strip()
    hh = HeadHunter()
    vacancy_from_hh = hh.get_vacancies(user_vacancy)
    saving_vac = JSONSafe("data/find_vacancy.json")
    saving_vac.write_data(vacancy_from_hh)
    user_sorting_number = int(input("Выберите номер, сортировки списка вакансий:\n"
                                    "1 - сортировка по возрастанию з/п\n"
                                    "2 - сортировка по убыванию з/п\n"
                                    "3 - без сортировки\n"))

    vacs_list = create_list_obj(vacancy_from_hh)

    sorted_vacs = sort_salary_from(vacs_list, user_sorting_number)

    user_top_number = int(input('Выберите номер топа вакансий:\n'
                                '1 - топ-5 вакансий\n' 
                                '2 - топ-10 вакансий\n'
                                '3 - топ-15 вакансий\n'
                                '4 - показать все вакансии\n'))
    if user_top_number == 1:
        for vac in sorted_vacs[:5]:
            print(vac)
    elif user_top_number == 2:
        for vac in sorted_vacs[:10]:
            print(vac)
    elif user_top_number == 3:
        for vac in sorted_vacs[:15]:
            print(vac)
    elif user_top_number == 4:
        for vac in sorted_vacs:
            print(vac)

    choose_another_vac = input("Выбрать другую вакансию?\n да/нет : \n").lower().strip()
    if choose_another_vac in ['y', 'yes', 'да', 'д']:

        user_interaction()
    elif choose_another_vac in ['n', 'no', 'нет', 'н']:
        print('Работа программы завершена. Желаем успеха в поиске новой вакансии!')
        exit()


if __name__ == "__main__":
    user_interaction()
