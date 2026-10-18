class Song:
    def __init__(self, name: str, length: str, single: bool):
        self.name = name
        self.length = length
        self.single = single

    def get_info(self) -> str:
        return f"{self.name} - {self.length}"
        