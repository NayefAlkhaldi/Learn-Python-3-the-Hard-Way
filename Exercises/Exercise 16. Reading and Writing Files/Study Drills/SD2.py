from sys import argv

script, filename = argv

file = open(filename)
print(f"Filename: {filename}")
print(f"Contest:\n{file.read()}")
file.close()