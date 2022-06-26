# Each time we call print a line function. We give it a variable that has a value of the line number.
def print_a_line(line_count, f):
	print(line_count, f.readline())
# Output should be like that.
# 1 First line
#      ^ readline function. Everytime readline function works. The next time will be the next line.
# ^ line_count