from collections import deque

petrol_pumps = int(input())
petrol_distance = deque()

starting_point = 0
stops = 0

for _ in range(petrol_pumps):
    petrol, distance = map(int, input().split())
    petrol_distance.append((petrol, distance))

while stops < petrol_pumps:
    tank = 0
    for curr_fuel, dist in petrol_distance:
        tank += curr_fuel
        if tank < dist:
            petrol_distance.rotate(-1)
            starting_point += 1
            stops = 0
            break
        tank -= dist
        stops += 1

print(starting_point)