first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())

for _ in range(int(input())):
    tokens = input().split()
    command = ' '.join(tokens[:2])
    numbers = [int(x) for x in tokens[2:]]

    if command == 'Add First':
        first_sequence.update(numbers)
    elif command == 'Add Second':
        second_sequence.update(numbers)
    elif command == 'Remove First':
        [first_sequence.remove(el) for el in numbers if el in first_sequence]
    elif command == 'Remove Second':
        [second_sequence.remove(el) for el in numbers if el in second_sequence]
    elif command == 'Check Subset':
        is_subset = (first_sequence.issubset(second_sequence)
                     or second_sequence.issubset(first_sequence))
        print(is_subset)

print(*sorted(first_sequence), sep=', ')
print(*sorted(second_sequence), sep=', ')