def concatenate(*args, **kwargs):
    result_str = ''
    for str in args:
        result_str += str
    for key, value in kwargs.items():
        if key in result_str:
            result_str = result_str.replace(key, value)
    return result_str

print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
