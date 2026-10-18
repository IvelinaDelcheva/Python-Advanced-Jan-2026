from project.stations.base_station import BaseStation


class MaintenanceStation(BaseStation):
    CAPACITY = 3
    INCREASE_SALARIES = 3000.0

    def __init__(self, name: str):
        super().__init__(name, self.CAPACITY)

    def update_salaries(self, min_value: float):
        for a in self.astronauts:
            if a.specialization == 'EngineerAstronaut':
                if a.salary <= min_value:
                    a.salary += self.INCREASE_SALARIES
