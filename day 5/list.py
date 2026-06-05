# list is mutable
# list can store different data types
# list is ordered
# list allows duplicates
# list is indexed and can be nested
my_list = [1, 2, 3, 4, 5]

print (my_list)
my_list.append(6)
my_list.remove(2)
print (my_list) 

#difference between append and insert is that append adds an element to the end of the list, while insert allows you to specify the index where the element should be added.
my_list.insert(0, 0) # inserts 0 at index 0
print (my_list)

my_list.extend([7, 8, 9]) #extend adds multiple elements to the end of the list
print (my_list)
#difference between extend and append is that append adds a single element to the end of the list, while extend allows you to add multiple elements from another iterable (like another list) to the end of the list.

my_list.pop() #pop removes the last element from the list
print (my_list)

my_list.count(3) #count returns the number of occurrences of a specified value in the list
print (my_list.count(3))

grades = [85, 90, 78, 92, 88]
print(grades)
average_grade = sum(grades) / len(grades) # calculates the average grade
print(average_grade)