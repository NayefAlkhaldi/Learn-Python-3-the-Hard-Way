# Main Imports =================================
from sys import exit, argv
from time import sleep
from textwrap import dedent
from random import randint, choice

# Files Imports
from scene import timer
from ending import finish
from character import person
from map_generator import map
from saving import save
# ================================================

script = argv

# Saving
saving_text = save()

# Player
if not (saving_text.GetLine("C:\\Users\\Nayef\\OneDrive - Ministry of Education\\Documents\\Python\\Learn Python 3 the Hard Way\\Exercise 45. You Make a Game\\ex45 game\\Game\\saving.txt", 'name', {})) and \
       (saving_text.GetLine("C:\\Users\\Nayef\\OneDrive - Ministry of Education\\Documents\\Python\\Learn Python 3 the Hard Way\\Exercise 45. You Make a Game\\ex45 game\\Game\\saving.txt", 'age', {})):

    player = person(input("Enter your name: "), input("Enter your age: "))

    saving_text.Switch('C:\\Users\\Nayef\\OneDrive - Ministry of Education\\Documents\\Python\\Learn Python 3 the Hard Way\\Exercise 45. You Make a Game\\ex45 game\\Game\\saving.txt', 1, str(player.name),)
    saving_text.Switch('C:\\Users\\Nayef\\OneDrive - Ministry of Education\\Documents\\Python\\Learn Python 3 the Hard Way\\Exercise 45. You Make a Game\\ex45 game\\Game\\saving.txt', 2, str(player.age),)
else:
    player = person(saving_text.GetLine("C:\\Users\\Nayef\\OneDrive - Ministry of Education\\Documents\\Python\\Learn Python 3 the Hard Way\\Exercise 45. You Make a Game\\ex45 game\\Game\\saving.txt", 'name', {}), 
    saving_text.GetLine("C:\\Users\\Nayef\\OneDrive - Ministry of Education\\Documents\\Python\\Learn Python 3 the Hard Way\\Exercise 45. You Make a Game\\ex45 game\\Game\\saving.txt", 'name', {}))

# Characters
friend_1 = person("Micheal", 21)
friend_2 = person("Mohammed", 22)
friend_3 = person("Noah", 18)

friends = [
    friend_1.name, friend_2.name, friend_3.name, 
    player.name
]

Player_inventory = ''

# Timer
first = timer()
last = timer()

# Timer start
start = first.begin()


# act 1
class home(object):
    def enter():
        global Player_inventory
        global saving_text

        saving_text.Switch('C:\\Users\\Nayef\\OneDrive - Ministry of Education\\Documents\\Python\\Learn Python 3 the Hard Way\\Exercise 45. You Make a Game\\ex45 game\Game\saving.txt', 3, 'home')

        while True:
            home_items = {
                '1': 'Camera',
                '2': 'Phone',
                '3': 'Gun',
                '4': 'Tire pumper',
                '5': 'Lamp'
            }

            print((
f"""
One day, the friends {', '.join(str(friend) for friend
in friends)} decided to go on a trip.
The promised day was Friday. When that day came, everyone
was meant to bring one of the trip stuff. Micheal and 
Mohammed are going bring food and water, Noah is going
to bring the tents. You're going to bring the camera
and the lamps. You went to your room and you found
5 stuff, every thing has it's own necessary and you
only can choose 3 of them:

1- {home_items['1']}
2- {home_items['2']}
3- {home_items['3']}
4- {home_items['4']}
5- {home_items['5']}
"""))
            items = input("[keypad>] ")
            selected_items = []
            
            for item in items.split():
                try:

                    if int(item) not in list(int(number) for number in home_items.keys()):
                        print("DOES NOT COMPUTE!")
                        Map('home')

                    else:
                        selected_items.append(item)

                except ValueError as error:
                    del error
                    continue

            if not len(selected_items) == 3:
                print("Three item only allowed!\n")
                return Map("home")


            count = 0

            for number in selected_items:
                count += 1

                if count != 3:
                    Player_inventory = Player_inventory + \
                                       f'{home_items[number]}, '

                else:
                    Player_inventory = Player_inventory + \
                                       home_items[number]


                if selected_items.count(number) > 1:
                    print("Please select three items\n")
                    return Map('home')
            saving_text.Switch('C:\\Users\\Nayef\OneDrive - Ministry of Education\\Documents\\Python\\Learn Python 3 the Hard Way\\Exercise 45. You Make a Game\\ex45 game\\Game\\saving.txt', 4, str(Player_inventory))
            return Map('woods')


# act 2
class woods(object):
    def enter():

        global start
        global player
        global Player_inventory
        global saving_text

        saving_text.Switch('C:\\Users\\Nayef\\OneDrive - Ministry of Education\\Documents\\Python\\Learn Python 3 the Hard Way\\Exercise 45. You Make a Game\\ex45 game\\Game\\saving.txt', 3, 'woods',)


        def search():

            print(
"""
Your friends went worried and decided to call police but...
there wasn't an internet connection. They thought about coming
back. When you took a look at the road, it was unfamiliar and
they didn't know how to get back. The friends decided to
walk forward into the woods and try to find someone for help.
They claimed all their stuff and they walked... and walked...
and walked but the road was the road was repeating itself!!!
they spent more than 2 days walking until they found an abandoned
house. They decided to stay a little while inside it just to take a
rest. But first, one of the friends must check out the house before going.
The chosen one was...
""")

            sleep(3)

            remaining = [friends[0], friends[1], friends[3]]
            chosen = choice(remaining)

            if chosen == player.name:
                print('you!\n')
                print(
"""
You went there to take a look. Nobody was there and the place
was looking safe.
""")

            else:
                print(f" {chosen}!\n")
                print(
f"""
{chosen} went there to take a look. Nobody was there and the place
was looking safe.
""")

                return Map('abandoned_house')


        print("""
Great choice!
After that, they took Noah's car and they. While the ride,
the car stopped immediately. Noah's knows a lot about cars,
so he checked it up and he found a nail inside the tire and
a lot of air has gone.
""")


        if 'Tire pumper' in Player_inventory:
            print(f"""
Luckily, you have a tire pumper, until now; everything
going on the plan. Finally, the friends have arrived.
They set up the camps and set up the fire. They were
too tired so everyone slept except {friend_3.name}, he
went to cut woods. At 12 Am, you woke up and you feel
something is missing... where is {friend_3.name}? he still
didn't come. Maybe something bad happend to him.
What should you do?

1- Search for him yourself.
2- Continue sleeping like something didn't happen.
""")

            selection = input("[Answer>] ")

            if selection == '1':
                print(
"""
After 40 minutes of searching around the woods,
you didn't find him.
Now you have to tell your friends about it.
""")
                search()

            elif selection == '2':
                print(f"""
You neglected your friend, you're a bad friend!
The next day, your friends relized that {friend_3.name}
is missing.
""")

                search()

            else:
                print("DOES NOT COMPUTE!\n")
                return Map("woods")


        else:
            ending_text = (
"""
There wasn't a tire pump so the friends decided to go walking until the
nearest wood and not the wood from the plan. You really enjoyed your time with
your friends, you had the best moments in your life.
""")

            end = last.end()

            return finish.end(ending_text, True, Map, 
                              timer.result(start, end))

# act 3
class abandoned_house(object):

    def enter():
        global start
        global saving_text

        saving_text.Switch('C:\\Users\\Nayef\\OneDrive - Ministry of Education\\Documents\\Python\\Learn Python 3 the Hard Way\\Exercise 45. You Make a Game\\ex45 game\\Game\\saving.txt', 3, 'abandoned_house',)

        def stay():
            while True:
                print(f"You choosed... to stay with {friends[1]}\n")
                print(
f"""
{friends[1]}: don't listen to that him because outside is very dangerous. He'll die!
you and him found a small room and {friends[1]} put the sleeping bag and slept.
But you can't now sleep, you feel something is weird. After 2 hours, and you still awake,
you heard someone slapped the door. You thought it was the air but you heard another sound..
a sound of someone screaming. Maybe ghosts are angry, are you still want to stay(y/n)?
""")

                choice = input("? ")

                if choice == 'n':
                    ending_text = """
You choosed... to run!!
You quickly took all your necessary stuff and you got out of the house.
you've been walking for 2 days and you finally got out of the woods!
                    """

                    end = last.end()

                    return finish.end(ending_text, True, Map, 
                                      timer.result(start, end))



                elif choice == 'y':
                    ending_text = (
"""
You've been insist on staying. You made a really bad decision.
After a few minutes, you saw a big monster and the monster ate you and 
your friend.
""")

                    status = finish()
                    end = last.end()


                    return finish.end(ending_text, False, Map, 
                                      timer.result(start, end),)
                else:
                    print("DOES NOT COMPUTE!\n")
                    continue

        def walk():
            ending_text = (
f"""
You choosed... not to stay.
After 2 days...
You found a car! You asked for help And you got in their car.
While they were driving they.. Boom! hit another car.
""")
            status = finish()
            end = last.end()


            return finish.end(ending_text, False, Map)

        print(
f"""
The friends entered the house... There was lots of spiders and weird sounds 
like now.. there is a crying baby sound..
{friends[1]}: we don't have anything to do else. So we will stay here this night... Only!

But {friends[0]} doesn't want to stay; he says that he doesn't feel comfortable here.
So he will leave this house and continue walking alone in woods.
""")

        choice = input(f"""
What do you think?

1- stay with {friend_2.name}
2- Go with {friend_1.name}?
        """)

        if choice == '1':
            stay()

        elif choice == '2':
            walk()

        else:
            print("DOES NOT COMPUTE!\n")
            return Map('abandoned_house')


main_map = map()
collected_places = main_map.collect(
                   home='home.enter()', woods='woods.enter()',
                   abandoned_house='abandoned_house.enter()', 
                   returning_to_home='returning_to_home.enter(),'
                )


Map = lambda str: exec(collected_places.get(str))


class main:
    older_saving = saving_text.GetLine('C:\\Users\\Nayef\\OneDrive - Ministry of Education\\Documents\\Python\\Learn Python 3 the Hard Way\\Exercise 45. You Make a Game\\ex45 game\\Game\\saving.txt', 'place', {}).split()[2]

    if older_saving == 'None':
        Map('home')

    else:
        Map(older_saving)