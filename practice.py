from sys import getsizeof
from array import array
from collections import deque
from functools import reduce
print("\n--- Array of Strings ---")
letters = ["a", "b", "c", "d", "e"]
print("letters:", letters)

print("\n--- Matrix (2D List) ---")
matrix = [[0, 1], [2, 3]]
print("matrix:", matrix)

print("\n--- List of Ones ---")
ones = [1] * 5
print("ones:", ones)

print("\n--- Combined List ---")
combined = letters + matrix + ones
print("combined:", combined)

print("\n--- Range of Numbers ---")
numbers = list(range(10))
print("numbers:", numbers)

print("\n--- List of Characters ---")
chars = list("hello world")
print("chars:", chars)

print("\n--- Length of Characters List ---")
print("length of chars - ", chars, "is", len(chars))

print("\n--- Modifying Lists ---")
print("letters before modification:", letters)
letters[0] = "A"
print("letters after modification:", letters)

print("\n--- Slicing Lists ---")
every_second_char = letters[::2]
print("Slicing to get every second element of letters", letters,
      # Slicing to get every second element
      "using letters[::2] is", every_second_char)

print("\n--- Reversing Lists ---")
reversed_letters = letters[::-1]
print("Reversing letters:", reversed_letters)

print("\n--- Unpacking Lists ---")
numbers = [1, 2, 3, 4, 5]
first, second, third, *others = numbers
print("first:", first)
print("second:", second)
print("third:", third)
print("others:", others)

print("\n--- Unpacking with Last Element ---")
first, *others, last = numbers
print("first:", first)
print("others:", others)
print("last:", last)

print("\n--- Unpacking Tuples ---")
items = (0, "a")
index, letter = items
print("index:", index)
print("letter:", letter)

print("\n--- Enumerating Lists ---")
for index, letter in enumerate(letters):
    print("index:", index, "letter:", letter)

print("\n--- Modifying Lists with append, insert, pop, remove, del ---")
print("letters before modifications:", letters)
letters.append("k")
print("letters after append('k'):", letters)
letters.insert(0, "-")
print("letters after insert(0, '-'):", letters)
letters.pop(0)
print("letters after pop(0):", letters)
letters.remove("b")
print("letters after remove('b'):", letters)
del letters[0:3]
print("letters after del letters[0:3]:", letters)

print("\n--- Checking for Elements in Lists ---")
if "d" in letters:
    print(f"Found: {letters.index('d')}")
else:
    print("Not Found: d")

print("\n--- Sorting Lists ---")
numbers = [41, 100, 3, 4, 5]
sorted_numbers = sorted(numbers)
print("Ascending numbers:", sorted_numbers)
descending_numbers = sorted(numbers, reverse=True)
print("Descending numbers:", descending_numbers)


def sort_item(item):
    first, second = item
    return second  # Sort by the second element of the tuple


items = [(1, 'b'), (2, 'a'), (3, 'c')]
sorted_items = sorted(items, key=sort_item)
print("Items sorted by second element:", sorted_items)

print("\n--- Sorting with Lambda Function ---")
sorted_items_using_lambda = sorted(items, key=lambda item: item[1])
print("Items sorted by second element using lambda:", sorted_items_using_lambda)

print("\n--- List Comprehensions ---")
squared_numbers = [x**2 for x in numbers]
print("Squared numbers:", squared_numbers)
event_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers:", event_numbers)
pairs = [(x, x**2) for x in numbers]
print("Pairs of numbers and their squares:", pairs)
list_comprehension_map = [item[1] for item in items]
print("List comprehension map (second elements):", list_comprehension_map)
list_comprehension_filter = [item for item in items if item[0] > 1]
print("List comprehension filter (first element > 1):", list_comprehension_filter)

print("\n--- Using map with Lambda Function ---")
mapped_items = map(lambda item: item[1], items)
print("Mapped items (second elements):", list(mapped_items))

print("\n--- Using filter with Lambda Function ---")
filtered_items = filter(lambda item: item[0] > 1, items)
print("Filtered items (first element > 1):", list(filtered_items))

print("\n--- Using reduce with Lambda Function ---")
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print("Product of numbers using reduce:", product)

print("\n--- Using zip to Combine Lists ---")
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd']
# strict=False allows for different lengths of lists
zipped = zip(list1, list2, strict=False)
print("Zipped list:", list(zipped))

print("\n--- Using zip to Combine Multiple Lists ---")
list3 = [True, False, True]
zipped_multiple = zip(list1, list2, list3)
print("Zipped multiple lists:", list(zipped_multiple))

print("\n--- Stack Example ---")
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print("Browsing session stack:", browsing_session)
last = browsing_session.pop()  # Last in, first out
print("Last browsing session popped:", last)

print("\n--- Queue Example ---")
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print("Queue:", queue)
first = queue.popleft()  # First in, first out
print("First item in queue popped:", first)

print("\n--- Dictionary Example ---")
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Dictionary:", my_dict)
print("Value for key 'b':", my_dict['b'])
print("Keys in dictionary:", list(my_dict.keys()))
print("Values in dictionary:", list(my_dict.values()))
print("Items in dictionary:", list(my_dict.items()))
print("Check if 'a' in dictionary:", 'a' in my_dict)
del my_dict['a']
print("Dictionary after deleting key 'a':", my_dict)
for key in my_dict:
    print(f"Key: {key}, Value: {my_dict[key]}")

print("\n--- Set Example ---")
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)
my_set.add(6)
print("Set after adding 6:", my_set)
my_set.remove(3)
print("Set after removing 3:", my_set)
print("Check if 4 in set:", 4 in my_set)

print("\n--- Tuple Example ---")
my_tuple = (1, 2, 3)
print("Tuple:", my_tuple)
print("First element of tuple:", my_tuple[0])
print("Length of tuple:", len(my_tuple))

print("\n--- Array Example ---")
my_array = array('i', [1, 2, 3, 4, 5])
print("Array:", my_array)
my_array.append(6)
print("Array after appending 6:", my_array)
my_array.pop(0)  # Remove the first element
print("Array after popping first element:", my_array)
my_array.remove(3)  # Remove the first occurrence of 3
print("Array after removing 3:", my_array)
my_array.insert(0, -1)  # Insert -1 at the beginning
print("Array after inserting -1 at the beginning:", my_array)
my_array.reverse()  # Reverse the array
print("Array after reversing:", my_array)
print("Typecode of array:", my_array.typecode)
print("Array as list:", my_array.tolist())
print("Array length:", len(my_array))
print("Array count of 2:", my_array.count(2))
print("Array index of 4:", my_array.index(4))
print("Array slice [1:4]:", my_array[1:4])
print("Array concatenation:", my_array + array('i', [7, 8, 9]))
print("Array repetition:", my_array * 2)
print("Array contains 5:", 5 in my_array)
print("Array contains 10:", 10 in my_array)
print("Array min:", min(my_array))
print("Array max:", max(my_array))
print("Array sum:", sum(my_array))
print("Array mean:", sum(my_array) / len(my_array))
print("Array sorted:", sorted(my_array))
print("Array reversed:", list(reversed(my_array)))
print("Array as string:", str(my_array))
print("Array representation:", repr(my_array))
print("Array bytes:", my_array.tobytes())
print("Array from bytes:", array('i', my_array.tobytes()))
print("Array from list:", array('i', [1, 2, 3, 4, 5]))

print("\n--- Deque Example ---")
my_deque = deque([1, 2, 3])
print("Deque:", my_deque)
my_deque.append(4)
print("Deque after appending 4:", my_deque)
my_deque.appendleft(0)
print("Deque after appending 0 to the left:", my_deque)
my_deque.pop()
print("Deque after popping from the right:", my_deque)
my_deque.popleft()
print("Deque after popping from the left:", my_deque)
my_deque.extend([5, 6, 7])
print("Deque after extending with [5, 6, 7]:", my_deque)
my_deque.extendleft([-2, -1])
print("Deque after extending left with [-2, -1]:", my_deque)
my_deque.rotate(2)
print("Deque after rotating right by 2:", my_deque)
my_deque.rotate(-2)
print("Deque after rotating left by 2:", my_deque)
my_deque.clear()
print("Deque after clearing:", my_deque)

print("\n--- Set Operations Example ---")
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Set A:", set_a)
print("Set B:", set_b)
print("Union of A and B:", set_a | set_b)
print("Intersection of A and B:", set_a & set_b)
print("Difference of A and B:", set_a - set_b)
print("Symmetric difference of A and B:", set_a ^ set_b)

print("\n--- Dictionary Comprehension Example ---")
squared_dict = {x: x**2 for x in range(5)}
print("Dictionary comprehension (squared numbers):", squared_dict)

print("\n--- Generator Expression Example ---")
squared_gen = (x**2 for x in range(5))
print("Generator expression (squared numbers):", list(squared_gen))

print("\n--- Using getsizeof to Compare Memory Usage ---")
squared_gen = (x**2 for x in range(10000))
print("Size of generator object:", getsizeof(squared_gen))
squared_list = [x**2 for x in range(10000)]
print("Size of list object:", getsizeof(squared_list))

print("\n--- Unpacking with * Operator Example ---")
numbers = [1, 2, 3, 4, 5]
print("Unpacking numbers with * operator:", *numbers)
values = [*range(5), *"Hello"]
print("Unpacking range and string into a list:", values)
first = [1, 2, 3]
second = [4, 5, 6]
combined = [*first, *second]
print("Combined list using unpacking:", combined)

print("\n--- CONDITIONS ---")

print("\n--- Using if, elif, else ---")
temp = 10
if temp > 30:
    print("It's a hot day")
elif temp >= 20 and temp <= 30:
    print("It's a nice day")
else:
    print("It's a cold day")

print("\n--- Chaining Comparison Operators ---")
age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"

print(message)

print("\n--- Using Ternary Operator ---")
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)

print("\n--- Using Logical Operators ---")
if age >= 18 and age < 65:
    print("Eligible for work")
else:
    print("Not eligible for work")
if age < 18 or age >= 65:
    print("Not eligible for work")
else:
    print("Eligible for work")
if not (age < 18 or age >= 65):
    print("Eligible for work")
else:
    print("Not eligible for work")
if 18 <= age < 65:
    print("Eligible for work")
if not (age < 18 or age >= 65):
    print("Eligible for work")

print("\n--- Comparison Operators ---")
print("bag" > "apple")  # After sort Bag comes first, hence True
print("10" == 10)  # False
print(10 == 10)  # True
print(10 != 5)  # True
print(10 > 5)  # True
print(10 < 20)  # True
print(10 >= 10)  # True
print(10 <= 9)  # False

print("\n--- Strings ---")

name = "John Doe"
print("Name:", name)
print("Length of name:", len(name))
print("First character:", name[0])
print("Last character:", name[-1])
print("From index 0 to 4 - Substring (0:4):", name[0:4])
print("From index 5 to end - Substring (5:):", name[5:])
print("From start to index 3 - Substring (:3):", name[:3])
print("Every second character - Substring (0::2):", name[0::2])
print("Reversed name - Substring (::-1):", name[::-1])
print("Uppercase name:", name.upper())
print("Lowercase name:", name.lower())
print("Title case name:", name.title())
print("Count of 'o' in name:", name.count('o'))
print("Index of 'D' in name:", name.find('D'))
print("Replace 'John' with 'Jane':", name.replace('John', 'Jane'))
print("Split name into parts:", name.split())
print("Check if name starts with 'John':", name.startswith('John'))
print("Check if name ends with 'Doe':", name.endswith('Doe'))
print("Check if 'Doe' in name:", 'Doe' in name)
print("Check if 'Smith' in name:", 'Smith' in name)
print("Concatenate name with ' Jr.':", name + " Jr.")
print("Formatted string with name:", f"My name is {name}.")
print("Formatted string with name and length:",
      f"My name is {name} and it has {len(name)} characters.")
print("String representation of name:", str(name))
print("String representation of name using repr:", repr(name))
print("String with escaped characters:", "Hello\nWorld")
print("Raw string with escaped characters:", r"Hello\nWorld")
print("Multiline string:\nThis is a\nmultiline string.")
print("Multiline string with triple quotes:\nThis is a\nmultiline string.")
print("String with tabs:\tHello\tWorld")

print("\n--- Type Conversion ---")
print("String to integer:", int("123"))
print("String to float:", float("3.14"))
print("Integer to string:", str(123))
print("Float to string:", str(3.14))
print("String to boolean (non-empty string):", bool("Hello"))
print("String to boolean (empty string):", bool(""))
print("Integer to boolean (non-zero):", bool(1))
print("Integer to boolean (zero):", bool(0))
print("Float to boolean (non-zero):", bool(3.14))
print("Float to boolean (zero):", bool(0.0))
print("List to string:", str([1, 2, 3]))
print("String to list:", list("Hello"))
print("Tuple to string:", str((1, 2, 3)))
print("String to tuple:", tuple("Hello"))
print("Set to string:", str({1, 2, 3}))
print("String to set:", set("Hello"))
print("Dictionary to string:", str({'a': 1, 'b': 2}))
print("String to dictionary (using eval):", eval("{'a': 1, 'b': 2}"))
print("String to dictionary (using json):",
      __import__('json').loads('{"a": 1, "b": 2}'))
print("String to integer with base 16:", int("1A", 16))
print("String to integer with base 2:", int("1010", 2))

print("\n--- Iteration ---")

print("Sending a message")
for number in range(3):
    print("Attempt", number+1, (number+1) * ".")

for number in range(1, 4):
    print("Attempt", number, number * ".")

successful = False
for number in range(3):
    print("Atempt", number+1)
    if successful:
        print("Successful")
        break
    print("Attempting...")
else:
    print("Unsuccessful after 3 attempts")

print(type(range(5)))

for x in range(5):
    print(x, end=" ")
print()

while number > 0:
    print(number)
    number -= 1

print("\n--- Functions ---\n")


def greet():
    print("Hi there")
    print("Welcome aboard!")


greet()


def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard!")


greet("Himanshu", "Soni")


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Himanshu")
print(message)


def increment(number, by):
    return number + by


print(increment(2, 1))
print(increment(number=2, by=1))
print(increment(by=1, number=2))


def multliply(x, y):
    return x * y


print("Directly multiplied:", multliply(2, 3))


def multliply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("Multiplied using for loop:", multliply(2, 3, 4, 5, 6))


def multliply(*numbers):
    return reduce(lambda x, y: x * y, numbers, 1)


print("Multiplied using reduce:", multliply(2, 3, 4, 5, 6))


def save_user(**user):
    print(user)
    print(user['name'])
    print(user['age'])
    print(user.get('id', 'No ID provided'))


save_user(id=1, name="Himanshu", age=22)

print("\n--- Classes ---\n")
class Point:
    color = "red"  # Class variable

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Method to draw the point
    def draw(self):
        print(f"Point ({self.x}, {self.y}) drawn.")

    # Operator overloading for addition (+)
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    @classmethod
    def zero(cls):
        return cls(0, 0)

    @staticmethod
    def distance(point1, point2):
        return ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5

    @property
    def createdAt(self):
        return self._createdAt

    @createdAt.setter
    def createdAt(self, value):
        self._createdAt = value

    @createdAt.deleter
    def createdAt(self):
        del self._createdAt


point = Point(1, 2)
point.draw()  # Output: Point (1, 2) drawn.

pointSum = point + Point(3, 4)
print("Point(1,2) + Point(3,4) =", pointSum.draw())  # Output: Point (4, 6)
point.__add__(Point(3, 4)).draw()  # Output: Point (4, 6) drawn.
print(point)  # Output: (1, 2)

Point.zero().draw()  # Output: Point (0, 0) drawn.
print("Distance between (1,2) and (4,6):", point.distance(
    Point(1, 2), Point(4, 6)))  # Output: 5.0

point.createdAt = "2024-06-01"
print("Point created at:", point.createdAt)

del point.createdAt
print("Point created at after deletion:", getattr(
    point, 'createdAt', 'Attribute deleted'))

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

    price = property(get_price, set_price)

    def get_quantity(self):
        return self._quantity

    def set_quantity(self, value):
        if value < 0:
            raise ValueError("Quantity cannot be negative")
        self._quantity = value

    quantity = property(get_quantity, set_quantity)

    def get_description(self):
        return self._description

    def set_description(self, value):
        if value is not None and not isinstance(value, str):
            raise ValueError("Description must be a string or None")
        self._description = value

    description = property(get_description, set_description)

    def __str__(self):
        return f"Product: name={self.name}, price={self.price}, quantity={self.quantity}, description={self.description}"


shirt = Product("Shirt", 29.99, 100, "A nice shirt")
# Output: Product: name=Shirt, price=29.99, quantity=100, description=A nice shirt
print(shirt)
print(shirt.name)  # Output: Shirt
shirt.price = 24.99  # Change price
print(shirt.price)  # Output: 24.99
shirt.quantity = 50  # Change quantity
print(shirt.quantity)  # Output: 50
print(shirt.description)  # Output: A nice shirt
shirt.description = "A very nice shirt"  # Change description
print(shirt.description)  # Output: A very nice shirt
print(shirt.__dict__)
print("Attempting to set negative price...")
try:
    shirt.price = -10
except ValueError as e:
    print("Error:", e)

print("\n--- Inheritance ---\n")


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"


print(Animal("Generic Animal").speak())  # Output: Generic Animal makes a sound


class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"


print(Dog("Buddy").speak())  # Output: Buddy barks

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        return f"{self.name} meows and is {self.color}"

print(Cat("Whiskers", "black").speak())  # Output: Whiskers meows and is black
    
