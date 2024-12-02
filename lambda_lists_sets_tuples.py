"""
Lambda functions are used to create anonymous functions. These are small functions which are not defined with any name. They are generally used when you require a nameless function for a short period of time. Lambda functions are defined using the keyword lambda followed by the function arguments.
"""

print("Lambda functions:", "\n")

# Define a lambda function that takes two arguments, x and y, and returns their sum.
my_lambda = lambda x, y: x + y

# Call the lambda function with arguments 2 and 3
result = my_lambda(2, 3)

# Print the result
print("Result of lambda function x, y: x + y is", result)

# Define a lambda function that takes a single argument, x, and returns the square of x.
square = lambda x: x**2

# Call the lambda function with argument 5
result = square(5)

# Print the result
print("Result of lambda function x: x**2 is", result)

# Define a lambda function that takes a single argument, x, and returns True if x is even and False otherwise.
is_even = lambda x: x % 2 == 0

# Call the lambda function with argument 4
result = is_even(4)

# Print the result
print("Result of lambda function x: x % 2 == 0 is", result, "\n")


"""
   Utilities for working with lists
"""
print("Utilities for working with lists:", "\n")

# Iterate over a list of numbers.
# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Print the list of numbers
print("List of numbers:", numbers)

print("Print each number in the list:")

# Iterate over the list of numbers
for number in numbers:

    # Print the result
    print("\t", "\t", number)

# Print a blank line
print("\n")

"""
   Remove duplicates from a list by converting it to a set and back to a list.
"""
print("Removing duplicates from a list:")

# Define a list with duplicates
my_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# Print the list with duplicates
print("List with duplicates:", my_list)

# Convert the list to a set to remove duplicates
my_set = set(my_list)

# Convert the set back to a list
# Can also be done in one line as follows:
# my_list = list(set(my_list))
my_list = list(my_set)

# Print the list without duplicates
print("List without duplicates:", my_list, "\n")


"""
   Take a list and make a set of the unique elements, and return the count of the unique elements occurance in the list.
   
   The function takes a list as input and returns a dictionary where the keys are the unique elements of the list and the values are the counts of each unique element.
"""
print("Counting the occurrence of unique elements in a list:")


def count_unique_elements(my_list):
    # Create an empty dictionary to store the counts of each unique element
    counts = {}

    # Iterate over the elements in the list
    for element in my_list:
        # Check if the element is already in the dictionary
        if element in counts:
            # If the element is in the dictionary, increment the count
            counts[element] += 1
        else:
            # If the element is not in the dictionary, add it with a count of 1
            counts[element] = 1

    # Return the dictionary of counts
    return counts


# Define a list of elements
my_list = ["a", "b", "c", "a", "b", "c", "a", "b", "c", "d", "e", "f", "g", "f", "b"]

# Print the list of elements
print("List of elements:", my_list)

# Call the count_unique_elements function with the list of elements
counts = count_unique_elements(my_list)

# Print the dictionary of counts
print("Counts of unique elements:", counts, "\n")


"""
   Take a list of tuples and return a list of the first elements of each tuple.
   
   The function takes a list of tuples as input and returns a list of the first elements of each tuple.
"""
print("Extracting the first element of each tuple in a list:")


def extract_first_elements(tuples_list):
    # Use a list comprehension to extract the first element of each tuple
    # The first element of a tuple t is accessed using t[0]
    first_elements = [t[0] for t in tuples_list]

    # Return the list of first elements
    return first_elements


# Define a list of tuples
tuples_list = [(1, "a"), (2, "b"), (3, "c")]

# Print the list of tuples
print("List of tuples:", tuples_list)

# Call the extract_first_elements function with the list of tuples
first_elements = extract_first_elements(tuples_list)

# Print the list of first elements
print("List of first elements:", first_elements, "\n")


"""
   Take a list of strings and return a list of the lengths of the strings.
   
   The function takes a list of strings as input and returns a list of the lengths of the strings.
"""
print("Calculating the lengths of strings in a list:")


def calculate_string_lengths(strings_list):
    # Use a list comprehension to calculate the length of each string
    # The length of a string s is accessed using len(s)
    string_lengths = [len(s) for s in strings_list]

    # Return the list of string lengths
    return string_lengths


# Define a list of strings
strings_list = [
    "apple",
    "banana",
    "cherry",
    "expialidocious",
    "supercalifragilisticexpialidocious",
]

# Print the list of strings
print("List of strings:", strings_list)

# Call the calculate_string_lengths function with the list of strings
string_lengths = calculate_string_lengths(strings_list)

# Print the list of string lengths
print("List of string lengths:", string_lengths, "\n")


"""
   Take a list of numbers and return a list of the numbers that are greater than a given threshold.
   
   The function takes a list of numbers and a threshold value as input and returns a list of the numbers that are greater than the threshold.
"""
print("Filtering numbers greater than a threshold:")


def filter_numbers(numbers_list, threshold):
    # Use a list comprehension to filter the numbers that are greater than the threshold
    filtered_numbers = [n for n in numbers_list if n > threshold]

    # Return the list of filtered numbers
    return filtered_numbers


# Define a list of numbers
numbers_list = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]

# Print the list of numbers
print("List of numbers:", numbers_list)

# Define a threshold value
threshold = 3

# Print the threshold value
print("Threshold value:", threshold)

# Call the filter_numbers function with the list of numbers and the threshold value
filtered_numbers = filter_numbers(numbers_list, threshold)

# Print the list of numbers greater than the threshold
print("Numbers greater than the threshold:", filtered_numbers, "\n")


"""
   Take a list of numbers and return the sum of the numbers.
   
   The function takes a list of numbers as input and returns the sum of the numbers.
   
   It produces the same result as the functools reduce() function.
"""
print("Calculating the sum of numbers in a list:")


def calculate_sum(numbers_list):
    # Use the sum() function to calculate the sum of the numbers in the list
    total_sum = sum(numbers_list)

    # Return the sum of the numbers
    return total_sum


# Define a list of numbers
numbers_list = [1, 2, 3, 4, 5]

# Print the list of numbers
print("List of numbers:", numbers_list)

# Call the calculate_sum function with the list of numbers
total_sum = calculate_sum(numbers_list)

# Print the sum of the numbers
print("Sum of numbers:", total_sum, "\n")


"""
   Take a list of numbers and return the product of the numbers.
   
   The function takes a list of numbers as input and returns the product of the numbers.
"""
print("Calculating the product of numbers in a list:")


def calculate_product(numbers_list):
    # Initialize the product to 1
    product = 1

    # Iterate over the numbers in the list
    for number in numbers_list:
        # Multiply the product by the number
        product *= number

    # Return the product of the numbers
    return product


# Define a list of numbers
numbers_list = [1, 2, 3, 4, 5]

# Print the list of numbers
print("List of numbers:", numbers_list)

# Call the calculate_product function with the list of numbers
product = calculate_product(numbers_list)

# Print the product of the numbers
print("Product of numbers:", product, "\n")


"""
   Set operations
"""
print("Set operations:", "\n")

# Define a set of numbers
numbers = {1, 2, 3, 4, 5}

# Print the set of numbers
print("Set of numbers:", numbers)

# Add an element to the set
numbers.add(6)

# Print the set of numbers after adding an element
print("Set of numbers after adding an element:", numbers)

# Remove an element from the set
numbers.remove(3)

# Print the set of numbers after removing an element
print("Set of numbers after removing an element:", numbers)

# Check if an element is in the set
is_present = 5 in numbers

# Print the result of checking if an element is in the set
print("Is 5 present in the set?", is_present)


# Define two sets of numbers
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Print the sets of numbers
print("Set 1:", set1)
print("Set 2:", set2)

# Calculate the union of the two sets
union = set1.union(set2)

# Print the union of the two sets
print("Union of Set 1 and Set 2:", union)

# Calculate the intersection of the two sets
intersection = set1.intersection(set2)

# Print the intersection of the two sets
print("Intersection of Set 1 and Set 2:", intersection)

# Calculate the difference between the two sets
difference = set1.difference(set2)

# Print the difference between the two sets
print("Difference between Set 1 and Set 2:", difference)

# Calculate the symmetric difference between the two sets
symmetric_difference = set1.symmetric_difference(set2)

# Print the symmetric difference between the two sets
print("Symmetric difference between Set 1 and Set 2:", symmetric_difference, "\n")


"""
   Tuple operations
"""
print("Tuple operations:", "\n")

# Define a tuple of strings
my_tuple = ("apple", "banana", "cherry")

# Print the tuple of strings
print("Tuple of strings:", my_tuple)

# Access the first element of the tuple
first_element = my_tuple[0]

# Print the first element of the tuple
print("First element of the tuple:", first_element)

# Access the last element of the tuple
last_element = my_tuple[-1]

# Print the last element of the tuple
print("Last element of the tuple:", last_element)

# Define a tuple of numbers
my_tuple = (1, 2, 3, 4, 5)

# Print the tuple of numbers
print("Tuple of numbers:", my_tuple)

# Calculate the sum of the numbers in the tuple
total_sum = sum(my_tuple)

# Print the sum of the numbers in the tuple
print("Sum of numbers in the tuple:", total_sum, "\n")


"""
   Dictionary operations
"""
print("Dictionary operations:", "\n")

# Define a dictionary of key-value pairs
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# Print the dictionary of key-value pairs
print("My Dictionary of key-value pairs:", my_dict)

# Access the value associated with the key "name"
name = my_dict["name"]

# Print the value associated with the key "name"
print("Value associated with the key 'name':", name)

# Update the value associated with the key "age"
my_dict["age"] = 35

# Update the value associated with the key "city"
my_dict["city"] = "Simpsonville"

# Print the updated dictionary of key-value pairs
print("Updated dictionary of key-value pairs:", my_dict)

# Add a new key-value pair for the state
my_dict["state"] = "SC"

# Add a new key-value pair to the dictionary
my_dict["country"] = "USA"

# Print the dictionary with the new key-value pair
print("Dictionary with the new key-value pair:", my_dict)
