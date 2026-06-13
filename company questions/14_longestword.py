#finding longest word in a string
x="Coding is awesome and fun"
# y=array(x.split())
def longestword(s):
    words = s.split()
    longest = max(words, key=len)
    return longest
result=longestword(x)   
print("The longest word in the string is:",result)
