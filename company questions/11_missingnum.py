#find the missing number in the array
array={9,6,4,2,3,5,7,0,1}
sorted_array=sorted(array)
missingnum=0
def missing(arr):
    for i in range(len(arr)):
        if arr[i]!=i:
            missingnum=i
            break
    return missingnum
result=missing(sorted_array)
print("The missing number in the array is:",result)

