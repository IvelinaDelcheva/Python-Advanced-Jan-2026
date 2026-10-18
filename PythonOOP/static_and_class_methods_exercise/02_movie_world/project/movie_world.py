from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers: list[Customer] = []
        self.dvds: list[DVD] = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        customer = next(c for c in self.customers if c.id == customer_id)
        dvd = next((dvd for dvd in customer.rented_dvds if dvd_id == dvd.id), None)
        if dvd:
            return f"{customer.name} has already rented {dvd.name}"
        dvd_mv = next((dvd for dvd in self.dvds if dvd_id == dvd.id), None)
        if dvd_mv.is_rented:
            return "DVD is already rented"
        if customer.age < dvd_mv.age_restriction:
            return f"{customer.name} should be at least {dvd_mv.age_restriction} to rent this movie"
        dvd_mv.is_rented = True
        customer.rented_dvds.append(dvd_mv)
        return f"{customer.name} has successfully rented {dvd_mv.name}"

    def return_dvd(self, customer_id, dvd_id) -> str:
        customer = next(c for c in self.customers if c.id == customer_id)
        dvd = next((dvd for dvd in customer.rented_dvds if dvd_id == dvd.id), None)
        if dvd:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        customers_dvds = [c.__repr__() for c in self.customers]
        customers_dvds.extend([dvd.__repr__() for dvd in self.dvds])
        return '\n'.join([item for item in customers_dvds])
