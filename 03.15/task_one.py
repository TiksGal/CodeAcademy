# Task Nr.1:

# Define a Shape class with the following attributes and methods:

# A name attribute, which is a string that represents the name of the shape.
# A sides attribute, which is an integer that represents the number of sides of the shape.
# An area method, which returns the area of the shape.
# Then, define a Rectangle class that inherits from the Shape class and has the following attributes and methods:

# A width attribute, which is a float that represents the width of the rectangle.
# A height attribute, which is a float that represents the height of the rectangle.
# An init method that initializes the name, sides, width, and height attributes.
# An area method that overrides the area method of the Shape class and returns the area of the rectangle.
# Finally, define a Square class that inherits from the Rectangle class and has the following attributes and methods:

# A side_length attribute, which is a float that represents the length of the sides of the square.
# An init method that initializes the side_length attribute and calls the init method 
# of the Rectangle class to initialize the name, sides, width, and height attributes.
class Shape:
    def __init__(self, name: str, sides: int) -> None:
        self.name = name
        self.sides = sides

    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, name: str, width: float, height: float) -> float:
        super().__init__(name, sides=4)
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, name: str, side_length: float) -> None:
        super().__init__(name, width=side_length, height=side_length)
        self.side_length = side_length
        

# Create a Rectangle
rectangle = Rectangle("My rectangle", width=5, height=10)

# Print the rectangle's name and number of sides
print(rectangle.name)  # Output: My rectangle
print(rectangle.sides)  # Output: 4

# Calculate and print the area of the rectangle
area = rectangle.area()
print(area)  # Output: 50.0

# Create a Square
square = Square("My square", side_length=7)

# Print the square's name and number of sides
print(square.name)  # Output: My square
print(square.sides)  # Output: 4

# Calculate and print the area of the square
area = square.area()
print(area)  # Output: 49.0
