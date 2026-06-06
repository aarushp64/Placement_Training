# Set is a collection of non-repetitive elements
# set is mutable
# set is unordered
# set does not allow duplicates
# set can store different data types
# set does not allow indexing or slicing
# my_set = set{} this ceates an empty set, but my_set = {} creates an empty dictionary
my_set = {1, 2, 3, 4, "ABC", 5.6, True, False}
print(my_set)
print(type(my_set)) 
my_set.add(5)
print(my_set)
my_set.remove(5.6)
print(my_set)

my_set.pop()
print(my_set) # this will remove a random element from the set
my_set.discard(6)
print(my_set) # this will remove 6 from the set if it is present, but will not raise an error if it is not present

# set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2)) # this will print {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.intersection(set2)) # this will print {4, 5}
print(set1.difference(set2)) # this will print {1, 2, 3}