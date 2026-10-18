from collections import deque

colors = deque(color for color in input().split())

main_colors = ["red", "yellow", "blue"]
all_colors = ["red", "yellow", "blue", "orange", "purple", "green"]
secondary_colors = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue']
}


collected_colors = []
while colors:
    if len(colors) == 1:
        substr = colors[0]
    else:
        substr =  [colors[0] + colors[-1], colors[-1] + colors[0]]

    for color in all_colors:
        if color in substr:
            collected_colors.append(color)
            colors.popleft()
            colors.pop()



for colcol in collected_colors:
    if colcol in secondary_colors:
        subset = set(secondary_colors[colcol])
        if not subset.issubset(collected_colors):
            collected_colors.remove(colcol)

print(collected_colors)





