# from system import argument variables
from sys import argv

# Script name and input files are argument variables
script, input_file = argv

# a function named print_all takes one argument
def print_all(f):
	# use the function read to read the argument
	print(f.read())

# a function named rewind takes one argument
def rewind(f):
	# seek sets the position of a file pointer
	f.seek(0)

# a function named print_a_line takes 2 arguments. Line_count and f (file).
def print_a_line(line_count, f):
	# print line count number and file readline. Which means the first line and after that it'll be the second line.
	print(line_count, f.readline())

# a variable named current_file is opening input_file.
current_file = open(input_file)

print("First let's print the whole file:\n")

# call print_all function with current_file variable.
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# call rewind function with current_file variable.
rewind(current_file)

print("Let's print three lines:")

# current_lines variable has a value of one.
current_lines = 1
# call print_a_line function with two variables. Current_line and current_file.
print_a_line(current_line, current_file)

# Add one to current_lne variable.
current_line += 1
# the same thing as here.
print_a_line(current_line, current_file)

# And all of that.
current_line += 1
print_a_line(current_line, current_file)