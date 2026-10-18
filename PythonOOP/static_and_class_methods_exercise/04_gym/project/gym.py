from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: list[Customer] = []
        self.trainers: list[Trainer] = []
        self.equipment: list[Equipment] = []
        self.plans: list[ExercisePlan] = []
        self.subscriptions: list[Subscription] = []

    def add_customer(self, customer: Customer) -> None:
        return self.add_obj(customer, self.customers)

    def add_trainer(self, trainer: Trainer) -> None:
        return self.add_obj(trainer, self.trainers)

    def add_equipment(self, equipment: Equipment) -> None:
        return self.add_obj(equipment, self.equipment)

    def add_plan(self, plan: ExercisePlan) -> None:
        return self.add_obj(plan, self.plans)

    def add_subscription(self, subscription: Subscription) -> None:
        return self.add_obj(subscription, self.subscriptions)

    def subscription_info(self, subscription_id: int) -> str:
        subscription = next((s for s in self.subscriptions if s.id == subscription_id), None)
        customer = next((c for c in self.customers if c.id == subscription.customer_id), None)
        trainer = next((t for t in self.trainers if t.id == subscription.trainer_id), None)
        exercise = next((e for e in self.plans if e.id == subscription.exercise_id), None)
        equipment = next((eq for eq in self.equipment if eq.id == exercise.equipment_id), None)
        return '\n'.join([subscription.__repr__(), customer.__repr__(), trainer.__repr__(), equipment.__repr__(),
                          exercise.__repr__()])

    @staticmethod
    def add_obj(obj: Customer | Trainer | Equipment | ExercisePlan | Subscription,
                collection: list[Customer | Trainer | Equipment | ExercisePlan | Subscription]) -> None:
        if obj not in collection:
            collection.append(obj)
