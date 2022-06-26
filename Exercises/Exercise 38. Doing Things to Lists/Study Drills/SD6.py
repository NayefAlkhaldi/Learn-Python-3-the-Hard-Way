# Let's do that!


def things(ten_things):
    print("Wait there are not 10 things in that list. Let's fix that.")

    stuff = ten_things.split(' ')
    more_stuff = ["Day", "Night", "Song", "Frisbee", 
                "Corn", "Banana", "Girl", "Boy"]

    while len(stuff) != 10:
        next_one = more_stuff.pop()
        print("Adding: ", next_one)
        stuff.append(next_one)
        print(f"There are {len(stuff)} items now.")

    print("There we go: ", stuff)

    print("Let's do some things with stuff.")

    print(stuff[1])
    print(stuff[-1]) # whoa! fancy
    print(stuff.pop())
    print(' '.join(stuff)) # what? cool!
    print('#'.join(stuff[3:5])) # super stellar!


ten_things_1 = "Apples Oranges Crows Telephone Light Sugar"
ten_things_2 = "Rabbits Loins Elephants Monkeys Penguins Dos"
ten_things_3 = "Noses Hands shoulders touses faces Lips Eyes"
ten_things_4 = "Computers mouses memories Keyboards Discs Hardwares"
ten_things_5 = "Red Orange Green Yellow Black White"
ten_things_6 = "Happy Sad Confuse Nervous Kind Worried"
ten_things_7 = "Shoeses Caps Sweaters Shorts Shirts Glasses"
ten_things_8 = "Roses Sunflowers Orchides Zinnias Panyses Gerberas"
ten_things_9 = "Penciles Books Pens Crayons Paint brushes Scissors"
ten_things_10 = "Cameras Lens Filters Flashes FrameCounters Tripods"

all_things = [ten_things_1, ten_things_2, ten_things_3,
              ten_things_4, ten_things_5, ten_things_6,
              ten_things_7, ten_things_8, ten_things_9,
              ten_things_10]

for stuff in all_things:
    things(stuff)