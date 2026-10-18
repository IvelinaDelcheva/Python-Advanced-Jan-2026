import os

absolute_path = os.path.abspath(__file__)
path_to_dir = os.path.dirname(absolute_path)

file_path = os.path.join(path_to_dir, 'my_first_file.txt')
try:
    os.remove(file_path)
except FileNotFoundError:
    print('File already deleted!')