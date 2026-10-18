from abc import ABC, abstractmethod


class BaseStation(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.astronauts = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum() and '-' not in value:
            raise ValueError("Station names can contain only letters, numbers, and hyphens!")
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("A station cannot have a negative capacity!")
        self.__capacity = value

    def calculate_total_salaries(self):
        total_salaries = sum(a.salary for a in self.astronauts)
        return f"{total_salaries:.2f}"

    def status(self):
        astronauts_ids = "N/A"
        if self.astronauts:
            astronauts_ids_sort = sorted(self.astronauts, key=lambda a: a.id_number)
            astronauts_ids = ' #'.join(a.id_number for a in astronauts_ids_sort)
        station_info = f"Station name: {self.name}; Astronauts: {astronauts_ids}; Total salaries: {self.calculate_total_salaries()}"
        return station_info

    @abstractmethod
    def update_salaries(self, min_value: float):
        pass
