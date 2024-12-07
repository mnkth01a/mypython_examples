'''
   Networking and JSON
   
'''
import urllib.request


# Set the URL you want to send the request to
url = 'http://www.example.com'

# Create a request object
request = urllib.request.Request(url)

# Send the request and store the response
response = urllib.request.urlopen(request)

# Print the response
print(response.read(), '\n')


# JSON
import json

# Create a dictionary object
person_dict = {'first': 'Christopher', 'last':'Harrison'}

# Add additional key pairs to dictionary as needed
person_dict['City'] = 'Seattle'

# Convert dictionary to JSON object
person_json = json.dumps(person_dict)

# Print JSON object
print(person_json, '\n')

