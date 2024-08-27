class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self._sides = [1] * self.sides_count if len(sides) != self.sides_count else list(sides)
        self._color = list(color)
        self.filled = False

    def get_color(self):
        return self._color

    def _is_valid_color(self, r, g, b):
        return all(0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        if self._is_valid_color(r, g, b):
            self._color = [r, g, b]

    def _is_valid_sides(self, *sides):
        return len(sides) == self.sides_count and all(x > 0 for x in sides)

    def get_sides(self):
        return self._sides

    def set_sides(self, *new_sides):
        if self._is_valid_sides(*new_sides):
            self._sides = list(new_sides)

    def __len__(self):
        return sum(self._sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self._radius = self._sides[0]

    def get_square(self):
        return 3.14 * self._radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self._sides
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *[sides[0]] * self.sides_count)

    def get_volume(self):
        return self._sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

print(len(circle1))

print(cube1.get_volume())