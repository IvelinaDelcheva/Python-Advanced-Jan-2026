from collections import deque

food_package_weights = [int(food) for food in input().split()]
food_requests = deque(int(food) for food in input().split())
minimum_fulfilled_requests = int(input())
requests_counter = 0

while food_package_weights and food_requests:
    first_food = food_package_weights[-1]
    first_request = food_requests[0]

    if first_food == first_request:
        food_package_weights.pop()
        food_requests.popleft()
        requests_counter += 1

    if first_food > first_request:
        requests_counter += 1
        next_portion = food_package_weights.pop() - food_requests.popleft() - 1
        if next_portion > 0:
            if food_package_weights:
                food_package_weights[-1] += next_portion
            else:
                food_package_weights.append(next_portion)
    if first_food < first_request:
        food_requests.append(food_requests.popleft() - food_package_weights.pop())

if requests_counter >= minimum_fulfilled_requests:
    print(f"Food relief success! Daniel helped {requests_counter} charity points.")

if 0 < requests_counter < minimum_fulfilled_requests:
    print(f"Daniel made a difference! He helped {requests_counter} charity points.")

if requests_counter <= 0:
    print("Daniel could not help much this time. He will try again next week.")

if food_package_weights:
    print(f"Remaining food packages: {'; '.join([str(package) for package in reversed(food_package_weights)])}")

if food_requests:
    print(f"Unmet food requests: {'; '.join([str(request) for request in food_requests])}")


