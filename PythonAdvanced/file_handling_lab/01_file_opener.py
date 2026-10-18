try:
    file = open('text_01.txt', 'r')
    print('File found')
except FileNotFoundError:
    print('File not found')



