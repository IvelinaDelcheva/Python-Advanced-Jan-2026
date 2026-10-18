text = input()
unique = set(letter for letter in text)
for letter in sorted(unique):
    print(f'{letter}: {text.count(letter)} time/s')