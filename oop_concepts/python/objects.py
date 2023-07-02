class Dog:
    # Class attribute
    attr1 = "mammal"
    
    # Instance attribute
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print("WOOF! My name is {}".format(self.name))
        

# Driver code
# Object instantiation
dog1 = Dog("Rodger")
dog2 = Dog("Tommy")

# Accessing class attributes
print("Rodger is a {}".format(dog1.__class__.attr1))
print("Tommy is also a {}".format(dog2.__class__.attr1))

# Accessing instance attributes
print("Name: {}".format(dog1.name))
print("Name: {}".format(dog2.name))

# Accessing class methods
dog1.speak()
dog2.speak()