from collections import deque

cups_capacity = deque(map(int, input().split()))
filled_bottles = deque(map(int, input().split()))

wasted_liters_of_water = 0

while cups_capacity or filled_bottles:

    if not cups_capacity or not  filled_bottles:
        break

    current_cup = cups_capacity[0]
    current_bottle = filled_bottles[-1]
    left_capacity_or_water = current_bottle - current_cup

    if left_capacity_or_water >= 0:
        wasted_liters_of_water += left_capacity_or_water
        cups_capacity.popleft()
        filled_bottles.pop()
    else:
        cups_capacity[0] -= current_bottle
        filled_bottles.pop()

if not cups_capacity:
    print(f'Bottles: ', *reversed(filled_bottles))
else:
    print(f'Cups: ', *cups_capacity)

print(f'Wasted litters of water: {wasted_liters_of_water}')