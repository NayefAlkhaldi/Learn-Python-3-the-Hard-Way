# The first module I read is random.

# link: https://www.geeksforgeeks.org/python-random-module/

# Examples I wrote:

import random

# Print a random number between 1 and 10
print(f"Let's choose a random number: {random.randint(1, 10)}? ok.")

# The second one was time.
# link: https://www.programiz.com/python-programming/time

# Calculate time between two moments
from time import time, sleep

start = time()
# wait a little
sleep(3)
end = time()

# Get the real number with abs() function
result = f"Time spent sleeping: {round(abs(start - end), 2)}"
print(result)

# The last one was the math module
# Link: https://www.tutorialsteacher.com/python/math-module#:~:text=The%20math%20module%20presents%20two%20angle%20conversion%20functions%3A,to%20180%20degrees%29.%20Example%3A%20Math%20Radians%20and%20Degrees

# My project
import math

area = input("Enter area: ")
area = area / 2

total_area = f"Total area (cm): {round(area ** 2 * math.pi, 2)}"
print(total_area)