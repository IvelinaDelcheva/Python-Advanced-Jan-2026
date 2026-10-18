from functools import reduce
def add(*args):
    return sum(args)

def subtract(*args):
    return reduce(lambda x, y: x-y, args)

def multiply(*args):
    return reduce(lambda x, y: x*y, args)

def divide(*args):
    return reduce(lambda x, y: x/y, args)

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def operate(operator, *args):
    func = operators[operator]
    return func(*args)


print(operate("/", 50, 5, 2))
print(operate("*", 3, 4))
