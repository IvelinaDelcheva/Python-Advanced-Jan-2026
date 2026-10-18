names = int(input())
unique = set()

for _ in range(names):
    name = input()
    unique.add(name)

for name in unique:
    print(name)