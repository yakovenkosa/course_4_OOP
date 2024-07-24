from abc import ABC, abstractmethod


class VacancyBase(ABC):

    __slots__ = ('title', 'city', 'salary_from', 'salary_to', 'description', 'link')

    @abstractmethod
    def __init__(self, title, city, salary_from, salary_to, description, link):
        self.title = title                 # Наименование вакансии
        self.city = city                   # Город, где открыта вакансия
        self.salary_from = salary_from     # З/П от
        self.salary_to = salary_to         # З/П до
        self.description = description     # Описание вакансии
        self._link = link                  # Ссылка на вакансию

    @abstractmethod
    def __str__(self):
        pass


class Vacancy(VacancyBase):
    title: str              # Наименование вакансии
    city: str               # Город, где открыта вакансия
    salary_from: int        # З/П от
    salary_to: int          # З/П до
    description: str        # Описание вакансии
    link: str               # Ссылка на вакансию

    def __init__(self, title: str, city: str, salary_from: int, salary_to: int, description: str, link: str):
        super().__init__(title, city, salary_from, salary_to, description, link)

    def __repr__(self):
        return (f"{self.title}, {self.city}, {self.salary_from},"
                f"{self.salary_to}, {self.description}, {self._link}")

    def __str__(self):
        return (f"Вакансия: {self.title}. "
                f"Город: {self.city}. "
                f"Зарплата от {self.salary_from} до {self.salary_to}. "
                f"Описание: {self.description}. "
                f"Ссылка: {self._link}.")

    @property
    def title_data(self):
        if self.title is not None:
            return self.title
        else:
            return "Ошибка"

    @property
    def city_data(self):
        if self.city is not None:
            return self.city
        else:
            return "Ошибка: не указан город"

    @property
    def description_data(self):
        if self.description is not None:
            return self.description
        else:
            return "Ошибка: отсутствует описание вакансии"

    @property
    def link_data(self):
        if self.link is not None:
            return self._link
        else:
            return "Ошибка: отсутствует ссылка на вакансию"

    def __lt__(self, other):
        """
        Метод сравнения: меньше
        """
        if self.salary_from is None or other.salary_from is None:
            return False
        return self.salary_from < other.salary_from

    def __gt__(self, other):
        """
        Метод сравнения: больше
        """
        if self.salary_from is None or other.salary_from is None:
            return False
        return self.salary_from > other.salary_from

    def __eq__(self, other):
        """
        Метод сравнения вакансий: равно
        """
        if self.salary_from is not None and other.salary_from is not None:
            return self.salary_from == other.salary_from
        return False
    