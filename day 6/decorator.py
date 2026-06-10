# decorator is a function that takes another function as an argument and extends the behavior of the latter function without explicitly modifying it.
# In Python, decorators are often used to add functionality to functions or methods in a clean and readable way. They are denoted by the "@" symbol followed by the decorator function name above the function definition that they are decorating.

def demo(say_hello):
    def wrapper(name):
        print("Before the function call")
        say_hello(name)
        print("After the function call")
    return wrapper
@demo
def say_hello(name):
    print(f"Hello, {name}!")
input_name = input("Enter your name: ")
say_hello(input_name)

# addition of two numbers using decorator
def add(func):
    def wrapper(a,b):
        print("Before the addition")
        result = func(a,b)
        print("After the addition")
        return result
    return wrapper

@add
def sum_numbers(a, b):
    return a + b

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"The sum is: ",sum_numbers(num1, num2))

#convert lowercase to uppercase using decorator
def uppercase(func):
    def wrapper(text):
        print("Converting to uppercase...")
        y = func(text)
        print("Conversion complete.")
        return y.upper()
    return wrapper
@uppercase
def caps(text):
    return text
x = input("Enter a string: ")
print(f"Uppercase: {caps(x)}")

#largest of three numbers using decorator
def large(func):
    def wrapper(a,b,c):
        print("Finding the largest number...")
        result = func(a,b,c)
        print("Finding complete.")
        return result
    return wrapper
@large
def largest(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:        
        return c
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
print(f"The largest number is: {largest(num1, num2, num3)}")
