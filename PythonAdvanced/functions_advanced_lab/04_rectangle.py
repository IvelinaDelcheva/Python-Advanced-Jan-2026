def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"

    def	area(l, w):
        return l * w

    def perimeter(l, w):
        return 2 * l + 2 * w

    return f"Rectangle area: {area(length, width)}\nRectangle perimeter: {perimeter(length, width)}"


print(rectangle(2, 10))
print(rectangle('2', 10))

