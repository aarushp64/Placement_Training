#given an array of n integers  where each vaalue reporesents the height of a vertical line on a chart. Find two lines which together with the x-axis forms a container, such that the container contains the most water. Return the maximum amount of water a container can store.
array=[8,8,6,2,5,8,4,3,7]
# array2=[4,3,2,1,4]
def max_water_container(heights):
    l=0
    r=len(heights)-1
    max_water=0
    while l<r:
        width=r-l
        height=min(heights[l],heights[r])
        max_water=max(max_water,width*height)
        if heights[l]<heights[r]:
            l=l+1
        else:
            r=r-1
    return max_water
result=max_water_container(array)
print("The maximum amount of water a container can store is:",result)


