#given an array of integers, remove the duplicates in-place such that each element appears only once and return the new length
x=[0,1,1,2,3,4,4,5]
def remove_duplicates(nums):
    if not nums:
        return 0
    unique=0
    for i in range(1,len(nums)):
        if nums[i]!=nums[unique]:
            unique+=1
            nums[unique]=nums[i]
    return unique+1

length = remove_duplicates(x)
print("The new length is:", length)
print("The array without duplicates is:", x[:length])