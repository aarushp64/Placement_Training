# generator is a special type of function that allow you to return a value and then continue executing the function from where it left off when the next value is requested. This is done using the yield keyword instead of return.
# yeild is used to produce a value and pause the function's execution, allowing it to be resumed later. This makes generators memory efficient and suitable for handling large datasets or infinite sequences.

def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
x= even_numbers(10)
print(next(x))  
print(next(x))   
print(next(x))  
print(next(x))

#squares of numbers using generator
def squares(n):
    for i in range(n):
        yield i ** 2

n = int(input("Enter the number of squares to generate (minus 2): "))
x = squares(n)
for i in range(n-2):
    print(next(x))

#odd even numbers using generator
def odd_even(n):
    for i in range(n):
        if i % 2 == 0:
            yield f"{i} is even"
        else:
            yield f"{i} is odd"
n = int(input("Enter the number of odd/even numbers to generate: "))
x = odd_even(n)
for i in range(n):
    print(next(x))

#differece between yield and return
# The main difference between yield and return is that return is used to exit a function and return
# yeild is used to produce a value and pause the function's execution, allowing it to be resumed later. When a function uses return, it terminates and cannot be resumed.

# How does generator enchance performance?
# Generators enhance performance by allowing you to generate values on-demand without storing the entire sequence in memory. 
# This is particularly beneficial when working with large datasets or infinite sequences, as it reduces memory usage and allows for more efficient processing.


#prime numbers using generator
# def prime_numbers(n):
#     for num in range(2, n):
#         is_prime = True
#         if num <= 1:
#             is_prime = False
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#     return is_prime
#     if is_prime:
#         yield num
# m = int(input("Enter the number of prime numbers to generate: "))
# p = prime_numbers(m)
# print(next(p))

