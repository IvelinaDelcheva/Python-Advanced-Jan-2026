import string

with open('text.txt', 'r') as file:
    lines = file.readlines()

write_lines = []
for index, line in enumerate(lines):
    letters_count = len([ch for ch in line if ch.isalpha()])
    punctuation_count = len([ch for ch in line if ch in string.punctuation])
    write_lines.append(f'Line {index}: {line.rstrip('\n')} ({letters_count})({punctuation_count})\n')

with open('output.txt', 'w') as output:
    output.writelines(write_lines)