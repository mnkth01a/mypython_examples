'''
   Networking and JSON
   
'''
import urllib.request


# Set the URL you want to send the request to
url = 'http://www.google.com'

# Create a request object
request = urllib.request.Request(url)

# Send the request and store the response
response = urllib.request.urlopen(request)

# Print the response
print(response.read())


