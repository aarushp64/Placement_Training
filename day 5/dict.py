# dictionary is a collection of key-value pairs
# dictionary is mutable
# dictionary is ordered
# dictionary does not allow duplicates
# dictionary can store different data types
my_dict = {"Name": "Aarush", "Age": 20, "City": "Pune"}
print(my_dict)
print(type(my_dict))

my_dict["Age"] = 21 # this will update the value of the key 
print(my_dict)
my_dict["Country"] = "India" # this will add a new key-value pair
print(my_dict)
my_dict.pop("City") # this will remove the key and its corresponding value
print(my_dict)
del my_dict["Country"] # this will also remove the key and its corresponding value
print(my_dict)

#nested dictionaries
nested_dict = {"Name": "Aarush", "Age": 20, "City": "Pune", "Education": {"Degree": "B.Tech", "University": "MIT ADTU"}}
print(nested_dict)
nested_dict["Education"]["University"] = "MIT Art Design & Technology" # this will update the value of the key "Degree" in the nested dictionary 
print(nested_dict)

x={"a": 1, "b": 2, "c": 3, "d": 4, "e": 5} 
print(x)
squared_x = {key: value**2 for key, value in x.items()}
print(squared_x)  #dictionary comprehension is a concise way to create dictionaries. It consists of an expression pair (key: value) followed by a for statement inside curly braces {}. The expression pair is evaluated for each item in the iterable, and the resulting key-value pairs are added to the new dictionary.

x = {key: value for key, value in x.items() if value<4 and value>2}
print(x)
