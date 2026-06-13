#finding thbe longest common prefix in a list of strings
x=["flower","flow","flight"]
# def longest(x):
#     for i in range(len(x[0])):
#         char = x[0][i]
#         for string in x:
#             if i >= len(string) or string[i] != char:
#                 return x[0][:i]
#     return x[0]
# result=longest(x)
# print("The longest common prefix is:",result)

sorted_x = sorted(x)
first = sorted_x[0]
last = sorted_x[-1]
i = 0
while i < len(first) and i < len(last) and first[i] == last[i]:
    i += 1
result = first[:i]
print("The longest common prefix is:", result)