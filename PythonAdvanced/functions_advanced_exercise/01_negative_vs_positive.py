numbers = [int(x) for x in input().split()]

def positive(*args):
    return sum(x for x in numbers if x > 0)

def negative(*args):
    return sum(x for x in numbers if x < 0)

print(negative(numbers))
print(positive(numbers))

if abs(negative(numbers)) > positive(numbers):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
