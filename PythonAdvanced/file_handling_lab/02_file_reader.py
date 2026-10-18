file = open('numbers.txt', 'r')
# sum = 0
#
# for num in file:
#     sum += int(num)
#
# print(sum)
total_sum = sum(int(num) for num in file)
print(total_sum)
