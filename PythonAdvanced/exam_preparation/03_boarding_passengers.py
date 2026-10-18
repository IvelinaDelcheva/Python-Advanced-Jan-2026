def boarding_passengers(ship_capacity: int, *args):
    boarding_details = {}
    group_guests = 0
    message = ''
    for passengers, program in args:
        if ship_capacity <= 0:
            break
        if ship_capacity >= passengers:
            ship_capacity -= passengers
            if not program in boarding_details.keys():
                boarding_details[program] = 0
            boarding_details[program] += passengers
            group_guests += 1
        else:
            continue
    message += "Boarding details by benefit plan:\n"
    for plan, guests in sorted(boarding_details.items(), key=lambda kv: (-kv[1], kv[0])):
        message += f"## {plan}: {guests} guests\n"
    if group_guests == len(args):
        message += "All passengers are successfully boarded!"
    elif ship_capacity <= 0:
        message += "Boarding unsuccessful. Cruise ship at full capacity."
    elif group_guests < len(args):
        message += f"Partial boarding completed. Available capacity: {ship_capacity}."
    return message


print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'),
                          (10, 'Gold')))
print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'),
                          (20, 'Diamond')))
