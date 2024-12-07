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
url = "http://www.example.com"

# Create a GET request object
request = urllib.request.Request(url)

# Send the GET request and store the response
response = urllib.request.urlopen(request)

# Print the response
print(response.read(), "\n")

# Use urllib.request.urlretrieve() function to download the data and save it to a file
urllib.request.urlretrieve(url, "example.html")


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


"""
   Hosting a webserver in Python
   
   1. Import the http.server module
   2. Create a class that inherits from http.server.BaseHTTPRequestHandler
   3. Define the do_GET method to handle GET requests
   4. Create a server object
   5. Start the server

"""

import http.server
import socketserver

# Define the server address and port
server_address = ("localhost", 8000)


# Create a request handler class
class RequestHandler(http.server.BaseHTTPRequestHandler):
    # Handle GET requests
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header(
           "Content-type",
           "text/plain"
           )
        
        self.end_headers()

        # Write content as utf-8 data
        self.wfile.write("Hello there!".encode())


# Create an http server object
server = http.server.HTTPServer(server_address, RequestHandler)

# Run the server
server.serve_forever()

# To stop the server, press Ctrl + C in the terminal window where the server is running
