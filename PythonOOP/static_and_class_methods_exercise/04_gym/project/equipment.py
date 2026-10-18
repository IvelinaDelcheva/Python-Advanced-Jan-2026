from project.idmixin import IDMixin


class Equipment(IDMixin):
    def __init__(self, name: str):
        self.name = name
        self.id = Equipment.id
        Equipment.autoincrement()

    @staticmethod
    def get_next_id():
        return Equipment.get_id()

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
        