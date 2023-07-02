class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def get_fn(self):
        return f"Length: {self.length}, Breadth: {self.breadth}"

    def calc_area(self):
        return self.length * self.breadth

    def display_area(self):
        area = self.calc_area()
        print(f"The area of the rectangle is: {area}")


# Create an instance of the Rectangle class
rectangle = Rectangle(5, 3)

# Access the attributes and methods of the rectangle instance
print(rectangle.get_fn())      # Output: Length: 5, Breadth: 3
rectangle.display_area()       # Output: The area of the rectangle is: 15
