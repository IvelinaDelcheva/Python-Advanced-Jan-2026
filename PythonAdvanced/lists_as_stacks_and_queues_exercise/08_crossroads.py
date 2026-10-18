from collections import deque

green_light = int(input())
free_window  = int(input())
cars = deque()
car_passed = 0
green_light_stop = False
command = input()
while command != 'END':

    if command != 'green':
        car = command
        cars.append(car)
    elif command == 'green':

        current_green = green_light
        left_green_window = 0
        while cars:
            current_car = cars.popleft()

            if len(current_car) <= current_green:
                car_passed += 1
                current_green -= len(current_car)
                left_green_window = current_green + free_window
            elif left_green_window >= len(current_car):
                left_green_window = current_green + free_window
                current_green = 0
                green_light_stop = True
                left_green_window -= len(current_car)
                car_passed += 1
            elif green_light_stop:
                continue
            else:
                print("A crash happened!")
                print(f"{current_car} was hit at {current_car[left_green_window]}.")
                exit()

    command = input()

else:
    print("Everyone is safe.")
    print(f"{car_passed} total cars passed the crossroads.")

