n = int(input())
longest_intersection = set()

def process_input(input_range: str) -> set:
    start, end = map(int, input_range.split(','))
    return set(range(start, end + 1))


for _ in range(n):
    first_range, second_range = input().split('-')

    first_set = process_input(first_range)
    second_set = process_input(second_range)

    longest = first_set.intersection(second_set)
    if len(longest) > len(longest_intersection):
        longest_intersection = longest

print(f"Longest intersection is {[num for num in longest_intersection]} with length {len(longest_intersection)}")
