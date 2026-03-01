course = 'Python Programming'
message = """
Welcome to the course: {}   
"""

print(message.format(course))  # Welcome to the course: Python Programming

print(course[0])  # P
print(course[-1])  # g
print(course[0: 3])  # Pyt
print(course[0:])  # Python Programming
print(course[:3])  # Pyt
print(course[:])  # Python Programming
print('Python "Programming"')  # Python "Programming"
print("Python \"Programming\"")  # Python "Programming"

fruit = 'apple'
print(fruit[1: -2]) ## pp

first = 'Himanshu'
last = 'Soni'
full = first + ' ' + last
print(full)  # Himanshu Soni
full = f"{first} {last}"
print(full)  # Himanshu Soni
full = f"{len(first)} {len(last)}"
print(full)  # 8 4

print(course.upper())  # PYTHON PROGRAMMING
print(course.lower())  # python programming
print(course.title())  # Python Programming
print(course.rstrip())  # Python Programming
print(course.find('Pro'))  # 10
print(course.replace('P', 'J'))  # Jython Jrogramming
print('Python' in course)  # True
print('Python' not in course)  # True
