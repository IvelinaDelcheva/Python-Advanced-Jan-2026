class IDMixin:
    id = 1

    @classmethod
    def get_id(cls):
        return cls.id

    @classmethod
    def autoincrement(cls):
        cls.id += 1
