from abc import ABC, abstractmethod


class Engine(ABC):
    """Абстрактный класс для получения вакансий с сайтов."""

    @abstractmethod
    def get_vacancies(self):
        """Абстрактный метод для получения списка вакансий с сайта."""
        pass
