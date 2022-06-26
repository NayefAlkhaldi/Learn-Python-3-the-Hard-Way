from ex42 import *

Dog.sound = 'woof!'
Cat.sound = 'meow'
Person.sound = 'hi'
Fish.sound = None

ralf = Dog("ralf")
pax = Cat("Pax")
adam = Person("adam")
sardine = Fish()

print(ralf.sound, pax.sound, adam.sound, sardine.sound)