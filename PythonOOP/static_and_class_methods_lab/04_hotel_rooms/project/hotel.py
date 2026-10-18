from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: list[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room_to_take = next(room for room in self.rooms if room.number == room_number)
        if room_to_take:
            success = room_to_take.take_room(people)
            if success is None:
                self.guests += people

    def free_room(self, room_number):
        room_to_free = next(room for room in self.rooms if room.number == room_number)
        self.guests -= room_to_free.guests
        room_to_free.free_room()

    def status(self) -> str:
        return f"Hotel {self.name} has {self.guests} total guests\nFree rooms: {', '.join([str(room.number) for room in self.rooms if not room.is_taken])}\nTaken rooms: {', '.join([str(room.number) for room in self.rooms if room.is_taken])}"
