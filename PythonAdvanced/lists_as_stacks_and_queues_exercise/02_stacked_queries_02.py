n = int(input())
stack = []

for _ in range(n):
    parts = input().split()
    query = parts[0]

    if query == '1':
        number = int(parts[1])
        stack.append(number)
    elif stack:
        if query == '2':
            stack.pop()
        elif query == '3':
            print(max(stack))
        elif query == '4':
            print(min(stack))

print(*reversed(stack), sep=', ')
