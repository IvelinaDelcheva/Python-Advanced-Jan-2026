numbers = tuple(map(float, input().split()))
numbers_occurrences = {}

for number in numbers:
    if number not in numbers_occurrences:
        numbers_occurrences[number] = numbers.count(number)

for number, occur in numbers_occurrences.items():
    print(f"{number:.1f} - {occur} times")

# [print(f"{number} - {occur} times") for number, occur in numbers_occurrences.items()]
