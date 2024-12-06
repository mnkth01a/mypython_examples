"""
   Object Oriented Programming in Python
   
      This file shows examples of object oriented programming in Python
      using classes and objects.  Dunders, decorators, and inheritance are
      also utilized in the examples.
      
      
"""

"""
   Basic Classes and Objects by creating a Person class using dunders and simple methods
"""


# Define a class named Person
class Person:
    """
    Person class that has a constructor that takes two parameters for the name and age.  The Person class has a method named say_hello that prints a greeting with the name of the person.  The Person class has a method named say_age that prints the age of the person.  The Person class has a method named say_hello_and_age that calls the say_hello and say_age methods.  The Person class has a method named __str__ that returns a string representation of the person.  The Person class has a method named __repr__ that returns a string representation of the person.  The Person class has a method named __eq__ that returns True if the name and age are the same.  The Person class has a method named __ne__ that returns True if the name or age are different.  The Person class has a method named __lt__ that returns True if the age is less than another person's age.  The Person class has a method named __le__ that returns True if the age is less than or equal to another person's age.  The Person class has a method named __gt__ that returns True if the age is greater than another person's age.  The Person class has a method named __ge__ that returns True if the age is greater than or equal to another person's age.  The Person class has a method named __add__ that returns the sum of the ages of two people.  The Person class has a method named __sub__ that returns the difference of the ages of two people.  The Person class has a method named __mul__ that returns the product of the ages of two people.  The Person class has a method named __truediv__ that returns the quotient of the ages of two people.  The Person class has a method named __floordiv__ that returns the floor division of the ages of two people.  The Person class has a method named __mod__ that returns the modulus of the ages of two people.  The Person class has a method named __pow__ that returns the power of the ages of two people.  The Person class has a method named __lshift__ that returns the left shift of the ages of two people.  The Person class has a method named __rshift__ that returns the right shift of the ages of two people.  The Person class has a method named __and__ that returns the bitwise and of the ages of two people.

    """

    # Define the constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Define a method named say_hello
    def say_hello(self):
        print(f"Hello, my name is {self.name}")

    # Define a method named say_age
    def say_age(self):
        print(f"I am {self.age} years old")

    # Define a method named say_hello_and_age
    def say_hello_and_age(self):
        self.say_hello()
        self.say_age()

    # Define a method named __str__
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

    # Define a method named __repr__
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

    # Define a method named __eq__
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    # Define a method named __ne__
    def __ne__(self, other):
        return self.name != other.name or self.age != other.age

    # Define a method named __lt__
    def __lt__(self, other):
        return self.age < other.age

    # Define a method named __le__
    def __le__(self, other):
        return self.age <= other.age

    # Define a method named __gt__
    def __gt__(self, other):
        return self.age > other.age

    # Define a method named __ge__
    def __ge__(self, other):
        return self.age >= other.age

    # Define a method named __add__
    def __add__(self, other):
        return self.age + other.age

    # Define a method named __sub__
    def __sub__(self, other):
        return self.age - other.age

    # Define a method named __mul__
    def __mul__(self, other):
        return self.age * other.age

    # Define a method named __truediv__
    def __truediv__(self, other):
        return self.age / other.age

    # Define a method named __floordiv__
    def __floordiv__(self, other):
        return self.age // other.age

    # Define a method named __mod__
    def __mod__(self, other):
        return self.age % other.age

    # Define a method named __pow__
    def __pow__(self, other):
        return self.age**other.age

    # Define a method named __lshift__
    def __lshift__(self, other):
        return self.age << other.age

    # Define a method named __rshift__
    def __rshift__(self, other):
        return self.age >> other.age

    # Define a method named __and__
    def __and__(self, other):
        return self.age & other.age


# Show examples of using the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
person3 = Person("Charlie", 35)

print("person1:", person1)
print("person2:", person2)
print("person3:", person3)

print("person1 == person2:", person1 == person2)
print("person1 != person2:", person1 != person2)
print("person1 < person2:", person1 < person2)
print("person1 <= person2:", person1 <= person2)
print("person1 > person2:", person1 > person2)
print("person1 >= person2:", person1 >= person2)

print("person1 + person2:", person1 + person2)
print("person1 - person2:", person1 - person2)
print("person1 * person2:", person1 * person2)
print("person1 / person2:", person1 / person2)
print("person1 // person2:", person1 // person2)
print("person1 % person2:", person1 % person2)
print("person1 ** person2:", person1**person2)
print("person1 << person2:", person1 << person2)
print("person1 >> person2:", person1 >> person2)
print("person1 & person2:", person1 & person2, "\n")

"""
   Inheritance of Classes
   
"""


# Define a class named Student that inherits from Person
class Student(Person):
    """
    Student class that inherits from Person Class

    Student class overrides the abstract methods area and perimeter and the Dunders __str__, __repr__, __eq__, __ne__, __lt__, __le__, __gt__, __ge__, __add__, __sub__, __mul__, __truediv__, __floordiv__, __mod__, and __pow__

    The Student class has a constructor that takes three parameters for the name, age, and major.  The Student class has a method named say_major that prints the major of the student.  The Student class has a method named say_hello_and_major that calls the say_hello and say_major methods.  The Student class has a method named __str__ that returns a string representation of the student.  The Student class has a method named __repr__ that returns a string representation of the student.  The Student class has a method named __eq__ that returns True if the name, age, and major are the same.  The Student class has a method named __ne__ that returns True if the name, age, or major are different.

    """

    # Define the constructor
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    # Define a method named say_major
    def say_major(self):
        print(f"My major is {self.major}")

    # Define a method named say_hello_and_major
    def say_hello_and_major(self):
        self.say_hello()
        self.say_major()

    # Define a method named __str__
    def __str__(self):
        return f"Student(name={self.name}, age={self.age}, major={self.major})"

    # Define a method named __repr__
    def __repr__(self):
        return f"Student(name={self.name}, age={self.age}, major={self.major})"

    # Define a method named __eq__
    def __eq__(self, other):
        return (
            self.name == other.name
            and self.age == other.age
            and self.major == other.major
        )

    # Define a method named __ne__
    def __ne__(self, other):
        return (
            self.name != other.name
            or self.age != other.age
            or self.major != other.major
        )


# Show examples of using the Student class
student1 = Student("Alice", 20, "Computer Science")
student2 = Student("Bob", 22, "Mathematics")
student3 = Student("Charlie", 24, "Physics")

print("student1:", student1)
print("student2:", student2)
print("student3:", student3, "\n")


"""

   Abstraction in Classes
   
"""
# Define an abstract base class named Shape
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Shape Abstract Base Class that has abstract methods for area and perimeter.

    The Shape class has methods for __str__, __repr__, __eq__, __ne__, __lt__, __le__, __gt__, __ge__, __add__, __sub__, __mul__, __truediv__, __floordiv__, __mod__, and __pow__

    """

    # Define an abstract method named area
    @abstractmethod
    def area(self):
        pass

    # Define an abstract method named perimeter
    @abstractmethod
    def perimeter(self):
        pass

    # Define a method named __str__
    def __str__(self):
        return f"Shape(area={self.area()}, perimeter={self.perimeter()})"

    # Define a method named __repr__
    def __repr__(self):
        return f"Shape(area={self.area()}, perimeter={self.perimeter()})"

    # Define a method named __eq__
    def __eq__(self, other):
        return self.area() == other.area() and self.perimeter() == other.perimeter()

    # Define a method named __ne__
    def __ne__(self, other):
        return self.area() != other.area() or self.perimeter() != other.perimeter()

    # Define a method named __lt__
    def __lt__(self, other):
        return self.area() < other.area()

    # Define a method named __le__
    def __le__(self, other):
        return self.area() <= other.area()

    # Define a method named __gt__
    def __gt__(self, other):
        return self.area() > other.area()

    # Define a method named __ge__
    def __ge__(self, other):
        return self.area() >= other.area()

    # Define a method named __add__
    def __add__(self, other):
        return self.area() + other.area()

    # Define a method named __sub__
    def __sub__(self, other):
        return self.area() - other.area()

    # Define a method named __mul__
    def __mul__(self, other):
        return self.area() * other.area()

    # Define a method named __truediv__
    def __truediv__(self, other):
        return self.area() / other.area()

    # Define a method named __floordiv__
    def __floordiv__(self, other):
        return self.area() // other.area()

    # Define a method named __mod__
    def __mod__(self, other):
        return self.area() % other.area()

    # Define a method named __pow__
    def __pow__(self, other):
        return self.area() ** other.area()


# Define a class named Circle that inherits from Shape
class Circle(Shape):
    """
    Circle class that inherits from Shape Abstract Base Class

    Circle class overrides the abstract methods area and perimeter and the Dunders __str__, __repr__, __eq__, __ne__, __lt__, __le__, __gt__, __ge__, __add__, __sub__, __mul__, __truediv__, __floordiv__, __mod__, and __pow__
    """

    # Define the constructor
    def __init__(self, radius):
        self.radius = radius

    # Define a method named area
    def area(self):
        return 3.14159 * self.radius**2

    # Define a method named perimeter
    def perimeter(self):
        return 2 * 3.14159 * self.radius

    # Define a method named __str__
    def __str__(self):
        return f"Circle(radius={self.radius}, area={self.area()}, perimeter={self.perimeter()})"

    # Define a method named __repr__
    def __repr__(self):
        return f"Circle(radius={self.radius}, area={self.area()}, perimeter={self.perimeter()})"

    # Define a method named __eq__
    def __eq__(self, other):
        return self.radius == other.radius

    # Define a method named __ne__
    def __ne__(self, other):
        return self.radius != other.radius

    # Define a method named __lt__
    def __lt__(self, other):
        return self.radius < other.radius

    # Define a method named __le__
    def __le__(self, other):
        return self.radius <= other.radius

    # Define a method named __gt__
    def __gt__(self, other):
        return self.radius > other.radius

    # Define a method named __ge__
    def __ge__(self, other):
        return self.radius >= other.radius

    # Define a method named __add__
    def __add__(self, other):
        return self.radius + other.radius

    # Define a method named __sub__
    def __sub__(self, other):
        return self.radius - other.radius

    # Define a method named __mul__
    def __mul__(self, other):
        return self.radius * other.radius

    # Define a method named __truediv__
    def __truediv__(self, other):
        return self.radius / other.radius

    # Define a method named __floordiv__
    def __floordiv__(self, other):
        return self.radius // other.radius

    # Define a method named __mod__
    def __mod__(self, other):
        return self.radius % other.radius

    # Define a method named __pow__
    def __pow__(self, other):
        return self.radius**other.radius


# Show examples of using the Circle class
circle1 = Circle(5)
circle2 = Circle(10)
circle3 = Circle(15)

print("circle1:", circle1)
print("circle2:", circle2)
print("circle3:", circle3)

print("circle1 == circle2:", circle1 == circle2)
print("circle1 != circle2:", circle1 != circle2)
print("circle1 < circle2:", circle1 < circle2)
print("circle1 <= circle2:", circle1 <= circle2)
print("circle1 > circle2:", circle1 > circle2)
print("circle1 >= circle2:", circle1 >= circle2)

print("circle1 + circle2:", circle1 + circle2)
print("circle1 - circle2:", circle1 - circle2)
print("circle1 * circle2:", circle1 * circle2)
print("circle1 / circle2:", circle1 / circle2)
print("circle1 // circle2:", circle1 // circle2)
print("circle1 % circle2:", circle1 % circle2)
print("circle1 ** circle2:", circle1**circle2, "\n")


# Define a class named Rectangle that inherits from Shape
class Rectangle(Shape):
    """
    Rectangle class that inherits from Shape Abstract Base Class

    Rectangle class overrides the abstract methods area and perimeter and the Dunders __str__, __repr__, __eq__, __ne__, __lt__, __le__, __gt__, __ge__, __add__, __sub__, __mul__, __truediv__, __floordiv__, __mod__, and __pow__
    """

    # Define the constructor
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Define a method named area
    def area(self):
        return self.width * self.height

    # Define a method named perimeter
    def perimeter(self):
        return 2 * (self.width + self.height)

    # Define a method named __str__
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height}, area={self.area()}, perimeter={self.perimeter()})"

    # Define a method named __repr__
    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height}, area={self.area()}, perimeter={self.perimeter()})"

    # Define a method named __eq__
    def __eq__(self, other):
        return self.width == other.width and self.height == other.height

    # Define a method named __ne__
    def __ne__(self, other):
        return self.width != other.width or self.height != other.height

    # Define a method named __lt__
    def __lt__(self, other):
        return self.area() < other.area()

    # Define a method named __le__
    def __le__(self, other):
        return self.area() <= other.area()

    # Define a method named __gt__
    def __gt__(self, other):
        return self.area() > other.area()

    # Define a method named __ge__
    def __ge__(self, other):
        return self.area() >= other.area()

    # Define a method named __add__
    def __add__(self, other):
        return self.area() + other.area()

    # Define a method named __sub__
    def __sub__(self, other):
        return self.area() - other.area()

    # Define a method named __mul__
    def __mul__(self, other):
        return self.area() * other.area()

    # Define a method named __truediv__
    def __truediv__(self, other):
        return self.area() / other.area()

    # Define a method named __floordiv__
    def __floordiv__(self, other):
        return self.area() // other.area()

    # Define a method named __mod__
    def __mod__(self, other):
        return self.area() % other.area()


# Show examples of using the Rectangle class
rectangle1 = Rectangle(5, 10)
rectangle2 = Rectangle(10, 20)
rectangle3 = Rectangle(15, 30)

print("rectangle1:", rectangle1)
print("rectangle2:", rectangle2)
print("rectangle3:", rectangle3)

print("rectangle1 == rectangle2:", rectangle1 == rectangle2)
print("rectangle1 != rectangle2:", rectangle1 != rectangle2)
print("rectangle1 < rectangle2:", rectangle1 < rectangle2)
print("rectangle1 <= rectangle2:", rectangle1 <= rectangle2)
print("rectangle1 > rectangle2:", rectangle1 > rectangle2)
print("rectangle1 >= rectangle2:", rectangle1 >= rectangle2)

print("rectangle1 + rectangle2:", rectangle1 + rectangle2)
print("rectangle1 - rectangle2:", rectangle1 - rectangle2)
print("rectangle1 * rectangle2:", rectangle1 * rectangle2)
print("rectangle1 / rectangle2:", rectangle1 / rectangle2)
print("rectangle1 // rectangle2:", rectangle1 // rectangle2)
print("rectangle1 % rectangle2:", rectangle1 % rectangle2)
print("rectangle1 ** rectangle2:", rectangle1**rectangle2, "\n")


# Define a class named Square that inherits from Rectangle
class Square(Rectangle):
    """
    Square class that inherits from Rectangle Class

    Square class overrides the abstract methods area and perimeter and the Dunders __str__, __repr__, __eq__, __ne__, __lt__, __le__, __gt__, __ge__, __add__, __sub__, __mul__, __truediv__, __floordiv__, __mod__, and __pow__

    The Square class has a constructor that takes a single parameter for the side length, and it calls the constructor of the Rectangle class with the side length as the width and height.  Because the side length is the same for the width and height of a square.  The area and perimeter methods are the same as the Rectangle class.

    """

    # Define the constructor
    def __init__(self, side):
        super().__init__(side, side)

    # Define a method named __str__
    def __str__(self):
        return f"Square(side={self.width}, area={self.area()}, perimeter={self.perimeter()})"

    # Define a method named __repr__
    def __repr__(self):
        return f"Square(side={self.width}, area={self.area()}, perimeter={self.perimeter()})"

    # Define a method named __eq__
    def __eq__(self, other):
        return self.width == other.width

    # Define a method named __ne__
    def __ne__(self, other):
        return self.width != other.width

    # Define a method named __lt__
    def __lt__(self, other):
        return self.area() < other.area()

    # Define a method named __le__
    def __le__(self, other):
        return self.area() <= other.area()

    # Define a method named __gt__
    def __gt__(self, other):
        return self.area() > other.area()

    # Define a method named __ge__
    def __ge__(self, other):
        return self.area() >= other.area()

    # Define a method named __add__
    def __add__(self, other):
        return self.area() + other.area()

    # Define a method named __sub__
    def __sub__(self, other):
        return self.area() - other.area()

    # Define a method named __mul__
    def __mul__(self, other):
        return self.area() * other.area()

    # Define a method named __truediv__
    def __truediv__(self, other):
        return self.area() / other.area()

    # Define a method named __floordiv__
    def __floordiv__(self, other):
        return self.area() // other.area()

    # Define a method named __mod__
    def __mod__(self, other):
        return self.area() % other.area()

    # Define a method named __pow__
    def __pow__(self, other):
        return self.area() ** other.area()


# Show examples of using the Square class
square1 = Square(5)
square2 = Square(10)
square3 = Square(15)

print("square1:", square1)
print("square2:", square2)
print("square3:", square3)

print("square1 == square2:", square1 == square2)
print("square1 != square2:", square1 != square2)
print("square1 < square2:", square1 < square2)
print("square1 <= square2:", square1 <= square2)
print("square1 > square2:", square1 > square2)
print("square1 >= square2:", square1 >= square2)

print("square1 + square2:", square1 + square2)
print("square1 - square2:", square1 - square2)
print("square1 * square2:", square1 * square2)
print("square1 / square2:", square1 / square2)
print("square1 // square2:", square1 // square2)
print("square1 % square2:", square1 % square2)
print("square1 ** square2:", square1**square2, "\n")


# Define a class named Triangle that inherits from Shape
class Triangle(Shape):
    """
    Triangle class that inherits from Shape Abstract Base Class

    Triangle class overrides the abstract methods area and perimeter and the Dunders __str__, __repr__, __eq__, __ne__, __lt__, __le__, __gt__, __ge__, __add__, __sub__, __mul__, __truediv__, __floordiv__, __mod__, and __pow__

    The Triangle class has a constructor that takes four parameters for the base, height, and two sides.  The area is calculated as 0.5 * base * height, and the perimeter is calculated as base + side1 + side2.  The area and perimeter methods are the same as the Rectangle class.

    """

    # Define the constructor
    def __init__(self, base, height, side1, side2):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2

    # Define a method named area
    def area(self):
        return 0.5 * self.base * self.height

    # Define a method named perimeter
    def perimeter(self):
        return self.base + self.side1 + self.side2

    # Define a method named __str__
    def __str__(self):
        return f"Triangle(base={self.base}, height={self.height}, side1={self.side1}, side2={self.side2}, area={self.area()}, perimeter={self.perimeter()})"

    # Define a method named __repr__
    def __repr__(self):
        return f"Triangle(base={self.base}, height={self.height}, side1={self.side1}, side2={self.side2}, area={self.area()}, perimeter={self.perimeter()})"

    # Define a method named __eq__
    def __eq__(self, other):
        return (
            self.base == other.base
            and self.height == other.height
            and self.side1 == other.side1
            and self.side2 == other.side2
        )

    # Define a method named __ne__
    def __ne__(self, other):
        return (
            self.base != other.base
            or self.height != other.height
            or self.side1 != other.side1
            or self.side2 != other.side2
        )

    # Define a method named __lt__
    def __lt__(self, other):
        return self.area() < other.area()

    # Define a method named __le__
    def __le__(self, other):
        return self.area() <= other.area()

    # Define a method named __gt__
    def __gt__(self, other):
        return self.area() > other.area()

    # Define a method named __ge__
    def __ge__(self, other):
        return self.area() >= other.area()

    # Define a method named __add__
    def __add__(self, other):
        return self.area() + other.area()

    # Define a method named __sub__
    def __sub__(self, other):
        return self.area() - other.area()

    # Define a method named __mul__
    def __mul__(self, other):
        return self.area() * other.area()

    # Define a method named __truediv__
    def __truediv__(self, other):
        return self.area() / other.area()

    # Define a method named __floordiv__
    def __floordiv__(self, other):
        return self.area() // other.area()

    # Define a method named __mod__
    def __mod__(self, other):
        return self.area() % other.area()

    # Define a method named __pow__
    def __pow__(self, other):
        return self.area() ** 2


# Show examples of using the Triangle class
triangle1 = Triangle(5, 10, 8, 8)
triangle2 = Triangle(10, 20, 16, 16)
triangle3 = Triangle(15, 30, 24, 24)

print("triangle1:", triangle1)
print("triangle2:", triangle2)
print("triangle3:", triangle3)

print("triangle1 == triangle2:", triangle1 == triangle2)
print("triangle1 != triangle2:", triangle1 != triangle2)
print("triangle1 < triangle2:", triangle1 < triangle2)
print("triangle1 <= triangle2:", triangle1 <= triangle2)
print("triangle1 > triangle2:", triangle1 > triangle2)
print("triangle1 >= triangle2:", triangle1 >= triangle2)

print("triangle1 + triangle2:", triangle1 + triangle2)
print("triangle1 - triangle2:", triangle1 - triangle2)
print("triangle1 * triangle2:", triangle1 * triangle2)
print("triangle1 / triangle2:", triangle1 / triangle2)
print("triangle1 // triangle2:", triangle1 // triangle2)
print("triangle1 % triangle2:", triangle1 % triangle2)
print("triangle1 ** triangle2:", triangle1**triangle2, "\n")


"""
   Static Methods in Classes
"""


# Define a class that has static methods
class Math:
    """
    Math class that has static methods for add, subtract, multiply, divide, power, modulus, floor_divide, left_shift, right_shift, and bitwise_and

    """

    # Define a static method named add
    @staticmethod
    def add(x, y):
        return x + y

    # Define a static method named subtract
    @staticmethod
    def subtract(x, y):
        return x - y

    # Define a static method named multiply
    @staticmethod
    def multiply(x, y):
        return x * y

    # Define a static method named divide
    @staticmethod
    def divide(x, y):
        return x / y

    # Define a static method named power
    @staticmethod
    def power(x, y):
        return x**y

    # Define a static method named modulus
    @staticmethod
    def modulus(x, y):
        return x % y

    # Define a static method named floor_divide
    @staticmethod
    def floor_divide(x, y):
        return x // y

    # Define a static method named left_shift
    @staticmethod
    def left_shift(x, y):
        return x << y

    # Define a static method named right_shift
    @staticmethod
    def right_shift(x, y):
        return x >> y

    # Define a static method named bitwise_and
    @staticmethod
    def bitwise_and(x, y):
        return x & y


# Show examples of using the static methods in the Math class
print("Math.add(10, 5):", Math.add(10, 5))
print("Math.subtract(10, 5):", Math.subtract(10, 5))
print("Math.multiply(10, 5):", Math.multiply(10, 5))
print("Math.divide(10, 5):", Math.divide(10, 5))
print("Math.power(10, 5):", Math.power(10, 5))
print("Math.modulus(10, 5):", Math.modulus(10, 5))
print("Math.floor_divide(10, 5):", Math.floor_divide(10, 5))
print("Math.left_shift(10, 5):", Math.left_shift(10, 5))
print("Math.right_shift(10, 5):", Math.right_shift(10, 5))
print("Math.bitwise_and(10, 5):", Math.bitwise_and(10, 5), "\n")


"""
   Class Methods in Classes
"""
