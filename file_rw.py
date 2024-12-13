"""

    File Open, Read, Write, Append, Remove

"""

import os
import shutil

# If the directory doc2 does not exist, create it and the child directory text_files/doc2
if not os.path.exists("text_files"):
    os.makedirs("text_files/doc2")

# Change to the child directory text_files
os.chdir("text_files/doc2")

### Set variable fn to the file path ###
fn = "file_rw.txt"

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
# os.remove(fn)

# Change to the parent directory
os.chdir("..")

# shutil.rmtree("doc2")

# End of file_rw.py
