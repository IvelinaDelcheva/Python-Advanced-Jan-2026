from project.animal import Animal
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: list[Animal] = []
        self.workers: list[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__budget - price >= 0 and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        if self.__budget - price < 0 and self.__animal_capacity > len(self.animals):
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name: str) -> str:
        worker_to_fire = next((w for w in self.workers if w.name == worker_name), None)
        if worker_to_fire:
            self.workers.remove(worker_to_fire)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        workers_salaries = sum(w.salary for w in self.workers)
        if self.__budget >= workers_salaries:
            self.__budget -= workers_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        animals_care = sum(a.money_for_care for a in self.animals)
        if self.__budget >= animals_care:
            self.__budget -= animals_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def print_result(self, collection: list[Animal | Worker], *args):
        result = [f"You have {len(collection)} {collection[0].__class__.__bases__[0].__name__.lower()}s"]
        object_dict = {arg: [] for arg in args}

        for anml in collection:
            object_dict[anml.__class__.__name__].append(anml)

        for cls, objects in object_dict.items():
            result.append(f'----- {len(object_dict[cls])} {cls}s:')
            result.append('\n'.join(f'{obj}' for obj in objects))
        return '\n'.join(result)

    def animals_status(self):
        return self.print_result(self.animals, 'Lion', 'Tiger', 'Cheetah')

    def workers_status(self):
        return self.print_result(self.workers, 'Keeper', 'Caretaker', 'Vet')
