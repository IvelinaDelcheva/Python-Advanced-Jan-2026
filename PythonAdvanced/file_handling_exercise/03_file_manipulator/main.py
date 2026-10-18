import os

abs_path = os.path.abspath(__file__)
dir_name = os.path.dirname(abs_path)

while (line := input()) != 'End':

    command, file_name, *args = line.split('-')

    if command == 'Create':
        with open(file_name, 'w') as file:
            pass
    elif command == 'Add':
        content = args[0]
        with open(file_name, 'a') as file:
            file.write(f'{content}\n')
    elif command == 'Replace':
        file_path = os.path.join(dir_name, file_name)
        if os.path.exists(file_path):
            with (open(file_name, 'r+') as file):
                text = file.read()
                file.seek(0)
                file.truncate(0)
                file.write(text.replace(args[0], args[1]))

        else:
            print("An error occurred")

    elif command == 'Delete':
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")



