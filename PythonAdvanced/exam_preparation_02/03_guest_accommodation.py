def accommodate(*args, **kwargs):
    accommodated = {}
    guests = list(args)
    rooms = kwargs
    sorted_rooms = sorted(kwargs.items(), key=lambda kv: (kv[1], int(kv[0].split('_')[1])))
    for index, guest in enumerate(args):
        for room in sorted_rooms:
            if guest == room[1]:
                if not room[0] in accommodated.keys():
                    accommodated[room[0]] = guest
                    guests.remove(guest)
                    rooms.pop(room[0])

    if guests:
        for left_guest in guests:
            smallest_capacity = 5
            best_fit = {}
            for left_room in rooms.items():
                if left_room[1] > left_guest:
                    diff = left_room[1] - left_guest
                    if diff < smallest_capacity:
                        smallest_capacity = diff
                        best_fit = left_room
            if best_fit:
                accommodated[best_fit[0]] = left_guest
                guests.remove(left_guest)
                rooms.pop(best_fit[0])
    if accommodated:
        message = f"A total of {len(accommodated)} accommodations were completed!\n"
        message += ''.join(f"<Room {key.split('_')[1]} accommodates {value} guests>\n" for key, value in
                             sorted(accommodated.items(), key=lambda kv: kv[0].split('_')[1]))

    else:
        message = "No accommodations were completed!\n"

    if guests:
        message += f"Guests with no accommodation: {sum(guests)}\n"

    if rooms:
        message += f"Empty rooms: {len(rooms)}"
    return  message



print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
print()
print(accommodate(10, 9, 8, room_307=6, room_802=5))
print()
print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))
