from ex42 import *

Jack = Person("Jack")

Jack.pets = {'Cats': ['Olivia', 'Milo'], 'Dogs': ['Scotch', 'Brisket']}

dogs = Jack.pets['Dogs']
cats = Jack.pets['Cats']

print(dogs, cats)