#counting vowels in a string
def vowels(s):
    s=s.lower()
    count=0
    for char in s:
        if char in 'aeiou':
            count+=1
    return count
string=input("Enter a string: ")
result=vowels(string)
print("The number of vowels in the string is:",result)
