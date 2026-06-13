#create a program that generateds and strones prime numbers up to a given number n. The program should take n as input and output the list of prime numbers up to n.
def generate_primes(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for divisor in range(2, int(num**0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
n = int(input("Enter a number: "))
prime_numbers = generate_primes(n)
print("Prime numbers up to", n, "are:", prime_numbers)