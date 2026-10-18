from collections import deque

packages_weight = [int(x) for x in input().split()]
couriers_capacities = deque(int(x) for x in input().split())

total_weight_packages = 0

while packages_weight and couriers_capacities:

    package = packages_weight[-1]
    courier = couriers_capacities[0]
    if courier >= package:
        total_weight_packages += package
        packages_weight.pop()
        courier -= (package * 2)
        if courier > 0:
            couriers_capacities[0] -= courier
            couriers_capacities.rotate(-1)
        else:
            couriers_capacities.popleft()
    elif courier < package:
        package -= courier
        total_weight_packages += couriers_capacities.popleft()
        packages_weight[-1] = package

print(f"Total weight: {total_weight_packages} kg")
if not packages_weight and not couriers_capacities:
    print(f"Congratulations, all packages were delivered successfully by the couriers today.")
elif packages_weight and not couriers_capacities:
    print(
        f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(str(x) for x in packages_weight)}")
elif couriers_capacities and not packages_weight:
    print(
        f"Couriers are still on duty: {', '.join(str(x) for x in couriers_capacities)} but there are no more packages to deliver.")
