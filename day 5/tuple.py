# tuple is immutable
# tuple can store different data types
# tuple is ordered
# tuple allows duplicates
# tuple alows indexing and slicing

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
#my_tuple.append(6) # this will raise an error because tuples are immutable
#my_tuple.remove(2) # this will also raise an error because tuples are immutable
print(my_tuple[0]) # indexing
print(my_tuple[1:4]) # slicing


print(type(my_tuple)) # this will print <class 'tuple'>
#what is typecasting? Typecasting is the process of converting a variable from one data type to another.
#typecasting a list to a tuple
my_list = [6,7,8,9,10]
print(tuple(my_list)) # this will convert the list my_list to a tuple

#nested tuples
nested_tuple = (1, 2, (3, 4), 5)    
print(nested_tuple)

#difference between list and tuple is that list is mutable and tuple is immutable. This means that you can change the elements of a list, but you cannot change the elements of a tuple.
# a= (1, 2, 3)
# a[0] = 4 # this will raise an error because tuples are immutable
# b = [1, 2, 3]
# b[0] = 4 # this will work because lists are mutable

