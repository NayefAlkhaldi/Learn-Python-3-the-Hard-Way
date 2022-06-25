# A variable has a value of 10
types_of_people = 10
# We put a variable inside by formatting it.
x = f"There ar {types_of_people} types of people."

# A variable
binary = "binary"
# A variable
do_not = "don't"

# The same as before. But here we used two instead of one.
y = f"Those who know {binary} and those who {do_not}"

# Print x and y
print(x)
print(y)

# Print a text with a variable. We did this by formatting it.
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Hilarious has a value of False.
hilarious = False
# We put {} here. It can be formatted.
joke_evaluation = "isn't that joke so funny?! {}"

# Format {} with hilarious or replace it.
print(joke_evaluation.format(hilarious))

# W and e variables
w = "This is the left side of..."
e = "a string with a right side."

# Print the variables together. No spaces.
print(w + e)