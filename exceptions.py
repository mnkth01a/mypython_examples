"""
This file contains the custom exceptions that are raised in the application.

"""


# Show the custom exception that is raised when the user tries to access a non-existent page.
class PageNotFound(Exception):
    """
    This class is used to raise a PageNotFound exception when the user tries to access a page that is not allowed.

    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


# Show the custom exception that is raised when the user tries to access a page that is not allowed.
class ForbiddenPage(Exception):
    """
    This class is used to raise a ForbiddenPage exception when the user tries to access a page that is not allowed.

    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


# Show the custom exception that is raised when the user tries to access a page that is not allowed.
class InvalidInput(Exception):
    """
    This class is used to raise an InvalidInput exception when the user tries to access a page that is not allowed.
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


# Show a try-except block to catch the custom exceptions.
try:
    raise PageNotFound("Page not found")
except PageNotFound as e:
    print(e)

try:
    raise ForbiddenPage("Forbidden page")
except ForbiddenPage as e:
    print(e)

try:
    raise InvalidInput("Invalid input")
except InvalidInput as e:
    print(e)

# End of exceptions.py
