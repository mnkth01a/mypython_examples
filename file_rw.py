"""

    File Open, Read, Write, Append, Remove

"""

import os

# If the directory doc2 does not exist, create it
if not os.path.exists("doc2"):
    os.makedirs("doc2")

### Set variable fn to the file path ###
fn = "doc2/file_rw.txt"

with open(fn, "w") as file:
    file.write("Hello, World!")  # Write a string to the file

with open(fn, "a") as file:
    name = input("Enter your name: ")  # Get user input
    file.write("\n")  # Write a newline character to the file
    file.write("It's me, " + name)  # Append a string to the file

with open(fn, "r") as file:
    # linefromfile = file.readline()  # Read the first line from the file
    # print(linefromfile)  # Print the first line with a newline character
    print(
        file.read(), "\n"
    )  # Read the rest of the file and print its contents with a newline character

# Remove the file
os.remove(fn)

# Remove the directory
import shutil

shutil.rmtree("doc2")

# End of file_rw.py
