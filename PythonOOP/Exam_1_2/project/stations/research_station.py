from project.stations.base_station import BaseStation


class ResearchStation(BaseStation):
    CAPACITY = 5
    INCREASE_SALARIES = 5000.0

    def __init__(self, name: str):
        super().__init__(name, self.CAPACITY)

    def update_salaries(self, min_value: float):
        for a in self.astronauts:
            if a.specialization == 'ScientistAstronaut':
                if a.salary <= min_value:
                    a.salary += self.INCREASE_SALARIES
