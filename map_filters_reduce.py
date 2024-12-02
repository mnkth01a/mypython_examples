"""
   The map(), filter(), and reduce() functions are built-in functions in Python that are used to process iterables.
   
      The map() function takes a function and an iterable as arguments and applies the function to each element in the iterable.
      
      The filter() function takes a function and an iterable as arguments and returns a new iterable containing only the elements for which the function returns True.
      
      The reduce() function takes a function and an iterable as arguments and applies the function cumulatively to the elements of the iterable, returning a single value.
"""

"""
   The map() function takes a function and an iterable as arguments and applies the function to each element in the iterable.
   
"""
# print("\n")
print("The map() function:")

# Define a list of numbers and use the map function to square each number in the list.
numbers = [1, 2, 3, 4, 5]

# Print the list of numbers
print("List of numbers:", numbers)

# Use the map() function to apply a lambda function to each element in the list
# The lambda function takes an element, x, and returns its square.
list_of_squared_numbers = list(map(lambda x: x**2, numbers))

# Print the squared numbers
print("List of squared numbers:", list_of_squared_numbers, "\n")


"""
   The filter() function takes a function and an iterable as arguments and returns a new iterable containing only the elements for which the function returns True.
"""
print("The filter() function:")

# Define a list of numbers and use the filter function to return only the even numbers in the list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 24, 25, 26, 27, 28, 29, 30]

# Print the list of numbers
print("List of numbers:", numbers)

# Use the filter() function to apply a lambda function to each element in the list
# The lambda function returns True if the element is even and False otherwise.
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Print the even numbers
print("List of even numbers:", even_numbers, "\n")


"""
   The reduce() function takes a function and an iterable as arguments and applies the function cumulatively to the elements of the iterable, returning a single value.
"""
print("The reduce() function:")

# Import the reduce function from the functools module
from functools import reduce

# Define a list of numbers and use the reduce function to calculate the sum of the numbers in the list.
numbers = [1, 2, 3, 4, 5]

# Print the list of numbers
print("List of numbers:", numbers)

# Use the reduce() function to apply a lambda function to each element in the list
# The lambda function takes two elements, x and y, and returns their sum.
sum_of_numbers = reduce(lambda x, y: x + y, numbers)

# Print the sum of the numbers
print("Sum of numbers:", sum_of_numbers, "\n")


