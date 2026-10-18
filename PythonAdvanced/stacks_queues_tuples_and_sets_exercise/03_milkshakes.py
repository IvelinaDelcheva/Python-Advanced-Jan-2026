from collections import deque

chocolate = [int(choc) for choc in input().split(', ')]
cups_of_milk = deque(int(milk) for milk in input().split(', '))

milkshakes = 0

while chocolate and cups_of_milk:
    if milkshakes == 5:
        break

    last_choc = chocolate[-1]
    first_milk = cups_of_milk[0]

    if last_choc <= 0 and first_milk <= 0:
        chocolate.pop()
        cups_of_milk.popleft()
        continue

    if last_choc <= 0:
        chocolate.pop()
        continue

    if first_milk <= 0:
        cups_of_milk.popleft()
        continue

    if last_choc == first_milk:
        chocolate.pop()
        cups_of_milk.popleft()
        milkshakes += 1
    else:
        cups_of_milk.rotate(-1)
        chocolate[-1] -= 5

success = 'Great! You made all the chocolate milkshakes needed!' if milkshakes == 5 \
    else 'Not enough milkshakes.'
chocolates_left = f"Chocolate: {', '.join(str(choc) for choc in chocolate)}" if chocolate \
    else "Chocolate: empty"
milk_left = f"Milk: {', '.join(str(milk) for milk in cups_of_milk)}" if cups_of_milk \
    else "Milk: empty"

print(success)
print(chocolates_left)
print(milk_left)