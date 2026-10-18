from collections import deque

quantity_of_food = int(input())
orders = deque(int(quantity) for quantity in input().split())

print(max(orders))

while orders and orders[0] <= quantity_of_food:
    quantity_of_food -= orders.popleft()

if orders:
    print(f'Orders left: ', *orders)
else:
    print(f'Orders complete')