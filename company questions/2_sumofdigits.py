#a program to calculate the sum of the digits of a positive integer.
def sum_of_digits(n):
    TOTAL = 0
    while n > 0:
        digit = n % 10
        TOTAL += digit
        n //= 10
    return TOTAL
n = int(input("Enter a positive integer: "))
result = sum_of_digits(n)
print("The sum of the digits of", n, "is:", result)