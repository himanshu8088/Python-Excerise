def greet():
    print("Hi there!")
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

# file = open("content.txt", "w")
# file.write(message)

message = get_greeting("Himanshu")
print(greet("Sam", "Alton"))


def increment(number, by):
    return number + by


print(increment(2, 1))
print(increment(number=2, by=1))
print(increment(by=1, number=2))


def multliply(x, y):
    return x * y


print(multliply(2, 3))


def multliply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multliply(2, 3, 4, 5, 6))


# dictonary as argument
def save_user(**user):
    print(user)
    print(user['name'])
    print(user['id'])
    print(user['age'])


save_user(id=1, name="john", age=22)
