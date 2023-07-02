# Python program to demonstrate private members

# Creating a Base class
class Base:
    def __init__(self):
        self.first_name = "John"
        self.__last_name = "Doe"


# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of Base class
        Base.__init__(self)

        print("Calling private member of base class: ")
        print(self.__last_name)


# Driver code
obj1 = Base()
print(obj1.first_name)


#! Uncommenting will flag errors
# print(obj1.c)
# obj2 = Derived()
