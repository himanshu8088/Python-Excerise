from sys import getsizeof
from array import array
from collections import deque
letters = ["a", "b", "c", "d", "e"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
print(zeros)

combined = zeros + letters + matrix
print(combined)

numbers = list(range(20))
print(numbers)

chars = list("Hello World")
print(chars)
print(len(chars))

letters[0] = "A"
print(letters)

print(letters[::2])  # Slicing to get every second letter
print(letters[::-1])  # Reversing the list

numbers = [1, 2, 3]

first, second, third = numbers
print(first, second, third)

# Unpacking a list into variables
first, *others = numbers
print(first, others)

first, *others, last = numbers
print(first, others, last)

items = (0, "a")
index, letter = items
print(index, letter)

# enumerate: returns tuple of index and value
for letter in enumerate(letters):
    print(letter)

# enumerate: returns tuple of index and value
for index, letter in enumerate(letters):
    print(index, letter)

letters.append("k")
print(letters)
letters.insert(0, "-")
print(letters)

letters.pop(0)
print(letters)

letters.remove("b")
print(letters)

del letters[0:3]
print(letters)

if "d" in letters:
    print(f"Found: {letters.index("d")}")
else:
    print(f"Not Found: d")

numbers = [41, 100, 3, 4, 5]
numbers.sort()
print(numbers)
reversedNumbers = sorted(numbers, reverse=True)
print(reversedNumbers)


def sort_item(item):
    return item[1]  # Sort by the second element of the tuple


items = [('product1', 10), ('product2', 5), ('product3', 20)]
items.sort(key=sort_item)
print(items)
# list comprehension to extract second elements
print("list comprehension map:", [item[1] for item in items])
print("list comprehension filter:", [item for item in items if item[1] >= 10])

items.sort(key=lambda item: item[1])
print(items)

x = map(lambda item: item[1], items)
for item in x:
    print(item)

y = list(map(lambda item: item[1], items))
print(y)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Using zip to combine two lists. First element of each list will be paired together, second element of each list will be paired together, and so on.
[print(item) for item in zip("abc", list1, list2)]

# Stack

browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)

last = browsing_session.pop()  # Last in, first out
print(last)
print(browsing_session)
if browsing_session:
    print("redirect", browsing_session[-1])  # Last element in the list

# Queue
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("Queue is empty")

# Array
arr = array('i', [1, 2, 3, 4, 5])
print(arr)
arr.append(6)
print(arr)
arr.pop(0)  # Remove the first element
print(arr)
arr.remove(3)  # Remove the first occurrence of 3
print(arr)
arr.insert(0, 0)  # Insert 0 at the beginning
print(arr)
arr.reverse()  # Reverse the array
print(arr)
print(arr.typecode)

# Set
numbers = {1, 1, 2, 3, 4}
first = set(numbers)
second = {1, 5}

print(first | second)  # Union
print(first & second)  # Intersection
print(first - second)  # Difference
print(first ^ second)  # Symmetric difference

# Dictionary
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
print(point)
point["x"] = 10
point["z"] = 20
print(point)
if "a" in point:
    print("Found")
print(point.get("a", "Not Found"))
del point["x"]  # Remove key "x"
print(point)
for key in point:
    print(key, point[key])

values = {x: x*2 for x in range(5)}
print(values)

# Generator

values = (x * 2 for x in range(10000))
print("gen:", getsizeof(values))  # Size of the generator object

values = [x * 2 for x in range(10000)]
print("gen:", getsizeof(values))  # Size of the list object

# Unpacking operator

numbers = [1, 2, 3, ]
print(*numbers)  # Unpacking the list to print its elements
values = list(range(5))
values = [*range(5), *"Hello"]
print(values)  # Unpacking range and string into a list

first = {"x": 1, "y": 2}
second = {"z": 3, "w": 4}
combined = {**first, **second}  # Merging two dictionaries
print(combined)