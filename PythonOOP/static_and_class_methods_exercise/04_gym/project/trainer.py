from project.idmixin import IDMixin


class Trainer(IDMixin):
    def __init__(self, name: str):
        self.name = name
        self.id = Trainer.id
        Trainer.autoincrement()

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Trainer.get_id()
