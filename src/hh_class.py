import requests
from abc import ABC, abstractmethod


class BaseHeadHunter(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancies(self, *args, **kwargs):
        pass


class HeadHunter(BaseHeadHunter):
    """
    Класс для работы с API HeadHunter
    Класс BaseHeadHunter является родительским классом.
    """

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.params = {'text': '', 'page': 0, 'per_page': 100, 'area': 113}
        self.vacancies = []

    def get_vacancies(self, keyword) -> list:
        """
        Функция получает вакансий с API по пользовательскому слову.
        :param keyword: Слово для поиска вакансии, которое вводит пользователь.
        :return: self.vacancies - возвращает список вакансий.
        """
        self.params['text'] = keyword
        while self.params.get('page') != 10:
            response = requests.get(self.url, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
        return self.vacancies
