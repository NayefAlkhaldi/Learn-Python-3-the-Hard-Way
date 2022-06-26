from sys import argv
# read the WYSS section for how to run this
script, name, age = argv

height = input("What's your height? ")

print("So, your name is {}. Your age is {}. Your height is {}. PERFECT!").format(name, age, height)