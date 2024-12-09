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
        self.send_header("Content-type", "text/plain")

        self.end_headers()

        # Encode and write the response to the client
        self.wfile.write(
            "\n\t\n\tHello there!\n\t\n\tWelcome to the server!\n\t\n\tThis is a test.".encode()
        )


# Create an http server object
server = http.server.HTTPServer(server_address, RequestHandler)

# Run the server
server.serve_forever()

# To stop the server, press Ctrl + C in the terminal window where the server is running


"""
   DJango Section

      To create a web app with DJango, you will need to follow these steps:
      
      1. Install Django using pip
      
      2. Create a new Django project using the django-admin command  (django-admin startproject myproject)
      
      3. Create a new Django app using the manage.py command (python manage.py startapp myapp)
      
      4. Define the models for your app in the models.py file (myapp/models.py)
      
      5. Create and run migrations to create the database schema (python manage.py makemigrations, python manage.py migrate)
      
      6. Register the models in the admin.py file (myapp/admin.py)
      
      7. Create views for your app in the views.py file (myapp/views.py)
      
      8. Define the URL patterns in the urls.py file (myapp/urls.py)
      
      9. Include the app URL patterns in the project URL patterns (myproject/urls.py)
      
      10. Run the development server using the manage.py command (python manage.py runserver)
"""

# To install Django using pip, run the following command in the terminal
# pip install django

# To create a new Django project, run the following command in the terminal
# django-admin startproject myproject

# To create a new Django app, run the following command in the terminal
# python manage.py startapp myapp

# To create and run migrations, run the following commands in the terminal
# python manage.py makemigrations
# python manage.py migrate

# To run the development server, run the following command in the terminal
# python manage.py runserver

# To stop the development server, press Ctrl + C in the terminal window where the server is running

# To create a superuser for the Django admin interface, run the following command in the terminal
# python manage.py createsuperuser

# To access the Django admin interface, go to http://localhost:8000/admin in your web browser and log in with the superuser credentials
