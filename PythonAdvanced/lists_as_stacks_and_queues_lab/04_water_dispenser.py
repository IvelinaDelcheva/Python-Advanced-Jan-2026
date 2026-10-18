from collections import deque

quantity_of_water = int(input())
queue = deque()

command = input()
while command != 'Start':
    names = command
    queue.append(names)
    command = input()

second_command = input()
while second_command != 'End':
    if second_command.isdigit():
        liters_to_get = int(second_command)
        if liters_to_get <= quantity_of_water:
            quantity_of_water -= liters_to_get
            print(f'{queue.popleft()} got water')
        else:
            print(f'{queue.popleft()} must wait')
    elif second_command.startswith('refill'):
        litters_to_refill = second_command.split()[1]
        quantity_of_water += int(litters_to_refill)
    second_command = input()

print(f'{quantity_of_water} liters left')
