n = int(input())
odd = set()
even = set()

for row in range(1, n + 1):
    name = sum(ord(ch) for ch in input()) // row

    if name % 2 == 0:
        even.add(name)
    elif name % 2 != 0:
        odd.add(name)

if sum(odd) == sum(even):
    print(*odd.union(even), sep=', ')
elif sum(odd) > sum(even):
    print(*odd.difference(even), sep=', ')
elif sum(even) > sum(odd):
    print(*even.symmetric_difference(odd), sep=', ')