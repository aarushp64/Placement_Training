# OOPS Object Oriented Programming System
# This concept focuses on using reusable code and creating objects that can interact with each other.
# It allows you to create classes, which are blueprints for creating objects.
# A class is a blueprint for creating object. It defines a set of attributes and methods that the object will have.
# An object is an instance of a class. It is created using the class and can have its own unique attributes and methods.


# Abstraction is the process of hiding the implementation details and showing only the functionality to the user. It allows you to focus on what an object does instead of how it does it.

# Encapsulation is the process of wrapping data and methods that operate on that data within a single unit, such as a class. It allows you to restrict access to certain components of an object and protect the integrity of the data.

# Inheritance is the process of creating a new class that is a modified version of an existing class. The new class is called a subclass or child class, and the existing class is called a superclass or parent class. The subclass inherits the attributes and methods of the superclass and can also have its own unique attributes and methods.

# Polymorphism is the ability of an object to take on many forms. It allows you to use a single interface to represent different types of objects. This is achieved through method overriding, where a subclass provides a specific implementation of a method that is already defined in its superclass.

# Method Overloading is the ability to define multiple methods with the same name but different parameters. It allows you to perform different tasks based on the number or type of arguments passed to the method. Pythion doesnt support method overloading but we can achieve it using default arguments or variable-length arguments.

# class Animal:
#     def speak(self):
#         return "Animal speaks"
# class Dog(Animal):
#     def speak(self):
#         return "Dog barks"  
# class Cat(Animal):
#     def speak(self):
#         return "Cat meows"
    
# dog = Dog()
# cat = Cat() 
# print(dog.speak())
# print(cat.speak())

#inheritance example
class father:
    def __init__(self, name):
        self.name = name
    def display(self):
        print("Father's name is", self.name)
class son(father):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    def display(self):
        super().display()
        print("Son's name is", self.name, "and age is", self.age)

s = son("Aarush", 20)
s.display()

