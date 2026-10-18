clothes = list(map(int, input().split()))
rack_capacity = int(input())

number_of_racks = 0

while clothes:
    current_capacity = rack_capacity
    number_of_racks += 1
    while clothes and clothes[-1] <= current_capacity:
        current_capacity -= clothes.pop()


print(number_of_racks)