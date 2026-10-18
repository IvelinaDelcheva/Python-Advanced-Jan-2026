# usernames = int(input())
# unique = set()
#
# for _ in range(usernames):
#     name = input()
#     unique.add(name)


# unique = set(input() for _ in range(int(input())))
# print(*unique, sep='\n')

print(*set(input() for _ in range(int(input()))), sep='\n')
