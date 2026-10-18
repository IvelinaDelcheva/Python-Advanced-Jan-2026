from collections import deque

string_expression = input().split()
result = deque()

operators = {
    "*" : lambda a, b: a * b,
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "/": lambda a, b: round(a // b)
}

for el in string_expression:
    if el not in operators:
        result.append(int(el))
    else:
        while len(result) > 1:
            first_num = result.popleft()
            second_num = result.popleft()
            result.appendleft(operators[el](first_num, second_num))

print(*result)

