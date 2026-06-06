# function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

#difference between print and return is that print is used to display the output of a function, while return is used to send a value back to the caller of the function.

def greet(name="World"):
    print("Hello, " + name + "!")       
input_name = input("Enter your name: ")
greet(input_name)

def odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd" 
input_num = int(input("Enter a number: "))
print(odd_even(input_num))
# num={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# for n in num:
#     print(n, " - ", odd_even(n))


#reverse a string without using a inbuild function
def reverse_string(s):
    x = ""
    for i in s:
        x = i + x
    return x
input_string = input("Enter a string: ")
print(reverse_string(input_string))


#swap two numbers without using a third variable

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Before swapping: ", num1, num2)
def swap(num1=5, num2=10):
    num1,num2 = num2,num1
    return num1,num2
print("After swapping: ", swap(num1, num2))



#second largest number in a list
def second_largest(lst=[1, 2, 3, 4, 5]):
    lst.sort()
    return lst[-2]
input_list = list(map(int, input("Enter a list of numbers separated by space: ").split()))
print("The second largest number in the list is: ", second_largest(input_list))
    


#fibonacci series
def fibonacci(n=10):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
n = int(input("Enter the number of terms in the Fibonacci series: "))
fibonacci(n)



#factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n = int(input("\nEnter a number: "))
print("The factorial of", n, "is", factorial(n))



#args keyword arguments = allows you to pass a variable number of non-keyword arguments to a function. The arguments are passed as a tuple.
#kwargs keyword arguments = allows you to pass a variable number of keyword arguments to a function. The arguments are passed as a dictionary.

#sum of n numbers using *args
def a(*num):
    return sum(num)
print(a(1, 2, 3, 4, 5))

def b(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
b(Name="Aarush", Age=20, City="Pune")



#lambda keyword = allows you to create anonymous functions. An anonymous function is a function that is defined without a name. Lambda functions are used for short, simple functions that are not going to be reused elsewhere in the code.

#finding odd or even using lambda function
odd_even_lambda = lambda y: "Even" if y % 2 == 0 and y != 0 else "Odd"
input_num = int(input("Enter a number: "))
print(odd_even_lambda(input_num))

#reverse a string using lamba function
reverse_string_lambda = lambda x: x[::-1]
input_string = input("Enter a string: ")    
print(reverse_string_lambda(input_string))

#prime number using function
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input("Enter a number: "))
if is_prime(n):
    print(n, "is a prime number.")    
else:
    print(n, "is not a prime number.")

#check if a number is a palindrome using function
def palindrome(n):
    return str(n) == str(n)[::-1]
n = int(input("Enter a number: "))
if palindrome(n):
    print(n, "is a palindrome number.")   
else:
    print(n, "is not a palindrome number.")

#using lamba convert uppercase to lowercase and vice versa
def case_convert(s):
    return s.upper() if s.islower() else s.lower()
input_string = input("Enter a string: ")
print(case_convert(input_string))


#local and global variables
# global variable = a variable that is defined outside of a function and can be accessed inside the function
# local variable = a variable that is defined inside a function and can only be accessed inside that function
x = 100 
def withdraw(amount):
    global x
    if amount > x:
        print("Insufficient balance")
    else:
        x -= amount
        print("Withdrawal successful. Remaining balance: ", x)
withdraw(30)
withdraw(80)

#vowel count in a string using function
input_string = input("Enter a string: ")
def vowel_count(s):
    count = 0
    for char in s:
        if char in "aeiou":
            count += 1
    return count
print("The number of vowels in the string is: ", vowel_count(input_string))