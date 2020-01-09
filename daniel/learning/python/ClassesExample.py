class Rectanle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


r1 = Rectanle(10, 20)

print("Height", r1.height)
print("Width :", r1.width)
r1.width = 100
print("Height", r1.height)
print("Width :", r1.width)


class Rectanle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width * self.height)


r1 = Rectanle(10, 20)
print("Area : ", r1.area())
print("Perimeter : ", r1.perimeter())
print("String value", str(r1))
print("Representation value : ", r1)


class Rectanle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width * self.height)

    def __str__(self):
        return 'Rectangle : Width={0}, Height={1}'.format(self.width, self.height)


r2 = Rectanle(100, 200)
print("R2 String value", str(r2))
print("R2 Representation value : ", r2)


class Rectanle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width * self.height)

    def __str__(self):
        return 'Rectangle : Width={0}, Height={1}'.format(self.width, self.height)

    def __repr__(self):
        return 'Rectangle({0},{1}'.format(self.width, self.height)


r3 = Rectanle(100, 200)
r4 = Rectanle(100, 200)
print("R3 String value", str(r3))
print("R3 Representation value : ", r3)

if r3 is not r4:
    print("False")
else:
    print("True")

if r3 == r4:
    print("True")
else:
    print("False")


class Rectanle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width * self.height)

    def __str__(self):
        return 'Rectangle : Width={0}, Height={1}'.format(self.width, self.height)

    def __repr__(self):
        return 'Rectangle({0},{1}'.format(self.width, self.height)

    def __eq__(self, other):
        if isinstance(other, Rectanle):
            return self.height == other.height and self.width == other.width
        else:
            return False


r3 = Rectanle(100, 200)
r4 = Rectanle(100, 200)

if r3 is not r4:
    print("False")
else:
    print("True")

if r3 == r4:
    print("True")
else:
    print("False")


class Rectanle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width * self.height)

    def __str__(self):
        return 'Rectangle : Width={0}, Height={1}'.format(self.width, self.height)

    def __repr__(self):
        return 'Rectangle({0},{1}'.format(self.width, self.height)

    def __eq__(self, other):
        if isinstance(other, Rectanle):
            return self.height == other.height and self.width == other.width
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectanle):
            return self.area() < other.area()
        else:
            return NotImplementedError


r3 = Rectanle(100, 200)
r4 = Rectanle(10, 200)

print(r3 < r4)
print(r4 < r3)

print(r3 > r4)  # Greate than will work. Python can understand from __lt__


# print(r1 <= r4) #will not work give you error

# Restrict setting values. Using private variables


class Rectanle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_width(self):
        return self._width

    def set_width(self, width):
        if width > 0:
            self._width = width
        else:
            raise ValueError("Negative values are not permitted")

    def get_height(self):
        return self._height

    def set_height(self, height):
        if height >= 0:
            self._height = height
        else:
            raise ValueError("Negative values are not permitted")

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width * self._height)

    def __str__(self):
        return 'Rectangle : Width={0}, Height={1}'.format(self._width, self._height)

    def __repr__(self):
        return 'Rectangle({0},{1}'.format(self._width, self._height)

    def __eq__(self, other):
        if isinstance(other, Rectanle):
            return self._height == other._height and self._width == other._width
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectanle):
            return self.area() < other.area()
        else:
            return NotImplementedError


r1 = Rectanle(10, 30)
print(r1)
r1.set_height(60)
print(r1)
# r1.set_width(-100) # not allowed
print(r1)


# getter setter is not recommended in python. Instead use @property


class Rectanle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width > 0:
            self._width = width
        else:
            raise ValueError("Negative values are not permitted")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height >= 0:
            self._height = height
        else:
            raise ValueError("Negative values are not permitted")

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width * self._height)

    def __str__(self):
        return 'Rectangle : Width={0}, Height={1}'.format(self._width, self._height)

    def __repr__(self):
        return 'Rectangle({0},{1}'.format(self._width, self._height)

    def __eq__(self, other):
        if isinstance(other, Rectanle):
            return self._height == other._height and self._width == other._width
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectanle):
            return self.area() < other.area()
        else:
            return NotImplementedError


r1 = Rectanle(100, 300)
print(r1.height)
r1.height = 600
print(r1.height)
print(r1)


# once we define @property then we can use that as variable anywhere


class Rectanle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width > 0:
            self._width = width
        else:
            raise ValueError("Negative values are not permitted")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height >= 0:
            self._height = height
        else:
            raise ValueError("Negative values are not permitted")

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width * self.height)

    def __str__(self):
        return 'Rectangle : Width={0}, Height={1}'.format(self.width, self.height)

    def __repr__(self):
        return 'Rectangle({0},{1}'.format(self.width, self.height)

    def __eq__(self, other):
        if isinstance(other, Rectanle):
            return self.height == other.height and self.width == other.width
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectanle):
            return self.area() < other.area()
        else:
            return NotImplementedError


r1 = Rectanle(110, 310)
print(r1.height)
r1.height = 610
# r1 = Rectanle(-110,310) # Not allowed
