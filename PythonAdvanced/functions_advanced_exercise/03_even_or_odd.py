def even(*args):
    return [num for num in args if num % 2 == 0]

def odd(*args):
    return [num for num in args if num % 2 != 0]

def even_odd(*args):
    func = args[-1]
    return commands[func](*args[:-1])

commands = {
    'even': even,
    'odd': odd
}


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
