from abc import ABC, abstractmethod
import json


class BaseSafe(ABC):

    @abstractmethod
    def write_data(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def read_file(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def delete_file(self, *args, **kwargs):
        raise NotImplementedError


class JSONSafe(BaseSafe):

    def __init__(self, file):
        self.file = file

    def write_data(self, data) -> None:
        """
        Функция, которая записывает данные в файл json.
        """
        with open(self.file, 'w', encoding='utf-8') as new_file:
            json.dump(data, new_file, indent=4, ensure_ascii=False)

    def read_file(self) -> None:
        """
        Функция для считывания файла json.
        """
        with open(self.file, 'r', encoding='utf-8') as file:
            file.readline()

    def delete_file(self) -> None:
        """
        Функция, для удаления информации из файла json.
        """
        with open(self.file, 'r+', encoding='utf-8') as file:
            file.truncate(0)
