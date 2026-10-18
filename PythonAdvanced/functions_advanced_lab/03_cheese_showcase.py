def sorting_cheeses(**kwargs):
    sorted_cheese = sorted(kwargs.items(), key = lambda kv: (-len(kv[1]), kv[0]))
    result = ''
    for cheese, pieces in sorted_cheese:
        result += f'{cheese}\n'
        for piece in sorted(pieces, key=lambda p: -p):
            result += f'{piece}\n'

    return result

print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)

