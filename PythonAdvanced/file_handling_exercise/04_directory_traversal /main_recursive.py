import os
directory = '../'
files = {}
print(os.getcwd())

def get_files(folder, level=2):
    if level == -1:
        return
    for element in os.listdir(folder):
        f = os.path.join(folder, element)
        if os.path.isfile(f):
            extension = os.path.splitext(element)[1]
            if extension not in files:
                files[extension] = []
            files[extension].append(element)
        else:
            get_files(f, level - 1)

get_files(directory)

with open(os.path.join(directory, "report.txt"), 'w') as output:
    for ext, file_names in sorted(files.items()):
        output.write(f'{ext}\n')
        for file_name in sorted(file_names):
            output.write(f'- - - {file_name}\n')
