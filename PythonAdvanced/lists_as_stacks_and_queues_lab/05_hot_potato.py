from collections import deque

names = deque(input().split())
n_toss = int(input()) - 1

while len(names) > 1:
    names.rotate(-n_toss)
    print(f'Removed {names.popleft()}')

print(f'Last is {names[0]}')