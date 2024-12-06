"""
   This file shows examples of dictionaries in Python.
"""

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


# create an empty dictionary
ages = {}

# Add key-value pairs to the dictionary
# add an entry with key "Alice" and value 22
ages["Alice"] = 22

# add an entry with key "Bob" and value 25
ages["Bob"] = 25

# add an entry with key "Charlie" and value 31
ages["Charlie"] = 31

# Print the dictionary of key-value pairs
print("Dictionary of key-value pairs:", ages)

# Set age = ages["Bob"]
age = ages["Bob"]

# Print the value associated with the key "Bob"
print("Value associated with the key 'Bob':", age)


# Check if a key is in the dictionary
if "Alice" in ages:
    print("Alice is in the dictionary")
else:
    print("Alice is not in the dictionary")
