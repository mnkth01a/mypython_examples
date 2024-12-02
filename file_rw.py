### Set variable fn to the file path ###
fn = "doc/file_rw.txt"

with open(fn, "w") as file:
    file.write("Hello, World!")  # Write a string to the file
    
with open(fn, "r") as file:
    print(file.read())  # Read the file and print its contents

with open(fn, "a") as file:
    file.write("\n")  # Write a newline character to the file
    file.write("It's me, Tom!")  # Append a string to the file

with open(fn, "r") as file:
    linefromfile = file.readline()  # Read the first line from the file
    #print(linefromfile)  # Print the first line with a newline character
    print(file.read())  # Read the rest of the file and print its contents
