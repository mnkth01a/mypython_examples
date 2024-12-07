"""
   Networking and JSON
   
   
   How to make a HTTP GET request in Python
   
   1. Import the urllib.request module
   2. Set the URL you want to send the request to
   3. Create a request object
   4. Send the request and store the response
   5. Print or Store the response
   
"""

import urllib.request


# Set the URL you want to send the GET request to
url = "http://www.google.com"

# Create a GET request object
request = urllib.request.Request(url)

# Send the GET request and store the response
response = urllib.request.urlopen(request)

# Print the response
print(response.read(), "\n")

# Use urllib.request.urlretrieve() function to download the data and save it to a file
urllib.request.urlretrieve(url, "google.html")


'''
"""
   How to make a HTTP POST request in Python
   
   1. Import the urllib.request module
   2. Set the URL you want to send the request to
   3. Create a dictionary object containing key-value pairs
   4. Encode the data as a URL query string
   5. Create a POST request object
   6. Send the POST request and store the response
   7. Print or Store the response
   
"""
# Make a POST request in Python using the urllib.request module
import urllib.parse

# Set the URL you want to send the request to
url = "http://www.example.com"

# Create a dictionary object containing key-value pairs
data = {"key1": "value1", "key2": "value2"}

# Encode the data as a URL query string
data = urllib.parse.urlencode(data)

# Create a POST request object
request = urllib.request.Request(url, data=data.encode())

# Send the POST request and store the response
response = urllib.request.urlopen(request)   # POST request doesn't work with example.com

# Print the response
print(response.read(), "\n")

# Use urllib.request.urlretrieve() function to download the data and save it to a file
urllib.request.urlretrieve(url, "example2.html")
'''

# JSON
import json

# Create a dictionary object
person_dict = {"first": "Christopher", "last": "Harrison"}

# Add additional key pairs to dictionary as needed
person_dict["City"] = "Seattle"

# Convert dictionary to JSON object
person_json = json.dumps(person_dict)

# Print JSON object
print(person_json, "\n")
