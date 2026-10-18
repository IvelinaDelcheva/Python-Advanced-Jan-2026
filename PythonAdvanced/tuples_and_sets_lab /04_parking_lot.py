number_of_commands = int(input())
parking_lot = set()
for _ in range(number_of_commands):
    command, car = input().split(', ')

    if command == "IN":
        parking_lot.add(car)
    elif command == "OUT":
        if car in parking_lot:
            parking_lot.remove(car)

if parking_lot:
    [print(car) for car in parking_lot]
else:
    print('Parking Lot is Empty')