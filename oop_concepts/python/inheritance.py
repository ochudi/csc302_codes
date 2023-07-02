# Python code to demonstrate how parent constructors are called.

# Parent class
class Person(object):
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))

# child class


class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Salary: {}".format(self.salary))
        print("Post: {}".format(self.post))


# Driver code
person1 = Person("John Doe", 123)
person2 = Person("Jane Doe", 124)
employee1 = Employee("Chris Evans", 125, 10_000, "Manager")
employee2 = Employee("Jennifer Lawrence", 126, 15_000, "Software Engineer")

person1.display()
person2.details()
employee1.display()
employee2.details()
