#check whether a string is a palindrome or not
# def palindrome(s):
#     s=s.lower().replace(" ","")
#     return s==s[::-1]
# string=input("Enter a string: ")
# if palindrome(string):
#     print(string,"is a palindrome.")
# else:
#     print(string,"is not a palindrome.")

#solving using two pointer approach
def palindrome(s):
    s=s.lower().replace(" ","")
    left=0
    right=len(s)-1
    while left<=right:
        if s[left]==s[right]:
            left+=1
            right-=1
        else:
            return False
    return True
string=input("Enter a string: ")
if palindrome(string):
    print(string,"is a palindrome.")
else:
    print(string,"is not a palindrome.")
