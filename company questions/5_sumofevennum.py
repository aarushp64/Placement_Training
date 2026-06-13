#takes a num n and prints the sum of all even numbers from 1 to n.
def sum_of_even_numbers(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total += i
    return total


n = int(input("Enter a number: "))
result = sum_of_even_numbers(n)
print("The sum of all even numbers from 1 to", n, "is:", result)