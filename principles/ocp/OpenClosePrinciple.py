from enum import Enum


class Colour(Enum):
    GREEN = 1
    BLUE = 2
    PINK = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


# OLD METHOD ; This is how you need to add new functions in exisitng class
class ProductFilter:
    @staticmethod
    def filter_by_color(products, color):
        for p in products:
            if p.color == color:
                yield p

    @staticmethod
    def filter_by_size(products, size):
        for p in products:
            if p.size == size:
                yield p


# Open Closed Principle

class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return CombineSpecification(self, other)


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return self.color == item.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.color = size

    def is_satisfied(self, item):
        return self.color == item.size


class CombineSpecification(Specification):
    def __init__(self, spec1, spec2):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied(self, item):
        return self.spec1.is_satisfied(item) and self.spec2.is_satisfied(item)


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


apple = Product("Apple", Colour.GREEN, Size.MEDIUM)
tree = Product("Tree", Colour.GREEN, Size.LARGE)
pen = Product("Pen", Colour.BLUE, Size.SMALL)

products = [apple, tree, pen]

print("Product Filter by Old way")
for p in ProductFilter.filter_by_color(products, Colour.GREEN):
    print(f'{p.name}')

green = ColorSpecification(Colour.GREEN)
bf = BetterFilter()
print("Product Filter by New way (COLOR)")
for p in bf.filter(products, green):
    print(f'{p.name}')

print("Product Filter by New way (SIZE)")
small = SizeSpecification(Size.SMALL)
for p in bf.filter(products, small):
    print(f'{p.name}')

print("Product Filter by New way (Combined small and Blue)")
combined = CombineSpecification(small, ColorSpecification(Colour.BLUE))
for p in bf.filter(products, combined):
    print(f'{p.name}')

print("Product Filter by New way (Combined small and Blue) using AND KEYWORD")
# You need to implement __and__
combined = small and ColorSpecification(Colour.BLUE)
for p in bf.filter(products, combined):
    print(f'{p.name}')
