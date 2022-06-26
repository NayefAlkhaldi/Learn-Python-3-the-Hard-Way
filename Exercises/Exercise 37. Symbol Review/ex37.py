# This is the table of examples.
from sys import exit

# and
x = 10
z = [5, 10, 15]

if x == 10 and x in z:
    print('foo')

# as
import tkinter as tk

# assert. This won't work on some editors
def divide(x, y) -> int:
    try:
        assert x or y <= 0, "Invalid Operator"
    except AssertionError as my_error:
        print(my_error)
    return abs(x / 2)

divide(0, 1)

# break
x = 10
while True:
    print(x)
    if x <= 0:
        break
    x -= 1

# class
class person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

Arron = person("Arron", "27")
print(Arron.name, Arron.age)

# continue
for i in range(10):
    if i == 0:
        continue
    print(i, end=' ')

# def
def convert_cm_to_foot(foot):
    return foot * 30.48

print(convert_cm_to_foot(6.11))

# del
data = [13, 432, 545, 130]
del data[0]
print(data)

# elif
fruit = 'apple'
if fruit == 'orange':
    print("Oh, I love oranges.")
elif fruit == 'apple':
    print("Oh, I hate apples.")

# else
foo = 10
bar = 38

if foo + bar > 190:
    print("foo and bar are a big numbers.")
else:
    print("foo and bar are small numbers.")

# except
try:
    0 // 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# exec
code = exec('print("Hello, world!")')

# finally
x = 'foo'
try:
    x > 5
except TypeError:
    print("Something went wrong.")
finally:
    print("I'm still here.")

# for
my_list = ['b', 'a', 'r']

for element in my_list:
    print(element)

# from
from math import pi
circle_area = pi * 17.5 ** 2
print(circle_area)

# global
# Avoid 'x' referenced before assignment error
x = 50

def change():
    global x
    x /= 2
change()
print(x)

# if
foo = 'foo'
bar = 'bar'

if foo != bar:
    print("They're not the same.")

# import
import os

# in
__list__ = ['a', 'b', 'c']
print('List' in __list__)

# is
y = None
print(y is None)

# lambda
convert_kilometers_to_miles = lambda x: x / 1.609344
miles = convert_kilometers_to_miles(75)
print(miles)

# not
j = False
print(j is not False)

# or
print(True or False != None)

# pass
def func() -> str:
    pass

# print
print("This is a text.")

# raise
try:
    raise TypeError("ERroR")
except Exception as error:
    print(error)

# return
def split(string):
    return string.split()

x = """The people who walked in darkness
       Awaken to see a great light"""
x = split(x)
print(x)

# try
try:
    print("Hello, world!")
finally:
    print("Hello, world!")

# while
a = []
count = 0

while len(a) < 30:
    a.append(str(count))
    count += 1

print(a)

# with
# You don't actually have to close the file if you used with statement.
with open("C:\\Users\\Nayef\\Documents\\sample.txt") as file:
    print(file.read())

# yield
# This might requires a little bit of understanding generators objects.
def test():
    x = 10
    yield x

output = test()
for i in output:
    print(i)

# True
print(10 > 5)

# False
print(10 < 5)

# None
def func():
    pass

print(func() is None)

# bytes
Text = b'Text'
print(type(Text) == bytes)
Text = Text.decode()
print(type(Text) == str)

# strings
x = 'string'
print(type(x) == str)

# numbers
i = 20
print(type(i) == int)

# floats
i = 20.0
print(type(i) == float)

# lists
l = []
print(type(l) == list)

# dicts
x = {'A': 'a', 'B': 'b', 'C': 'c'}
#         a key ^    ^ a value
print(x['B'])
#     ^ A dicitionary. B is a key where we are trying to print the value.

# \\
print("Correct way to print slashes: \\")

# \'
print('Correct way to print single quotes: you\'re')

# \"
print("Correct way to print double qoutes: \"hi\"")

# \a "Only works on terminal."
print("Do you hear that? \a")

print("foo\bo")

# \f
print("Who likes..\fspaghetti?")

# \n
print("*************\n*************\n*************")

# \r
print("POOP.\rI'm not hiding anything ;)")

# \t
print("This should be tabbed\t<HERE")

# \v
print("Vertical tab escape is the same as \\n\vI told ya.")

# %d
integer = 10
print("This should be 10: %d" % integer)

# %i
floating = 10.0
print("This should be 10.0: %i" % floating)

# %o
octal = 2000
print("This should be 3750: %o" % octal)

# %u
print("This should be 500: %u" % 500)

# %x
print("Now! This should be 0x78: %x" % 120)

# %X
print("Now! This should be 0x78: %X" % 120)

# %e
print("This should be 1.000000e+02: %e" % 100)

# %E
print("This should be 1.000000e+02: %E" % 100)

# %f
print("This should be 20.500000: %f" % 20.5)

# %F
print("This should be 20.500000: %F" % 20.5)

# %g
print("This should be 60.76: %g" % 60.7649382)

# %G
print("This should be 60.76: %G" % 60.7649382)

# %c
print("This should be A: %c" % 65)

# %r
x = "Text"
print("This should be <type 'str'>: %r" % type(x))

# %s
print("This should be 'Hello there': %s % 'Hello, there'")

# '%%'
print("This should be 50.57%%: %g%%" % 50.57)

# +
print(2 + 7 == 9)

# -
print(5 - 10 == -5)

# *
print(8 * 8 == 64)

# **
print(5 ** 3 == 125)

# /
print(15 / 2 == 7.5)

# //
print(15 // 2 == 7)

# %
print(50 % 5 == 0)

# <
print(4 < 10)

# >
print(10 > 4)

# <=
print(5 <= 6)

# >=
print(6 >= 6)

# ==
print(100 == 100)

# !=
print(105 != 100)

# ( )

print(abs(-5.3))

# [ ]
x = [1, 2, 3]
print(x[0])

# { }
y = {'key': 'value'}
print(y)

# @
def reverse(func):
    def wrapper(name):
        return name[::-1].lower()
    return wrapper

@reverse
def reverse_name(name):
    return name

print(reverse_name('Oliver'))

# ,
x, y = 10, 10
print(x, y)

# :
def example(): pass

# .
import random
print(random.randint(0, 10))

# =
bar = 0
print(bar)

# ;
def foo(): bar=10;foobar=15

# +=
z = 0
z += 10

# -=
z -= 15

# *=
z *= 3.5

# /=
z /= 2

# //=
z //= 3

# %=
z %= 12

# **=
z **= 3
print(z)
exit(0)