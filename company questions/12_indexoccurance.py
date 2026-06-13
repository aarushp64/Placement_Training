#find the index of the first occurrence in a string
x="applesandoranges"
y="and"
# print(x.find(y))
def indexoccurance(x,y):
    for i in range(len(x)-len(y)+1):
        if x[i:i+len(y)]==y:
            return i
result=indexoccurance(x,y)
if result != -1:
    print("The index of the first occurrence of", y, "in", x, "is:", result)