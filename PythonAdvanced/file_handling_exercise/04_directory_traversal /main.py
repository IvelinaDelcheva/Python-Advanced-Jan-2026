import os
directory = '../'
files = {}

for element in os.listdir(directory):
    f = os.path.join(directory, element)

    if os.path.isfile(f):
        ext = element.split('.')[-1]
        if ext not in files:
            files[ext] = []
        files[ext].append(element)
    else:
        for el in os.listdir(f):
            filename = os.path.join(f, el)
            if os.path.isfile(filename):
                ext = el.split('.')[-1]
                if ext not  in files:
                    files[ext] = []
                files[ext].append(el)


with open(os.path.join(directory, "report.txt"), 'w') as output:
    for ext, file_names in sorted(files.items()):
        output.write(f'.{ext}\n')
        for file_name in file_names:
            output.write(f'- - - {file_name}\n')
