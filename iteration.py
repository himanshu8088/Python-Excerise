print("Sending a message")

# range function
for number in range(3):
    print("Attempt", number+1, (number+1) * ".")

for number in range(1, 4):
    print("Attempt", number, number * ".")

# for else statement
successful = False
for number in range(3):
    print("Atempt", number+1)
    if successful:
        print("Successful")
        break
    print("Attempting...")
else:
    print("Unsuccessful after 3 attempts")

# Iterable
print(type(range(5)))

for x in range(5):
    print(x, end=" ")
print()

for x in 'Hello':
    print(x, end=" ")
print()

for x in [1, 2, 3, 4, 5]:
    print(x, end=" ")
print()


while number > 0:
    print(number)
    number -= 1
