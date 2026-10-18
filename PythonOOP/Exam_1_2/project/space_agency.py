from project.astronauts.engineer_astronaut import EngineerAstronaut
from project.astronauts.scientist_astronaut import ScientistAstronaut
from project.stations.maintenance_station import MaintenanceStation
from project.stations.research_station import ResearchStation


class SpaceAgency:
    def __init__(self):
        self.astronauts = []
        self.stations = []

    def add_astronaut(self, astronaut_type: str, astronaut_id_number: str, astronaut_salary: float):
        valid_a = {"EngineerAstronaut": EngineerAstronaut, "ScientistAstronaut": ScientistAstronaut}

        if astronaut_type not in valid_a.keys():
            raise ValueError("Invalid astronaut type!")

        a_same_id = next((a for a in self.astronauts if a.id_number == astronaut_id_number), None)
        if a_same_id:
            raise ValueError(f"{astronaut_id_number} has been already added!")

        self.astronauts.append(valid_a[astronaut_type](astronaut_id_number, astronaut_salary))
        return f"{astronaut_id_number} is successfully hired as {astronaut_type}."

    def add_station(self, station_type: str, station_name: str):
        valid_s = {"ResearchStation": ResearchStation, "MaintenanceStation": MaintenanceStation}

        if station_type not in valid_s.keys():
            raise ValueError("Invalid station type!")

        s_same_name = next((s for s in self.stations if s.name == station_name), None)
        if s_same_name:
            raise ValueError(f"{station_name} has been already added!")

        self.stations.append(valid_s[station_type](station_name))
        return f"{station_name} is successfully added as a {station_type}."

    def assign_astronaut(self, station_name: str, astronaut_type: str):
        s_existence = next((s for s in self.stations if s.name == station_name), None)
        if s_existence is None:
            raise ValueError(f"Station {station_name} does not exist!")

        astronaut_ex = next((a for a in self.astronauts if a.__class__.__name__ == astronaut_type), None)
        if astronaut_ex is None:
            raise ValueError("No available astronauts of the type!")

        if s_existence.capacity <= 0:
            return "This station has no available capacity."

        self.astronauts.remove(astronaut_ex)
        s_existence.astronauts.append(astronaut_ex)
        s_existence.capacity -= 1
        return f"{astronaut_ex.id_number} was assigned to {s_existence.name}."

    @staticmethod
    def train_astronauts(station, sessions_number: int):
        for session in range(sessions_number):
            for a in station.astronauts:
                a.train()

        total_stamina = sum(a.stamina for a in station.astronauts)
        return f"{station.name} astronauts have {total_stamina} total stamina after {sessions_number} training session/s."

    @staticmethod
    def retire_astronaut(station, astronaut_id_number: str):
        a_to_retire = next((a for a in station.astronauts if a.id_number == astronaut_id_number and a.stamina != 100),
                           None)
        if a_to_retire is None:
            return "The retirement process was canceled."
        station.astronauts.remove(a_to_retire)
        station.capacity += 1
        return f"Retired astronaut {astronaut_id_number}."

    def agency_update(self, min_value: float):
        for s in self.stations:
            s.update_salaries(min_value)
        total_available_capacity = sum(s.capacity for s in self.stations)
        s_sorted = sorted(self.stations, key=lambda station: (-len(station.astronauts), station.name))
        agency_info = ["*Space Agency Up-to-Date Report*",
                       f"Total number of available astronauts: {len(self.astronauts)}\n"
                       f"**Stations count: {len(self.stations)}; Total available capacity: {total_available_capacity}**"]
        for srt_station in s_sorted:
            agency_info.append(
                f"{srt_station.status()}")

        return '\n'.join(agency_info)
