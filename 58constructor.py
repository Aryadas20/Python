class Person:

    def __init__(self, n, o):  #constructor
        # print("Hey I am a person")
        self.name = n
        self.occ= o

    def info(self):
         print(f"{self.name} is a {self.occ}")

a = Person("Arya", "Google ceo") # every time call when never i create a object from class 
b = Person("Avneet", "Assistant")
a.info()
b.info()
# print(a.name)



# Parameterized Constructor in Python
# When the constructor accepts arguments along with self, it is known as parameterized constructor.

# These arguments can be used inside the class to assign the values to the data members.

# Example:
# class Details:
#     def __init__(self, animal, group):
#         self.animal = animal
#         self.group = group

# obj1 = Details("Crab", "Crustaceans")
# print(obj1.animal, "belongs to the", obj1.group, "group.")
# Output:
# Crab belongs to the Crustaceans group.



# Default Constructor in Python
# When the constructor doesn't accept any arguments from the object and has only one argument, self, in the constructor, it is known as a Default constructor.

# Example:
# class Details:
#   def __init__(self):
#     print("animal Crab belongs to Crustaceans group")
# obj1=Details()

# Copied!
# Output:
# animal Crab belongs to Crustaceans group