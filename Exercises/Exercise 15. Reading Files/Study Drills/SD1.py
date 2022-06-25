# from system import argument variable
from sys import argv

# Script name, filename is an argument variables.
script, filename = argv

# text variable is opening file.
txt = open(filename)

print(f"Here's your file {filename}:")
# Read the text.
print(txt.read())

# Doing things again.
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())