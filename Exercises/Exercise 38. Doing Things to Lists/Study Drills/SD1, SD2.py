ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", 
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() # pop(more_stuff) | call pop on more_stuff
    print("Adding: ", next_one)
    stuff.append(next_one) # append(stuff, next_one) | call append on stuff and give it next_one variable
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa! fancy
print(stuff.pop()) # pop(stuff) | call pop on stuff
print(' '.join(stuff)) # what? cool! # join(stuff, ' ') | call join on stuff and give it ' ' string
print('#'.join(stuff[3:5])) # super stellar! # join(stuff[3:5]. '#') | call join on stuff[3:5] and give it '#' string