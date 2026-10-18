from collections import deque

bees = deque(int(bee) for bee in input().split())
nectar = [int(nectar) for nectar in input().split()]
symbols = deque(symbol for symbol in input().split())

total_honey = 0

operators = {
    "+" : lambda a, b: a + b,
    "-": lambda a, b: abs(a - b),
    "*":  lambda a, b: a * b,
    "/": lambda a, b: a / b
}

while bees and nectar:

    first_bee = bees[0]
    last_nectar = nectar[-1]

    if last_nectar >= first_bee:
        first_symbol = symbols.popleft()
        if first_symbol == '/' and last_nectar == 0:
            bees.popleft()
            nectar.pop()
            continue

        total_honey += operators[first_symbol](bees.popleft(), nectar.pop())
    elif last_nectar < first_bee:
        nectar.pop()

left_bees = f"Bees left: {', '.join(str(bee) for bee in bees)}" if bees else ""
nectar_left = f"Nectar left: {', '.join(str(nec) for nec in nectar)}" if nectar else ""

print(f"Total honey made: {total_honey}")
if left_bees:
    print(left_bees)
if nectar_left:
    print(nectar_left)

