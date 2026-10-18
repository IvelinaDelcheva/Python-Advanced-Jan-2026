clothes = list(map(int, input().split()))
rack_capacity = int(input())

number_of_racks = 0

while clothes:
    current_capacity = rack_capacity
    clothes_for_rack = 0
    number_of_racks += 1
    while clothes_for_rack < current_capacity and clothes:
        if clothes_for_rack + clothes[-1] >= current_capacity:
            break
        else:
            clothes_for_rack += clothes.pop()


print(number_of_racks)