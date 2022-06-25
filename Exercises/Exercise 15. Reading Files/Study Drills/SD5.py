from sys import argv

script, filename = argv[0], input("Filename: ")

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

# That one was better...