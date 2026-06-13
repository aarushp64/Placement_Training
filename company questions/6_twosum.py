# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

def two_sum():
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] + list[j] == target:
                return [i, j]
    return None
list = [2, 7, 11, 15]
target = 9
result = two_sum()
if result:
    print("Indices of the two numbers that add up to", target, "are:", result)
else:    print("No two numbers add up to", target)