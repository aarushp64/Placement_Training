#a string is every opening braket has a corresponding closing bracket of the same type
#{},[],() is valid but {] is not valid
def valid():
    a=input("Enter a string of brackets: ")
    stack=[]
    for i in a:
        if i in['(','{','[']:
            stack.append(i)
        else:
            if not stack:
                return False
            top=stack.pop()
            if i==')' and top!='(':
                return False
            elif i=='}' and top!='{':
                return False
            elif i==']' and top!='[':
                return False
    return not stack
if valid():
    print("The string is valid")
else:
    print("The string is not valid")
