n = int(input())
longest_intersection = set()

for _ in range(n):
    first_range, second_range = input().split('-')

    first_start, first_end = map(int, first_range.split(','))
    second_start, second_end = map(int, second_range.split(','))

    first_set = set(range(first_start, first_end + 1))
    second_set = set(range(second_start, second_end + 1))

    longest = first_set.intersection(second_set)
    if len(longest) > len(longest_intersection):
        longest_intersection = longest

print(f"Longest intersection is {[num for num in longest_intersection]} with length {len(longest_intersection)}")
