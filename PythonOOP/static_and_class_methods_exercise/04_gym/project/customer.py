from project.idmixin import IDMixin


class Customer(IDMixin):
    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.id
        Customer.autoincrement()

    @staticmethod
    def get_next_id():
        return Customer.get_id()

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
