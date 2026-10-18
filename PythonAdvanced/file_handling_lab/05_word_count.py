import re

with open('words.txt', 'r') as file:
    words = file.read().split(' ')

with open('text.txt', 'r') as file:
    text = file.read()

print(words)
print(text)

words_count = {}

for word in words:
    pattern = rf'\b{word}\b'

    found_words = re.findall(pattern, text, re.IGNORECASE)
    words_count[word] = len(found_words)

lines = [f'{word} - {value}\n' for word, value in dict(sorted(words_count.items(), key=lambda kv: -kv[1])).items()]

with open('other_file.txt', 'w') as file:
    file.writelines(lines)