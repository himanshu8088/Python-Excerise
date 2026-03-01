class Point:
    color = "red"  # Class variable

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y}) drawn.")

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    @classmethod
    def zero(cls):
        return cls(0, 0)


point = Point(1, 2)
point.draw()  # Output: draw
print(type(point))  # <class '__main__.Point'>
print(isinstance(point, Point))  # Output: True

Point.zero().draw()  # Output: Point (0, 0) drawn.

print(Point.color)  # Output: red
Point.color = "blue"  # Change class variable
print(Point.color)
print(point.color)

x = Point(3, 4)
y = Point(5, 6)
print(f"x+y={x + y}")  # Output: Point (8, 10)


# Product class with properties and validation
class Product:

    def __init__(self, name, price, quantity=0, description=None):
        self._name = name
        self._price = price
        self._quantity = quantity
        self._description = description

    # Properties for name
    name = property(lambda self: self._name,
                    lambda self, value: setattr(self, '_name', value))

    def get_price(self):
        return self._price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    # Properties for price
    price = property(get_price, set_price)

    # Properties for description

    def __get_description(self):
        return self._description

    def __set_description(self, value):
        if value is not None and not isinstance(value, str):
            raise ValueError("Description must be a string")
        self._description = value

    description = property(__get_description, __set_description)

    # Properties for quantity
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Quantity cannot be negative")
        self._quantity = value


shirt = Product("Shirt", 19.99, 10, "A nice shirt")
print(shirt.name)  # Output: Shirt
shirt.price = 18.99  # Change price
print(shirt.price)  # Output: 18.99
shirt.quantity = 5  # Change quantity
print(shirt.quantity)  # Output: 5
print(shirt.description)  # Output: A nice shirt
shirt.description = "A very nice shirt"  # Change description
print(shirt.description)  # Output: A very nice shirt
print(shirt.__dict__)
print(shirt._name)  # Accessing private variable directly (not recommended)
shirt.set_price(10)
print(f"New price: {shirt.get_price()}")  # Output: New price: 10


# Inheritance example
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        print(f"{self.name} is walking.")


class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print(f"{self.name} is swimming.")


tom = Mammal('Tom')
tom.eat()
tom.walk()

nemo = Fish('Nemo')
nemo.eat()
nemo.swim()

print(f"isinstance(tom, Animal): {isinstance(tom, Animal)}")  # Output: True
print(f"isinstance(nemo, Animal): {isinstance(nemo, Animal)}")  # Output: True
print("isinstance(tom, Fish):", isinstance(tom, Fish))  # Output: False
print("isinstance(nemo, Mammal):", isinstance(nemo, Mammal))  # Output: False
print("issubclass(Mammal, Animal):", issubclass(Mammal, Animal))  # Output: True
print("issubclass(Fish, Animal):", issubclass(Fish, Animal))  # Output: True
