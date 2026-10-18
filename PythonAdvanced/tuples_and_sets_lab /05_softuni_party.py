number_of_guests = int(input())
guests = set()

for _ in range(number_of_guests):
    res_code = input()
    guests.add(res_code)

command = input()
while command != 'END':
    res_come = command
    if res_come in guests:
        guests.remove(res_come)
    command = input()

print(len(guests))
print('\n'.join(sorted(guests)))