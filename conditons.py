# temp = int(input("What is the temperature? "))
temp = 10
if temp > 30:
    print("It's a hot day")
elif temp >= 20 and temp <= 30:
    print("It's a nice day")
else:
    print("It's a cold day")

# Chaining Comparison Operators
temp = 25
if temp > 30:
    print("It's a hot day")
elif 20 <= temp <= 30:
    print("It's a nice day")
else:
    print("It's a cold day")

age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"
print(message)  # Eligible

# Using Ternary Operator

message = "Eligible" if age>=18 else "Not Eligible"
print(message)  # Eligible