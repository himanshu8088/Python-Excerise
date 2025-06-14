try:
    age = int(input("Enter your age: "))
except (ValueError, ZeroDivisionError) as exception:
    print("Invalid input! Please enter a valid integer for age.")
    print(f"Error details: {exception}")
    print(f"Error type: {type(exception)}")
else:
    print(f"You entered a valid age: {age}")    
print("Program continues after handling the exception.")

# Cleaning up resources with try-finally

try:
    file = open("example.txt", "w")
finally:
    file.close()    

# Or, using with statement for better resource management, it will automatically close the file

with open("example.txt", "w") as file, open("example2.txt", "w") as file2:
    file.write("Hello, World!")
    file2.write("Hello, World 2!")

# Raising exceptions intentionally
def check_positive_number(num):
    if num < 0:
        raise ValueError("The number must be positive.")
try:
    check_positive_number(-5)
except ValueError as e:
    print(f"Caught an exception: {e}")    