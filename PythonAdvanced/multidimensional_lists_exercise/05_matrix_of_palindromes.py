rows, columns = [int(x) for x in input().split()]
start = ord('a')

for r in range(start, start + rows):
    for c in range(columns):
        line = chr(r) + chr(r + c) + chr(r)
        print(line, end=' ')
    print()

