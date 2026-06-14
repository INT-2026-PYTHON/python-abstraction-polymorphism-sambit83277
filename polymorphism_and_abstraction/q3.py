# 3. Abstract Shape with ABC Module
from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    PI = 3.14159

    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return self.PI * self.radius * self.radius

    def perimeter(self):
        return 2 * self.PI * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__("Triangle")
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        # Heron's Formula
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c
try:
    shape = Shape("nope")
except TypeError as e:
    print("Cannot create Shape directly:")
    print(f"TypeError: {e}")

print()
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 5)
]
for shape in shapes:
    print(
        f"{shape.name:<10} -> "
        f"area={shape.area()}, "
        f"perimeter={shape.perimeter()}"
    )