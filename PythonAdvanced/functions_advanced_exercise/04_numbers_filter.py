def odd(*args):
    return [x for x in args if x % 2 != 0]

def even(*args):
    return [x for x in args if x % 2 == 0]

maper = {
    'odd': odd,
    'even': even
}

def even_odd_filter(**kwargs):
    result = {}
    for command, nums in kwargs.items():
        result[command] = maper[command](*nums)
    return dict(sorted(result.items(), key=lambda kv: -len(kv[1])))



print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
