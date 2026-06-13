#return an integer where each digit is incremented by 1. For example, if the input is 123, the output should be 234.
def increment_digits(n):
    result = 0
    position = 1
    while n != 0:
        digit = n % 10
        incremented_digit = (digit + 1) % 10
        result = result * 10 + incremented_digit
        position *= 10
        n //= 10
    return result
n = int(input("Enter an integer: "))
result = increment_digits(n)    
print("The incremented integer is:", result)