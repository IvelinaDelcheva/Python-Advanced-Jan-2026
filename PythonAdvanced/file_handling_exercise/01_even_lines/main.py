with open('text.txt', 'r') as file:
    text = file.readlines()

symbols = {"-", ",", ".", "!", "?"}

for index, line in enumerate(text):
    if index % 2 == 0:
        for symbol in symbols:
            if symbol in line:
                line = line.replace(symbol, '@')
        print(' '.join(line.rstrip('\n').split(' ')[::-1]))