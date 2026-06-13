#check wheater the num is arstrong num
x=int(input("Enter a number: "))

def armstrong_num(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** len(str(n))
        temp //= 10
    return sum
if armstrong_num(x) == x:
    print(x, "is an Armstrong number")
else:
    print(x, "is not an Armstrong number")